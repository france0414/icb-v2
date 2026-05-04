"""
Refresh PROJECT_SITE.json from a live Odoo site.

Usage:
  python scripts/update_project_site_assets.py https://demo.example.com

This script:
1. Fetches the provided page URL
2. Extracts current stylesheet links from the HTML
3. Keeps Odoo /web/assets/*.css bundles
4. Writes docs/design/PROJECT_SITE.json with current liveUrl and assetBundles
"""

from __future__ import annotations

import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from html import unescape
from pathlib import Path

DEFAULT_SSL_CONTEXT = ssl.create_default_context()
INSECURE_SSL_CONTEXT = ssl._create_unverified_context()

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECT_SITE_JSON = REPO_ROOT / "docs" / "design" / "PROJECT_SITE.json"

LINK_RE = re.compile(r"<link[^>]+rel=[\"'][^\"']*stylesheet[^\"']*[\"'][^>]*href=[\"']([^\"']+)[\"'][^>]*>", re.IGNORECASE)
HREF_RE = re.compile(r"href=[\"']([^\"']+)[\"']", re.IGNORECASE)
ASSET_NAME_RE = re.compile(r"/web\.assets_([a-z0-9_\-]+)\.min\.css", re.IGNORECASE)


def normalize_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
        parsed = urllib.parse.urlparse(url)
    if not parsed.netloc:
        raise ValueError(f"無效網址: {url}")
    return parsed.geturl()


def fetch_html(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0 Safari/537.36"
        },
    )
    contexts = [DEFAULT_SSL_CONTEXT, INSECURE_SSL_CONTEXT]
    last_error: Exception | None = None
    for idx, context in enumerate(contexts):
        try:
            with urllib.request.urlopen(req, timeout=30, context=context) as resp:
                charset = resp.headers.get_content_charset() or "utf-8"
                if idx == 1:
                    print("⚠️  SSL 憑證驗證失敗，已退回 insecure 模式抓取 HTML")
                return resp.read().decode(charset, errors="replace")
        except urllib.error.URLError as exc:
            last_error = exc
            if idx == 0 and isinstance(exc.reason, ssl.SSLCertVerificationError):
                continue
            raise
    if last_error:
        raise last_error
    raise RuntimeError("抓取網址失敗")


def asset_sort_key(item: tuple[str, str]) -> tuple[int, str]:
    key, _ = item
    if key == "common_css":
        return (0, key)
    if key == "frontend_css":
        return (1, key)
    if key == "frontend_lazy_css":
        return (2, key)
    return (9, key)


def keep_preferred_bundles(bundles: dict[str, str]) -> dict[str, str]:
    filtered = {key: value for key, value in bundles.items() if key in {"common_css", "frontend_css", "frontend_lazy_css"}}
    if filtered:
        return dict(sorted(filtered.items(), key=asset_sort_key))
    return dict(sorted(bundles.items(), key=asset_sort_key))


def infer_live_url(requested_url: str, stylesheet_urls: list[str]) -> str:
    requested = urllib.parse.urlsplit(requested_url)
    if stylesheet_urls:
        first_asset = urllib.parse.urlsplit(stylesheet_urls[0])
        if first_asset.scheme and first_asset.netloc:
            return f"{first_asset.scheme}://{first_asset.netloc}"
    return f"{requested.scheme}://{requested.netloc}"


def validate_asset_urls(live_url: str, asset_bundles: dict[str, str]) -> list[str]:
    live = live_url.rstrip("/")
    valid: list[str] = []
    for key, relative in asset_bundles.items():
        asset_url = urllib.parse.urljoin(live + "/", relative.lstrip("/"))
        req = urllib.request.Request(asset_url, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=20, context=INSECURE_SSL_CONTEXT) as resp:
                if 200 <= resp.status < 400:
                    valid.append(key)
        except Exception:
            continue
    return valid


def make_note(valid_keys: list[str]) -> str:
    base_note = "asset hash 會隨 Odoo 更新、SCSS/theme 調整而變動。preview 前若有案件網址，應先重新抓取目前 <link rel=stylesheet> 中的 /web/assets/*.css 後再更新此檔。"
    if valid_keys:
        return base_note + f" 已驗證可用 bundle: {', '.join(valid_keys)}。"
    return base_note + " 本次尚未完成 bundle 可用性驗證。"


def display_asset_url(live_url: str, relative: str) -> str:
    return urllib.parse.urljoin(live_url.rstrip("/") + "/", relative.lstrip("/"))


def load_existing_project_site() -> dict:
    if PROJECT_SITE_JSON.exists():
        try:
            return json.loads(PROJECT_SITE_JSON.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def parse_cli_args(argv: list[str]) -> tuple[str, bool]:
    args = argv[1:]
    no_verify = False
    filtered: list[str] = []
    for arg in args:
        if arg == "--no-verify":
            no_verify = True
        else:
            filtered.append(arg)
    if not filtered:
        raise ValueError("用法: python scripts/update_project_site_assets.py <案件網址> [--no-verify]")
    return filtered[0], no_verify


def update_project_site(url: str, verify_assets: bool = True) -> dict:
    html = fetch_html(url)
    stylesheet_urls = extract_stylesheet_links(html, url)
    asset_bundles = collect_odoo_css_bundles(stylesheet_urls, url)
    if not asset_bundles:
        raise RuntimeError("找不到 /web/assets/*.css，未更新 PROJECT_SITE.json")

    live_url = infer_live_url(url, stylesheet_urls)
    asset_bundles = keep_preferred_bundles(asset_bundles)
    valid_keys = validate_asset_urls(live_url, asset_bundles) if verify_assets else []
    existing = load_existing_project_site()
    payload = {
        "liveUrl": live_url,
        "assetBundles": asset_bundles,
        "assetsCheckedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "assetBundlesVerified": verify_assets,
        "verifiedBundleKeys": valid_keys,
        "note": make_note(valid_keys),
    }
    if existing.get("liveUrl") and existing["liveUrl"] != live_url:
        payload["previousLiveUrl"] = existing["liveUrl"]
    PROJECT_SITE_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload


def print_update_summary(payload: dict) -> None:
    print(f"✅ 已更新 {PROJECT_SITE_JSON}")
    print(f"🌐 liveUrl: {payload['liveUrl']}")
    if payload.get("previousLiveUrl"):
        print(f"↩️  previousLiveUrl: {payload['previousLiveUrl']}")
    print("🎨 assetBundles:")
    for key, value in payload["assetBundles"].items():
        print(f"  - {key}: {value}")
        print(f"    ↳ {display_asset_url(payload['liveUrl'], value)}")
    if payload.get("assetBundlesVerified"):
        verified = payload.get("verifiedBundleKeys", [])
        if verified:
            print(f"🔎 已驗證 bundle: {', '.join(verified)}")
        else:
            print("⚠️  尚未驗到可用 bundle，請人工確認站台是否需登入或改用前台頁網址")
    else:
        print("ℹ️  本次未執行 asset URL 驗證")


def sync_preview_assets(url: str, verify_assets: bool = True) -> dict:
    payload = update_project_site(url, verify_assets=verify_assets)
    print_update_summary(payload)
    return payload


def cli_main(argv: list[str]) -> int:
    try:
        input_url, no_verify = parse_cli_args(argv)
        live_url = normalize_url(input_url)
    except ValueError as exc:
        print(f"❌ {exc}")
        return 1

    try:
        sync_preview_assets(live_url, verify_assets=not no_verify)
    except urllib.error.URLError as exc:
        print(f"❌ 抓取網址失敗: {exc}")
        return 1
    except RuntimeError as exc:
        print(f"❌ {exc}")
        return 1
    return 0


# CLI entry point stays at end of file so helper functions are defined first.


def extract_stylesheet_links(html: str, base_url: str) -> list[str]:
    matches = LINK_RE.findall(html)
    if not matches:
        matches = []
        for tag in re.findall(r"<link[^>]+>", html, flags=re.IGNORECASE):
            if "stylesheet" not in tag.lower():
                continue
            href_match = HREF_RE.search(tag)
            if href_match:
                matches.append(href_match.group(1))

    urls: list[str] = []
    for href in matches:
        href = unescape(href.strip())
        if not href:
            continue
        urls.append(urllib.parse.urljoin(base_url, href))
    return urls


def collect_odoo_css_bundles(urls: list[str], live_url: str) -> dict[str, str]:
    bundles: dict[str, str] = {}
    live_origin = urllib.parse.urlsplit(live_url)
    live_base = f"{live_origin.scheme}://{live_origin.netloc}"

    for full_url in urls:
        parsed = urllib.parse.urlsplit(full_url)
        if parsed.netloc != live_origin.netloc:
            continue
        match = ASSET_NAME_RE.search(parsed.path)
        if not match:
            continue
        bundle_name = match.group(1).replace("-", "_") + "_css"
        relative = parsed.path
        if parsed.query:
            relative += "?" + parsed.query
        bundles[bundle_name] = relative

    preferred_order = [
        "common_css",
        "frontend_css",
        "frontend_lazy_css",
        "website_assets_editor_css",
    ]
    ordered: dict[str, str] = {}
    for key in preferred_order:
        if key in bundles:
            ordered[key] = bundles[key]
    for key, value in bundles.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


if __name__ == "__main__":
    raise SystemExit(cli_main(sys.argv))
