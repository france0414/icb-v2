#!/usr/bin/env python3
"""
Auto convert Stitch/HTML input into Odoo XML+SCSS and build local preview.

Usage:
  python scripts/auto_convert_preview.py --input clientinfo/<folder>
  python scripts/auto_convert_preview.py --input clientinfo/<folder>/code.html --homepage
  python scripts/auto_convert_preview.py --input <path> --live-url https://example.com --no-open
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import webbrowser
from datetime import datetime
from pathlib import Path

os.environ.setdefault("PYTHONIOENCODING", "utf-8")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from normalize_ai_build import ensure_scss_rules, normalize_xml, write_report
from update_project_site_assets import normalize_url, sync_preview_assets
from build_preview import build_preview

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = REPO_ROOT / "outputs"
DEFAULT_HTML_NAMES = ("code.html", "index.html")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert Stitch/HTML into Odoo XML+SCSS and preview it")
    parser.add_argument("--input", required=True, help="Input HTML file or folder containing code.html")
    parser.add_argument("--homepage", action="store_true", help="Wrap output as homepage with pageName=homepage")
    parser.add_argument("--live-url", help="Frontend live URL for refreshing preview assets before build")
    parser.add_argument("--name", help="Override output slug")
    parser.add_argument("--no-open", action="store_true", help="Do not open preview in the browser")
    return parser.parse_args()


def resolve_html_input(raw_input: str) -> Path:
    path = Path(raw_input)
    if not path.is_absolute():
        path = REPO_ROOT / path
    path = path.resolve()

    if path.is_dir():
        for candidate in DEFAULT_HTML_NAMES:
            html_path = path / candidate
            if html_path.exists():
                return html_path
        raise FileNotFoundError(f"找不到 HTML 檔案，請在資料夾內提供 {', '.join(DEFAULT_HTML_NAMES)}")

    if not path.exists():
        raise FileNotFoundError(f"找不到輸入路徑: {path}")
    return path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "stitch_page"


def derive_output_name(html_path: Path, explicit_name: str | None, homepage: bool) -> str:
    if explicit_name:
        return slugify(explicit_name)

    base = html_path.parent.name if html_path.name in DEFAULT_HTML_NAMES else html_path.stem
    base_slug = slugify(base)
    if homepage and "home" not in base_slug:
        return f"{base_slug}_home"
    return base_slug


def extract_body(html_text: str) -> str:
    match = re.search(r"<body[^>]*>([\s\S]*?)</body>", html_text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return html_text.strip()


def sanitize_html_fragment(fragment: str) -> str:
    fragment = re.sub(r"<script\b[^>]*>[\s\S]*?</script>", "", fragment, flags=re.IGNORECASE)
    fragment = re.sub(r"on[a-z]+\s*=\s*(['\"]).*?\1", "", fragment, flags=re.IGNORECASE)
    return fragment.strip()


def ensure_sections(fragment: str) -> str:
    if re.search(r"<section\b", fragment, re.IGNORECASE):
        return fragment
    return (
        '<section data-snippet="s_text_block" class="s_text_block o_colored_level pt64 pb64" '
        'data-name="Text" data-custom-name="ImportedHtml">\n'
        '  <div class="container">\n'
        f'{indent_html(fragment, 4)}\n'
        '  </div>\n'
        '</section>'
    )


def indent_html(text: str, spaces: int) -> str:
    prefix = " " * spaces
    return "\n".join(prefix + line if line.strip() else line for line in text.splitlines())


def wrap_odoo_xml(fragment: str, name: str, homepage: bool) -> str:
    homepage_line = "\n    <t t-set=\"pageName\" t-value=\"'homepage'\"/>" if homepage else ""
    return (
        f'<t t-name="website.{name}">\n'
        '  <t t-call="website.layout">'
        f'{homepage_line}\n'
        '    <div id="wrap" class="oe_structure oe_empty">\n'
        f'{indent_html(fragment, 6)}\n'
        '    </div>\n'
        '  </t>\n'
        '</t>\n'
    )


def default_scss(name: str) -> str:
    block = name.replace("_", "-")
    return (
        f'.s_custom_{block} {{\n'
        '  h1,\n'
        '  h2,\n'
        '  h3,\n'
        '  h4,\n'
        '  h5,\n'
        '  h6 {\n'
        '    line-height: 1.2;\n'
        '  }\n'
        '}\n'
    )


def write_mapping(mapping_path: Path, name: str, homepage: bool, source_path: Path) -> None:
    lines = [
        "# Stitch Mapping",
        "",
        f"- source: `{source_path}`",
        f"- output: `{name}`",
        f"- homepageMode: {'yes' if homepage else 'no'}`",
        "",
        "# Manual follow-up",
        "# - refine imported classes into project-specific s_custom_* blocks when needed",
        "# - replace placeholder spacing/utilities with final Odoo spacing rhythm",
    ]
    mapping_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_strict_final(strict_xml: Path, strict_scss: Path, xml_text: str, scss_text: str) -> None:
    strict_xml.write_text(xml_text, encoding="utf-8", newline="\n")
    strict_scss.write_text(scss_text, encoding="utf-8", newline="\n")


def main() -> int:
    args = parse_args()

    try:
        html_path = resolve_html_input(args.input)
    except FileNotFoundError as exc:
        print(f"❌ {exc}")
        return 1

    output_name = derive_output_name(html_path, args.name, args.homepage)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    xml_path = OUTPUTS_DIR / f"{output_name}.xml"
    scss_path = OUTPUTS_DIR / f"{output_name}.scss"
    mapping_path = OUTPUTS_DIR / f"{output_name}.mapping.scss"
    strict_xml_path = OUTPUTS_DIR / f"{timestamp}_{output_name}_strict_final.xml"
    strict_scss_path = OUTPUTS_DIR / f"{timestamp}_{output_name}_strict_final.scss"

    html_text = html_path.read_text(encoding="utf-8", errors="replace")
    fragment = ensure_sections(sanitize_html_fragment(extract_body(html_text)))
    wrapped_xml = wrap_odoo_xml(fragment, output_name, args.homepage)
    xml_path.write_text(wrapped_xml, encoding="utf-8", newline="\n")
    scss_path.write_text(default_scss(output_name), encoding="utf-8", newline="\n")

    normalized_xml_text, xml_changes = normalize_xml(xml_path)
    scss_additions = ensure_scss_rules(scss_path, normalized_xml_text)
    report_path = write_report(xml_path, xml_changes, scss_additions)
    final_scss_text = scss_path.read_text(encoding="utf-8")
    write_mapping(mapping_path, output_name, args.homepage, html_path)
    write_strict_final(strict_xml_path, strict_scss_path, normalized_xml_text, final_scss_text)

    if args.live_url:
        try:
            sync_preview_assets(normalize_url(args.live_url), verify_assets=True)
        except Exception as exc:
            print(f"⚠️  更新 live assets 失敗，改用現有/fallback preview asset：{exc}")

    preview_path = build_preview(xml_path, final_scss_text)

    print(f"✅ XML: {xml_path.relative_to(REPO_ROOT)}")
    print(f"✅ SCSS: {scss_path.relative_to(REPO_ROOT)}")
    print(f"✅ Report: {report_path.relative_to(REPO_ROOT)}")
    print(f"✅ Mapping: {mapping_path.relative_to(REPO_ROOT)}")
    print(f"✅ Strict final XML: {strict_xml_path.relative_to(REPO_ROOT)}")
    print(f"✅ Strict final SCSS: {strict_scss_path.relative_to(REPO_ROOT)}")
    print(f"✅ Preview: {preview_path.relative_to(REPO_ROOT)}")

    if not args.no_open:
        webbrowser.open(preview_path.as_uri())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
