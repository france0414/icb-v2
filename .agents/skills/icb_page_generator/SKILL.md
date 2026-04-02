---
name: icb_page_generator
description: Odoo 15 網頁開發的統一知識入口。當使用者要求生成頁面、加入 Snippet、動態產品或部落格區塊、按鈕風格、互動 JS 元件，或詢問 Odoo 15 前端規範時，使用此 skill。
license: MIT
compatibility: opencode
metadata:
  audience: maintainers, developers
  workflow: odoo-web-building
---

# Odoo Page Generator

此檔由 scripts/sync_icb_skill.py 自動產生，請優先修改 sources/skill/icb_skill.source.json。

> [!NOTE]
> `.agent/skills/icb_page_generator/SKILL.md`、`.agents/skills/icb_page_generator/SKILL.md` 與 OpenCode instructions 應維持語意一致。
> 核心知識來源固定為 `./.agent/skills/icb_page_generator/resources/` 與 `./AGENTS.md`。

## 統一讀取順序

1. 先讀 ./AGENTS.md
2. 再讀 ./TODO.md，確認目前尚未完成的知識庫工作
3. 讀 ./docs/design/PROJECT_THEME.css 了解專案配色
4. 若使用者提供參考文字、圖片或文件，優先從 ./clientInfo/ 讀取；公版結構參考從 ./templates/ 讀取
5. 依需求讀取 resources/ 內的對應文件
6. 需要模板索引或快速定位模板時，讀 ./.agent/skills/icb_page_generator/resources/indexes/templates_index.json

## 核心規則

1. **XML 結構：** 所有頁面都必須由 <t t-name="..."><t t-call="website.layout">...</t></t> 包覆
2. **首頁：** 首頁需加 <t t-set="pageName" t-value="'homepage'"/>
3. **佈局容器：** 每個 <section> 內的核心框架必須明確選擇使用 .container (限制寬度置中) 或 .container-fluid (滿版)，不可遺漏或隨意自創網格外殼
4. **規劃呈現：** 除 /create Phase A 文字骨架外，禁止輸出 plan.md 或任何規劃檔；規劃僅在對話中簡短說明，使用者確認後直接執行
5. **重疊與絕對定位保護：** 所有會導致元素重疊的 SCSS (如負邊距 mt-n5、絕對定位 position:absolute 覆蓋圖文) 必須加上 `#wrapwrap:not(.odoo-editor-editable)` 前綴，確保在 Odoo 編輯模式下元素會解開重疊，讓使用者能正常點擊並替換文字與圖片
6. **斷點規範：** 符合 Bootstrap 4.5 的斷點，請使用 Bootstrap 4.5 的斷點寫法（含 media-breakpoint-up/down mixin）。若需額外斷點，請使用 docs/design/user_custom_rules.scss 的自訂 RWD 斷點變數與 mixin（//--自訂RWD 斷點變數 開始--// 區塊）
7. **Snippet：** 必須有 data-snippet 和 data-name 屬性
8. **Snippet 來源：** 乾淨 snippets 來源必須是 Odoo 15 官方原始 XML。
9. **Snippet 例外標註：** 若有例外（非 Odoo 15 官方原始 XML），產出檔案的檔頭必須標註：exception: <reason> | source: <url/path>
10. **自訂命名：** s_custom_PascalCase 必須搭配 data-custom-name="PascalCase"，僅用於可編輯的自訂區塊（section/snippet）；系統頁面/系統區塊不可改
11. **Icon 規範：** 主要使用 Font Awesome v4（例如 `fa fa-star`）
12. **圖片：** 使用 https://picsum.photos/[width]/[height] 作為佔位圖
13. **樣式原則：** 新寫樣式一律放 SCSS，禁止在 XML 內寫 <style>；style="" 僅在 Odoo 系統元件本身必須或既有結構已依賴時可保留/最小使用
14. **可編輯色彩規則：** 凡是 Odoo 後台 UI 本來可直接調整的色彩/濾鏡（例如 carousel 的 .o_we_bg_filter）必須保留為 XML 行內樣式，避免被搬到 SCSS 造成使用者無法在介面調整。
15. **主題色保留規則：** 當需要沿用 o_cc 類別的字體/按鈕配色但想換背景色時，請保留 o_cc (如 o_cc3) 並使用 XML 行內 style 覆寫背景色/漸層（如 text-block 範例），避免移到 SCSS 影響後台可調性。
16. **間距：** 使用 Bootstrap 4 的 pt/pb 規則，優先採用 8 的倍數
17. **AI 雙模式任務與 templates/ 定位：** `templates/` 是「靈感庫 + 積木庫」，不是「直接成品庫」。嚴禁直接複製 templates/ 任一檔案完整結構作為最終輸出。1.【套版模式 `/page`】允許從 `templates/` 和 `.agent/skills/icb_page_generator/resources/page_templates.md` 配方直接組裝，替換文案圖片即可。2.【創作模式 `/create`】不論使用者提供「純文字描述」或「外部範例圖文/網址」，皆為創作模式。AI 必須重新設計 section 順序與視覺重心，以設計靈感為首，但骨架必須嚴格遵守 Odoo 原則（Bootstrap Grid、QWeb 外框、動態鎖定區塊）。先出文字骨架確認後才生成 XML+SCSS。3.【元件晉升保守策略】創作或抓站轉化出來的新畫面，預設只產出「當下專案草稿 (位於 outputs/)」，不自動拆成公版元件、不寫入 templates/；僅在明確要求「晉升公版」時才寫入。
18. **templates/ Token 節省規則：** 不可直接讀取整份大型 XML 檔（如 content-sections.xml、home-*.xml）。正確流程：先讀 `templates/README.md` 了解目錄結構，再查 `custom_blocks.md` 或 `page_templates.md` 取得 XML 檔名與行號範圍，最後用 view_range 精準讀取所需片段。`templates/base/` 為鎖定結構（禁止修改內部 DOM），`templates/improved/` 為元件積木庫。
19. **公版與客製 SCSS 提取原則：** 當 AI 判斷需要為特定組件（如特殊按鈕風格、動態區塊特有樣式）補上 SCSS 時，主來源絕對是 `templates/improved/` 目錄中，與該 XML/HTML 檔名完全相同的 `.scss` 檔案（例如：要抓 `templates/improved/banners/banner.xml` 的樣式，就去讀 `templates/improved/banners/banner.scss`）！AI 必須精準提取原生代碼，嚴禁自行發明或通靈 CSS
20. **輸出位置：** 產出檔案放在 outputs/，檔名必須包含日期與時間
21. **重用全域樣式：** 若 docs/design/user_custom_rules.scss 已有客製樣式（如 .s_custom_titleUnderLine, .s_custom_scaleL, 輪播箭頭位置等），AI 只需要套用 class，禁止重寫；若沒有對應樣式，則必須在輸出 SCSS 補上。詳見 .agent/skills/icb_page_generator/resources/scss_reference.md
22. **抓取轉化原則 (Scraping Sandbox)：** 當使用者在 `/create` 提供外部參考網址或截圖時，1. 嚴禁直接將草稿寫入 templates/，必須放在 outputs/。2. 嚴禁在 XML 內寫 <style id="scss-code">，必須產出獨立的 .scss 與 .xml。3. XML 最外圍必須遵守 <t t-name...><t t-call="website.layout"> 的 QWeb 標準層級。4. 動態區塊如新聞、產品必須對接 s_dynamic_snippet，嚴禁寫死前端假卡片結構。
23. **Menu-01~04 SCSS 來源：** 統一在 templates/improved/headers/header-menus.scss，依 MENU-1~MENU-4 的 START/END 區塊擷取；當使用者要求 /page menu-0X 時，只輸出對應 SCSS 片段（含 START/END 註解）。
24. **/create 結構優先：** 無論是根據靈感還是外部網址還原版面，解析出 DOM/CSS 的呈現邏輯後，能用 Odoo/Bootstrap 既有結構（row/col/容器）還原左右/層次者，優先用結構取代 CSS，避免多寫 SCSS；只有結構無法達成時才補 SCSS。

## 依需求讀取的知識庫

核心知識資源位於 `./.agent/skills/icb_page_generator/resources/`

| 任務 | 讀取文件 |
|------|---------|
| 選擇 Snippet / 了解嵌套規則 | `.agent/skills/icb_page_generator/resources/snippet_rules.md` |
| 生成動態產品 / 部落格區塊 | `.agent/skills/icb_page_generator/resources/dynamic_rules.md` |
| 套用按鈕風格 | `.agent/skills/icb_page_generator/resources/button_styles.md` |
| 加入互動 JS 元件 | `.agent/skills/icb_page_generator/resources/component_library.md` |
| 設計版面配置 | `.agent/skills/icb_page_generator/resources/layout_patterns.md` |
| 查詢 SCSS 變數 / Mixin / 斷點 | `.agent/skills/icb_page_generator/resources/scss_reference.md` |
| 呼叫歷史客製化區塊 | `.agent/skills/icb_page_generator/resources/custom_blocks.md` |
| 套用首頁樣板配方 (Home 1~4) | `.agent/skills/icb_page_generator/resources/page_templates.md` |
| Header SCSS 覆寫 / Footer XML+SCSS 生成 | `.agent/skills/icb_page_generator/resources/header_footer_rules.md` |
| 聯絡表單佈局與 SCSS 覆寫 | `.agent/skills/icb_page_generator/resources/form_rules.md` |
| Blog / Shop 系統頁面 SCSS 覆寫 | `.agent/skills/icb_page_generator/resources/system_pages_scss.md` |
| 模板索引與快速定位 | `.agent/skills/icb_page_generator/resources/indexes/templates_index.json` |

## 尚未補齊但必須遵守的規則

以下知識文件仍在 `TODO.md` 的待完成項目內；在文件建立前，直接遵守這些限制：

1. **Header：** 禁止輸出 XML，只能輸出 SCSS 覆寫（基於第一組 Header 選項）
2. **Footer：** 必須輸出完整 XPath XML（基於 Links 選項）+ 配套 SCSS
3. **Blog / Shop / 系統頁面：** 禁止輸出 XML，只能輸出 SCSS 覆寫
4. **表單類區塊：** 佈局外殼 (Layout) + 原生表單投放 (Dropzone) 分離策略；若設計師提供既有 HTML，優先保留結構，只補 SCSS 與必要 class

## 可用指令

| 指令 | 說明 |
|------|------|
| `/page` | 生成完整頁面（套版模式） |
| `/create` | 創作全新頁面（無論輸入是網址/截圖或文字，皆先骨架分析後生成） |
| `/dynamic` | 快速加入動態產品或部落格區塊 |
| `/btn` | 套用或建立按鈕風格 |
| `/js` | 加入互動 JS 元件 |
| `/block` | 呼叫已整理的客製化歷史區塊 |

## 輸出原則

1. 頁面型任務通常輸出 XML + SCSS
2. 系統頁面型任務通常輸出 SCSS only
3. 若需求屬於 Odoo 系統自動生成頁面，先確認是否只能覆寫樣式，不能直接改 HTML/XML

## Resources 目錄

```
./.agent/skills/icb_page_generator/resources/
├── snippet_rules.md
├── dynamic_rules.md
├── button_styles.md
├── component_library.md
├── layout_patterns.md
├── custom_blocks.md
├── scss_reference.md
├── page_templates.md
├── header_footer_rules.md
├── form_rules.md
├── system_pages_scss.md
└── indexes/templates_index.json
```
