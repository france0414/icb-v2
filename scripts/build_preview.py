"""
Odoo Local Preview Builder
==========================
用法: python scripts/build_preview.py [XML 檔案路徑]
範例: python scripts/build_preview.py outputs/2026-03-09_homepage.xml

此腳本會：
1. 讀取指定的 Odoo XML 檔案
2. 去掉 QWeb 語法（<t t-call>, <t t-set> 等），只保留 HTML 結構
3. 編譯 docs/user_custom_rules.scss → preview/custom.css
4. 產出 preview/index.html，引入：
   - 測試機的完整 Odoo CSS (遠端)
   - 局部自訂 CSS (本地編譯)
5. 自動開啟瀏覽器預覽
"""

import re
import subprocess
import sys
import webbrowser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PREVIEW_DIR = REPO_ROOT / "preview"
SCSS_SOURCE = PREVIEW_DIR / "_preview_entry.scss"  # Bootstrap mixin shim + @import user_custom_rules
CUSTOM_CSS_OUTPUT = PREVIEW_DIR / "custom.css"

# 測試機的完整 Odoo CSS（包含 Bootstrap 4 + 所有原生樣式）
ODOO_CSS_URL = "https://demo-design.gtmc.app/web/assets/4486-0aa6846/1/web.assets_frontend.min.css"

PREVIEW_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Odoo Preview — {title}</title>

    <!-- 1. Odoo 測試機完整 CSS (Bootstrap 4 + 原生樣式) -->
    <link rel="stylesheet" href="{odoo_css_url}">

    <!-- 2. FontAwesome 4 (Odoo 14 使用的版本) -->
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
        f'sass --no-source-map --style=compressed "{SCSS_SOURCE}" "{CUSTOM_CSS_OUTPUT}"',
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


def build_preview(xml_path: Path, page_css: str = "") -> Path:
    """從 XML 檔案建立預覽 HTML"""
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 編譯 SCSS
    compile_scss()

    # 2. 讀取 XML 並清理
    raw_xml = xml_path.read_text(encoding="utf-8")
    clean_html = strip_qweb(raw_xml)

    # 3. 產出預覽 HTML
    title = xml_path.stem
    preview_html = PREVIEW_TEMPLATE.format(
        title=title,
        odoo_css_url=ODOO_CSS_URL,
        page_css=page_css,
        content=clean_html,
    )

    output_path = PREVIEW_DIR / "index.html"
    output_path.write_text(preview_html, encoding="utf-8", newline="\n")
    print(f"📄 預覽檔已產出: {output_path}")
    return output_path


def main() -> None:
    if len(sys.argv) < 2:
        print("用法: python scripts/build_preview.py <XML 檔案路徑> [額外 SCSS 檔案路徑]")
        print("範例: python scripts/build_preview.py outputs/2026-03-09_homepage.xml")
        sys.exit(1)

    xml_path = Path(sys.argv[1])
    if not xml_path.exists():
        print(f"❌ 找不到檔案: {xml_path}")
        sys.exit(1)

    # 如果有提供額外的 SCSS 檔案（頁面專屬樣式），讀入作為 <style> 嵌入
    page_css = ""
    if len(sys.argv) >= 3:
        scss_path = Path(sys.argv[2]).resolve()
        if scss_path.exists():
            # 建立臨時 wrapper，先載入 Bootstrap mixin shim 再 import 頁面 SCSS
            shim_path = PREVIEW_DIR / "_bs4_shim.scss"
            wrapper_path = PREVIEW_DIR / "_page_temp.scss"
            
            # 寫入 shim（如果尚不存在）
            if not shim_path.exists():
                shim_content = (PREVIEW_DIR / "_preview_entry.scss").read_text(encoding="utf-8")
                # 只取 shim 的 mixin 定義部分（去掉最後的 @import）
                shim_only = shim_content.split("// Import the actual")[0]
                shim_path.write_text(shim_only, encoding="utf-8")
            
            # 建立 wrapper：先載入 shim，再載入頁面 SCSS
            scss_posix = scss_path.as_posix()
            wrapper_path.write_text(
                f'@import "bs4_shim";\n@import "{scss_posix}";\n',
                encoding="utf-8"
            )
            
            result = subprocess.run(
                f'sass --no-source-map --style=compressed "{wrapper_path}"',
                capture_output=True,
                text=True,
                shell=True,
                encoding="utf-8",
                errors="replace",
            )
            if result.returncode == 0:
                page_css = result.stdout
                print(f"🎨 頁面專屬樣式已編譯: {scss_path.name}")
            else:
                err_msg = (result.stderr or "")[:300]
                print(f"⚠️  頁面 SCSS 編譯失敗:\n{err_msg}")

    output_path = build_preview(xml_path, page_css)

    # 自動開啟瀏覽器
    print("🌐 正在開啟瀏覽器...")
    webbrowser.open(output_path.as_uri())
    print("✅ 完成！")


if __name__ == "__main__":
    main()
