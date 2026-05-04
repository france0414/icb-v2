"""
Odoo Local Preview Builder
==========================
用法: python scripts/build_preview.py [XML 檔案路徑]
範例: python scripts/build_preview.py outputs/2026-03-09_homepage.xml

此腳本會：
1. 讀取指定的 Odoo XML 檔案
2. 去掉 QWeb 語法（<t t-call>, <t t-set> 等），只保留 HTML 結構
3. 編譯 docs/design/user_custom_rules.scss → preview/custom.css
4. 產出 preview/index.html，引入：
   - 測試機的完整 Odoo CSS (遠端)
   - 局部自訂 CSS (本地編譯)
5. 自動開啟瀏覽器預覽
"""

import json
import re
import subprocess
import sys
import webbrowser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PREVIEW_DIR = REPO_ROOT / "preview"
SCSS_SOURCE = PREVIEW_DIR / "_preview_entry.scss"  # Bootstrap mixin shim + @import user_custom_rules
CUSTOM_CSS_OUTPUT = PREVIEW_DIR / "custom.css"
PROJECT_SITE_JSON = REPO_ROOT / "docs" / "design" / "PROJECT_SITE.json"

# Fallback：若未建立 PROJECT_SITE.json，使用 Odoo 原廠預設站（舊行為）
FALLBACK_CSS_URLS = [
    "https://demo-design.gtmc.app/web/assets/4486-0aa6846/1/web.assets_frontend.min.css",
]


def load_odoo_css_urls() -> list[str]:
    """讀 docs/design/PROJECT_SITE.json 組出 CSS URL 清單；找不到則 fallback。"""
    if not PROJECT_SITE_JSON.exists():
        print(f"ℹ️  未找到 {PROJECT_SITE_JSON.name}，使用 fallback（demo-design 原廠站）")
        return FALLBACK_CSS_URLS

    try:
        cfg = json.loads(PROJECT_SITE_JSON.read_text(encoding="utf-8"))
        base = cfg["liveUrl"].rstrip("/")
        bundles = cfg.get("assetBundles", {})
        urls = [base + path for key, path in bundles.items() if key.endswith("_css")]
        if not urls:
            print(f"⚠️  {PROJECT_SITE_JSON.name} 沒有 *_css bundle，fallback")
            return FALLBACK_CSS_URLS
        print(f"🌐 預覽 CSS 來源：{base}（{len(urls)} 個 bundle）")
        return urls
    except Exception as e:
        print(f"⚠️  讀取 {PROJECT_SITE_JSON.name} 失敗：{e}，fallback")
        return FALLBACK_CSS_URLS

PREVIEW_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Odoo Preview — {title}</title>

    <!-- 1. Odoo 測試機完整 CSS (Bootstrap 4 + 原生樣式) -->
{odoo_css_links}

    <!-- 2. FontAwesome 4 (Odoo 15 使用的版本) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- 3. 本地編譯的自訂 SCSS → CSS -->
    <link rel="stylesheet" href="custom.css">

    <!-- 4. 頁面特定的額外 SCSS (若有) -->
    <style>
{page_css}
    </style>
</head>
<body>
    <div id="wrapwrap" class="homepage">
        <main>
            <div id="wrap" class="oe_structure oe_empty">
{content}
            </div>
        </main>
    </div>

    <!-- Bootstrap 4 JS (for carousel, collapse, etc.) -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js"></script>
</body>
</html>
"""


def compile_scss() -> None:
    """編譯 user_custom_rules.scss → preview/custom.css"""
    if not SCSS_SOURCE.exists():
        print(f"⚠️  找不到 SCSS 來源: {SCSS_SOURCE}")
        print("   將跳過自訂樣式編譯，preview 只會載入測試機 CSS。")
        CUSTOM_CSS_OUTPUT.write_text("/* user_custom_rules.scss not found */\n", encoding="utf-8")
        return

    print(f"🔧 編譯 SCSS: {SCSS_SOURCE.name} → custom.css")
    result = subprocess.run(
        f'npx sass --no-source-map --style=compressed "{SCSS_SOURCE}" "{CUSTOM_CSS_OUTPUT}"',
        capture_output=True,
        text=True,
        shell=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        err_msg = (result.stderr or "")[:500]
        print(f"⚠️  SCSS 編譯有警告或錯誤（但仍繼續）:\n{err_msg}")
        # 如果完全失敗，寫一個空 CSS
        if not CUSTOM_CSS_OUTPUT.exists():
            CUSTOM_CSS_OUTPUT.write_text(f"/* SCSS compile error */\n", encoding="utf-8")
    else:
        size_kb = CUSTOM_CSS_OUTPUT.stat().st_size / 1024
        print(f"✅ 編譯成功！custom.css ({size_kb:.1f} KB)")


def strip_qweb(xml_content: str) -> str:
    """去掉 QWeb 語法，只保留 HTML 結構，並替換 Odoo 圖片路徑"""
    # 移除 <t t-name="..."> 與 </t> 包覆
    content = re.sub(r'<t\s+t-name="[^"]*"\s*>', '', content := xml_content)
    content = re.sub(r'<t\s+t-call="[^"]*"\s*>', '', content)
    content = re.sub(r'<t\s+t-set="[^"]*"\s+t-value="[^"]*"\s*/>', '', content)
    content = re.sub(r'</t>', '', content)

    # 移除 data-original-title, aria-describedby 等冗餘屬性 (減少噪音)
    content = re.sub(r'\s*data-original-title="[^"]*"', '', content)
    content = re.sub(r'\s*aria-describedby="[^"]*"', '', content)
    content = re.sub(r'\s*title=""', '', content)

    # 替換 Odoo 內部圖片路徑為 picsum.photos 佔位圖
    # 匹配 /web/image/... 格式的路徑
    img_counter = [0]
    def replace_odoo_img(match):
        img_counter[0] += 1
        seed = img_counter[0] * 100  # 讓每張圖不同
        return f'https://picsum.photos/seed/{seed}/1920/800'
    
    content = re.sub(r'/web/image/[^"\)\s]+', replace_odoo_img, content)

    return content.strip()


# ==========================================================
# Odoo-aware lint：抓常見錯誤，加速除錯循環
# 規則只警告不阻擋，呼叫端自行決定是否修正
# ==========================================================
VOID_TAGS = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
ODOO_SELF_CLOSE_OK = {"t","xpath","attribute","field","record","data"}

def lint_odoo_xml(xml_text: str, xml_path: Path, scss_text: str = "") -> list[str]:
    """回傳警告訊息清單。針對 Odoo 專案的常見錯誤。"""
    warnings: list[str] = []

    # 1) 自閉合非 void / 非 QWeb 標籤 → HTML5 會誤解為 opening tag
    for m in re.finditer(r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?/>', xml_text):
        tag = m.group(1).lower()
        if tag in VOID_TAGS or tag in ODOO_SELF_CLOSE_OK:
            continue
        line = xml_text[:m.start()].count("\n") + 1
        warnings.append(f"L{line}: <{tag}/> 自閉合非 void 標籤，瀏覽器會吞掉後續 DOM，改 <{tag}></{tag}>")

    # 2) s_dynamic_snippet_* 內禁止手刻卡片
    for m in re.finditer(r'<section[^>]*class="[^"]*s_dynamic_snippet_[^"]*"[^>]*>([\s\S]*?)</section>', xml_text):
        body = m.group(1)
        if re.search(r'<div[^>]*class="[^"]*\bcard\b', body) or re.search(r'<div[^>]*class="[^"]*o_carousel_product_card', body):
            line = xml_text[:m.start()].count("\n") + 1
            warnings.append(f"L{line}: s_dynamic_snippet_* 內出現手刻卡片標記，dynamic snippet 是 locked 結構由 Odoo runtime 渲染，不可預置假卡片")

    # 3) 首頁必須有 pageName='homepage'
    name = xml_path.stem.lower()
    if "home" in name and 't-call="website.layout"' in xml_text:
        if not re.search(r"""pageName["']?\s*t-value\s*=\s*["']\s*'homepage'""", xml_text) \
           and not re.search(r"""t-set\s*=\s*["']pageName["']\s+t-value\s*=\s*["']'homepage'""", xml_text):
            warnings.append("首頁範本缺少 <t t-set=\"pageName\" t-value=\"'homepage'\"/>（首頁專屬必加）")

    # 4) Footer 必須用 xpath inherit，不可裸 <div id="footer">
    if "footer" in name:
        if '<div id="footer"' in xml_text and 'inherit_id="website.layout"' not in xml_text:
            warnings.append("Footer 缺少 xpath 繼承外框，應包在 <data inherit_id=\"website.layout\"><xpath expr=\"//div[@id='footer']\" position=\"replace\"> 內")

    # 5) stretched-link 反模式（應用 s_custom_cardLink::before 替代）
    if re.search(r'class="[^"]*\bstretched-link\b', xml_text):
        warnings.append("偵測到 stretched-link：本專案改用 s_custom_clickableCard + s_custom_cardLink::before overlay，避免編輯器無法點選內文")

    # 6) SCSS 啟發式：:hover 有 transform: scale 但同層 selector 無 overflow: hidden
    if scss_text:
        for m in re.finditer(r'([^\{\}]+?)\{\s*[^}]*?:hover[^}]*?transform\s*:\s*scale', scss_text):
            sel = m.group(1).strip().splitlines()[-1]
            # 粗略檢查：該 selector（去掉 :hover）是否有 overflow: hidden
            base_sel = re.sub(r':hover.*$', '', sel).strip()
            if base_sel and f"overflow: hidden" not in scss_text and f"overflow:hidden" not in scss_text:
                warnings.append(f"SCSS: '{base_sel[:60]}' 有 hover scale 但未見 overflow: hidden，hover 可能超出卡片範圍")
                break  # 提一次就好

    return warnings


def build_preview(xml_path: Path, page_css: str = "") -> Path:
    """從 XML 檔案建立預覽 HTML"""
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 編譯 SCSS
    compile_scss()

    # 2. 讀取 XML 並清理
    raw_xml = xml_path.read_text(encoding="utf-8")

    # 2.5 Odoo-aware lint
    scss_sibling = xml_path.with_suffix(".scss")
    scss_text = scss_sibling.read_text(encoding="utf-8") if scss_sibling.exists() else ""
    lint_warnings = lint_odoo_xml(raw_xml, xml_path, scss_text)
    if lint_warnings:
        print(f"🔎 Odoo-aware lint：{len(lint_warnings)} 個警告")
        for w in lint_warnings:
            print(f"   ⚠️  {w}")
    else:
        print("🔎 Odoo-aware lint：通過")

    clean_html = strip_qweb(raw_xml)

    # 3. 產出預覽 HTML
    title = xml_path.stem
    css_urls = load_odoo_css_urls()
    odoo_css_links = "\n".join(
        f'    <link rel="stylesheet" href="{u}">' for u in css_urls
    )
    preview_html = PREVIEW_TEMPLATE.format(
        title=title,
        odoo_css_links=odoo_css_links,
        page_css=page_css,
        content=clean_html,
    )

    output_path = PREVIEW_DIR / "index.html"
    output_path.write_text(preview_html, encoding="utf-8", newline="\n")
    print(f"📄 預覽檔已產出: {output_path}")
    return output_path


def compile_page_scss(scss_path: Path) -> str:
    """編譯單一 SCSS 檔為 CSS 字串，優先用 libsass，否則退回 sass CLI。"""
    try:
        import sass as libsass  # libsass
    except ImportError:
        libsass = None

    if libsass is not None:
        try:
            css = libsass.compile(filename=str(scss_path), output_style="compressed")
            print(f"🎨 頁面 SCSS 已以 libsass 編譯: {scss_path.name}")
            return css
        except libsass.CompileError as e:
            print(f"⚠️  libsass 編譯錯誤，改嘗試 sass CLI:\n{str(e)[:400]}")

    result = subprocess.run(
        f'npx sass --no-source-map --style=compressed "{scss_path}"',
        capture_output=True,
        text=True,
        shell=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode == 0 and result.stdout.strip():
        print(f"🎨 頁面 SCSS 已以 sass CLI 編譯: {scss_path.name}")
        return result.stdout

    err_msg = (result.stderr or "")[:500]
    if not err_msg:
        err_msg = "未安裝 libsass，且系統找不到 sass CLI。"
    print(f"⚠️  頁面 SCSS 編譯失敗:\n{err_msg}")
    return ""


def main() -> None:
    if len(sys.argv) < 2:
        print("用法: python scripts/build_preview.py <XML 檔案路徑> [額外 SCSS 檔案路徑]")
        print("範例: python scripts/build_preview.py outputs/2026-03-09_homepage.xml")
        print("若未指定 SCSS，自動抓同名 .scss（如 outputs/xxx.xml → outputs/xxx.scss）")
        sys.exit(1)

    xml_path = Path(sys.argv[1])
    if not xml_path.exists():
        print(f"❌ 找不到檔案: {xml_path}")
        sys.exit(1)

    # 取得 SCSS 檔：優先用第 2 個 argv，其次自動抓同名同目錄 .scss
    page_css = ""
    scss_path: Path | None = None
    if len(sys.argv) >= 3:
        scss_path = Path(sys.argv[2]).resolve()
    else:
        sibling = xml_path.with_suffix(".scss")
        if sibling.exists():
            scss_path = sibling.resolve()
            print(f"🔍 自動偵測到同名 SCSS: {sibling.name}")

    if scss_path and scss_path.exists():
        page_css = compile_page_scss(scss_path)

    output_path = build_preview(xml_path, page_css)

    # 自動開啟瀏覽器
    print("🌐 正在開啟瀏覽器...")
    webbrowser.open(output_path.as_uri())
    print("✅ 完成！")


if __name__ == "__main__":
    main()
