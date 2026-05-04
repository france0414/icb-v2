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
4. 若使用者提供參考文字、圖片或文件，優先從 ./clientinfo/ 讀取；公版結構參考從 ./templates/ 讀取
5. 依需求讀取 resources/ 內的對應文件
6. 需要模板索引或快速定位模板時，讀 ./.agent/skills/icb_page_generator/resources/indexes/templates_index.json
7. 若使用者語意在 knowledge_map 找不到明確對應項，先讀 ./.agent/skills/icb_page_generator/resources/indexes/search_index.json（L2 關鍵字索引），依 triggers / keywords 比對後再 Read 命中的 file；命中 0 筆再主動詢問使用者

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
10. **自訂命名分兩層：** (1) section 層（snippet 等級）用 s_custom_PascalCase + data-custom-name="PascalCase"，僅限可編輯自訂區塊的 <section>，系統頁面/系統區塊不可改。(2) section 內的 div / p / li / 按鈕等內層元素不加 s_custom_ 前綴，直接用簡潔自訂 class 名即可（例：<div class="maskCard maskCard1">、<p class="strengthNum">、<ul class="contactList">），避免 s_custom_ 滿場飛。SCSS 選擇器用 `.s_custom_sectionName .innerClass { ... }` 作用域隔離。完整規範詳見 .agent/skills/icb_page_generator/resources/data_custom_name_spec.md
11. **自訂 RWD mixin：** 除 Bootstrap 4.5 內建 media-breakpoint-up/down(sm|md|lg|xl) 外，user_custom_rules.scss 已定義四個專案自訂 mixin 可直接 @include：mobile-xs（≤375px）、mobile-s（≤450px）、laptop-m（≤1365px）、laptop（≤1439px）。用法：`@include laptop { ... }`。優先用 Bootstrap mixin，需介於斷點之間或筆電/手機小尺寸細節時才用自訂 mixin。另有全域 container 覆寫 ($wrap-size: 1550px) 與 $container_small (1200px) 兩個 wrap / wrap-small mixin 可參考。
12. **Icon 規範：** 主要使用 Font Awesome v4（例如 `fa fa-star`）
13. **圖片：** 使用 https://picsum.photos/[width]/[height] 作為佔位圖
14. **樣式原則：** 新寫樣式一律放 SCSS，禁止在 XML 內寫 <style>；style="" 僅在 Odoo 系統元件本身必須或既有結構已依賴時可保留/最小使用
15. **樣式三層優先順序：** 先套用 docs/design/user_custom_rules.scss 等既有可重用 class，再使用 Bootstrap 4.5 原生 grid/utility（container/row/col、spacing、flex 等），最後才用 SCSS 補齊缺口；能用前兩層解決就不要新寫 SCSS。
16. **可編輯色彩規則：** 凡是 Odoo 後台 UI 本來可直接調整的色彩/濾鏡（例如 carousel 的 .o_we_bg_filter）必須保留為 XML 行內樣式，避免被搬到 SCSS 造成使用者無法在介面調整。
17. **主題色保留規則：** 當需要沿用 o_cc 類別的字體/按鈕配色但想換背景色時，請保留 o_cc (如 o_cc3) 並使用 XML 行內 style 覆寫背景色/漸層（如 text-block 範例），避免移到 SCSS 影響後台可調性。
18. **間距：** 使用 Bootstrap 4 的 pt/pb 規則，優先採用 8 的倍數
19. **AI 雙模式任務與 templates/ 定位：** `templates/` 是「靈感庫 + 積木庫」，不是「直接成品庫」。嚴禁直接複製 templates/ 任一檔案完整結構作為最終輸出。1.【套版模式 `/page`】允許從 `templates/` 和 `.agent/skills/icb_page_generator/resources/page_templates.md` 配方直接組裝，替換文案圖片即可。2.【創作模式 `/create`】不論使用者提供「純文字描述」或「外部範例圖文/網址」，皆為創作模式。AI 必須重新設計 section 順序與視覺重心，以設計靈感為首，但骨架必須嚴格遵守 Odoo 原則（Bootstrap Grid、QWeb 外框、動態鎖定區塊）。先出文字骨架確認後才生成 XML+SCSS。3.【元件晉升保守策略】創作或抓站轉化出來的新畫面，預設只產出「當下專案草稿 (位於 outputs/)」，不自動拆成公版元件、不寫入 templates/；僅在明確要求「晉升公版」時才寫入。
20. **創作模式前置分流：** 先判斷需求屬於「布局規劃」或「內頁設計 / 正式頁面設計」。布局規劃的重點是確認 section 順序、資訊層級與版面骨架，預設以灰階 / 中性色呈現；若客戶有偏好的版型語感或視覺節奏，應優先請其提供參考網址，並以網址作為布局與風格節奏判讀依據。內頁設計 / 正式頁面設計的重點是產出可落地的頁面視覺，必須遵守該案件在 Odoo 中的主題色配置；若有參考網址，僅作為版型與風格輔助，不可覆蓋案件主題色。
21. **templates/ Token 節省規則：** 不可直接讀取整份大型 XML 檔（如 content-sections.xml）。正確流程：先讀 `templates/README.md` 了解目錄結構，再查 `custom_blocks.md` 或 `page_templates.md` 取得 XML 檔名與行號範圍，最後用 view_range 精準讀取所需片段。`templates/base/` 為鎖定結構（禁止修改內部 DOM），`templates/improved/` 為元件積木庫。首頁配方改讀 `resources/home_recipes.md`，不再有 home-*.xml 範本檔。
22. **公版與客製 SCSS 提取原則：** 當 AI 判斷需要為特定組件（如特殊按鈕風格、動態區塊特有樣式）補上 SCSS 時，主來源絕對是 `templates/improved/` 目錄中，與該 XML/HTML 檔名完全相同的 `.scss` 檔案（例如：要抓 `templates/improved/banners/banner.xml` 的樣式，就去讀 `templates/improved/banners/banner.scss`）！AI 必須精準提取原生代碼，嚴禁自行發明或通靈 CSS
23. **輸出位置：** 產出檔案放在 outputs/，檔名必須包含日期與時間
24. **重用全域樣式：** 若 docs/design/user_custom_rules.scss 已有客製樣式（如 .s_custom_titleUnderLine, .s_custom_scaleL, 輪播箭頭位置等），AI 只需要套用 class，禁止重寫；若沒有對應樣式，則必須在輸出 SCSS 補上。詳見 .agent/skills/icb_page_generator/resources/scss_reference.md
25. **抓取轉化原則 (Scraping Sandbox)：** 當使用者在 `/create` 提供外部參考網址或截圖時，1. 嚴禁直接將草稿寫入 templates/，必須放在 outputs/。2. 嚴禁在 XML 內寫 <style id="scss-code">，必須產出獨立的 .scss 與 .xml。3. XML 最外圍必須遵守 <t t-name...><t t-call="website.layout"> 的 QWeb 標準層級。4. 動態區塊如新聞、產品必須對接 s_dynamic_snippet，嚴禁寫死前端假卡片結構。
26. **預覽資產規則：** 凡 `/create`、`/create-home`、`/page`、`/page-home` 需要做預覽時，不可寫死任何 Odoo asset CSS 路徑。若任務涉及 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，而使用者尚未提供案件前台網址，必須先主動詢問網址，再繼續後續生成或預覽。正確流程是：若已知案件網址，應先從該網址當前頁面重新抓取實際引用中的 CSS bundle（如 web.assets_common / web.assets_frontend 等）並更新預覽設定，再載入本次輸出的 XML/SCSS。每次生成 HTML 或重跑 preview 前，都必須重新檢查目前頁面實際引用的最新 CSS URL，不可沿用前一次抓到的 asset 路徑，因為 Odoo 每次存檔後 asset 代號可能改變。只有在明確沒有案件網址時，才允許使用 fallback CSS 作為近似預覽。
27. **1:1 strict 模式：** 若使用者明確要求 1:1 還原 AI 生成頁面，必須以『版型/間距/字級/按鈕/互動位置』最高相似度輸出，並保留 Odoo 可編輯性；若遇框架限制無法完全一致，需附差異摘要。
28. **AI 知識衝突防護：** 當 LLM 通用知識（Bootstrap 5、FA v5/v6、React/Vue 組件模式等）與本專案規格衝突時，優先順序為：本專案規格（AGENTS.md + SKILL.md）> 本專案知識庫（resources/）> 本專案模板（templates/）> Odoo 15 官方文件 > Bootstrap 4.5 官方文件 > LLM 通用訓練知識。遇衝突必須自我修正後才生成代碼，詳見 .agent/skills/icb_page_generator/resources/ai_conflict_prevention.md。
29. **Menu-01~04 SCSS 來源：** 統一在 templates/improved/headers/header-menus.scss，依 MENU-1~MENU-4 的 START/END 區塊擷取；當使用者要求 /page menu-0X 時，只輸出對應 SCSS 片段（含 START/END 註解）。
30. **/create 結構優先：** 無論是根據靈感還是外部網址還原版面，解析出 DOM/CSS 的呈現邏輯後，能用 Odoo/Bootstrap 既有結構（row/col/容器）還原左右/層次者，優先用結構取代 CSS，避免多寫 SCSS；只有結構無法達成時才補 SCSS。
31. **Snippet 三類型識別：** Snippet 分「排版型」(有 section + o_colored_level，可獨立)、「基本型」(有 section + o_colored_level，可獨立)、「內容型」(無 section，無 o_colored_level，必須放入父容器)。詳見 snippet_rules.md。
32. **o_colored_level 規則：** o_colored_level 是 Odoo 主題色階標記，讓使用者切換 o_cc1~o_cc5。主要 section、row、col、card 通常要加；純排版 div 或固定白底小元件不需加。詳見 snippet_rules.md。
33. **s_text 容器規則：** div.s_text (data-snippet='s_text') 是 Odoo 標準文字容器，在編輯器中可拖拉調整高度，內部可使用 Bootstrap row/col 做多欄排版。適合在已有 row/col 骨架內再增加靈活高度控制，或在 Accordion card-body 內實現圖文混排。詳見 snippet_rules.md。
34. **按鈕規範：** 按鈕一律用 <a> 不用 <button>。不自訂 class 名稱，只使用系統組合：btn + [btn-primary|btn-secondary|btn-fill-primary|btn-outline-*] + [btn-sm|btn-lg] + [rounded-circle|flat]。詳見 button_styles.md。
35. **字體大小統一：** user_custom_rules.scss 已定義 var(--h1)~var(--h6) 與對應 class（.h1 / .h2 ... / p.h1 / p.h2 ...）。使用規則：(1) 真正標題用 <h1>~<h6>（SEO 層級正確），字級自動綁定 var(--hX)。(2) 需要『大字但不想佔用 hX 語意』時（例：slogan、引文、卡片副標、數字強調）用 <p class="h2"> 或 <strong class="h3"> — p.hX / .hX 只改視覺大小不改 HTML 語意，對 SEO 友善。(3) 系統會清除 span，請避免依賴 <span> 作為可編輯文字容器。(4) 輸出 SCSS 嚴禁自己寫 font-size: clamp(...)、硬編 rem/px 覆蓋 h1~h6 或 .h1~.h6；若需特殊字級，用 var(--hX) 搭 font-weight/letter-spacing 調整。(5) 一頁只能有一個 <h1>，其他大字用 p.h1 / .h1。
36. **字體家族禁止覆蓋：** 專案主題已全站載入字體（font-family），SCSS 嚴禁再寫 font-family: ... 覆蓋（不論是 #wrapwrap、body、h1~h6、或自訂 class）。需要視覺層次只能調 font-weight (300/400/500)、letter-spacing、line-height、font-style；真的有特殊需求（例：某個品牌區用 monospace）必須在 brief.json 明確指定才允許，且只能加在最小範圍 class 上。
37. **媒體查詢一律用 Bootstrap mixin：** SCSS 的 RWD 斷點禁止硬寫 @media (max-width: 991.98px) / @media (min-width: 768px) 這類數字，必須使用 Bootstrap 4.5 提供的 mixin：media-breakpoint-down(sm|md|lg|xl)（對應 max-width: 575.98 / 767.98 / 991.98 / 1199.98）、media-breakpoint-up(sm|md|lg|xl)、media-breakpoint-between(md, lg)。寫法範例 `@include media-breakpoint-down(md) { ... }`。若專案自訂斷點（docs/design/user_custom_rules.scss //自訂RWD 斷點變數）才用對應 mixin。例外：只有 @media (hover: hover) / (prefers-reduced-motion) 這類非尺寸的 media feature 才允許直接寫 @media。
38. **區塊間距（外層 section pt/pb 預設配方、內層 col 預設 pt0 pb0）：** 詳見 .agent/skills/icb_page_generator/resources/spacing_rules.md。規則摘要：Hero→pt96 pb96、一般 section→pt80 pb80、次要→pt64 pb64、緊湊→pt48 pb48、Footer→pt96 pb48；col 不加 pt/pb；禁止 Bootstrap pt-4/pt-5 dash 寫法；偏離預設需 XML 註解寫理由。
39. **自訂結構可編輯性（七條紅線 + 可點卡片 overlay）：** 詳見 .agent/skills/icb_page_generator/resources/editability_rules.md。摘要：文字在真實 HTML 元素、圖片不 SCSS hard-code、::before/::after 只做裝飾、wrapper 最多兩層、overlay 加 #wrapwrap:not(.odoo-editor-editable) 守護、pointer-events 不擋內容、需拖拉高度用 s_text；可點卡片用 s_custom_clickableCard + s_custom_cardLink::before，禁止 stretched-link。
40. **/create 流程（Phase 0 brief.json → Phase A 文字骨架 → Phase B 頁面內容 XML+SCSS → Phase C Footer 獨立輸出，僅 /create-home）與 designMoves 規範：** 詳見 .agent/skills/icb_page_generator/resources/create_workflow.md。摘要：(1) Phase B 只處理 <div id='wrap'> 內 sections，可分段思考與逐段 preview，但最終必須合併輸出為單一 `full.xml` + `full.scss`，B1/B2/B3 只作中間產物。(2) Footer 是獨立 xpath 檔，不屬於 Phase B 任何一段。(3) 每階段停下等確認；brief.json 必含 3–5 個具名 designMoves、Phase A 至少採用 2 個。(4) /create-home 需 pageName='homepage' + Footer 獨立輸出；一般 /create 不輸出 Footer。(5) 抓站草稿放 outputs/、分離 xml/scss、對接動態 snippet。
41. **Layout-first 對稿模式：** 內頁 /create 可切換 Layout-first（只做結構骨架），圖片位置用灰色色塊占位、不放彩圖；若未指定則維持一般 /create 正常流程。
42. **產品/Blog 區塊策略：** 在 Layout-first 或使用者未要求 dynamic 時，預設用一般 section + row/col 的靜態結構（sheet 方式）；只有明確要求動態資料時才切 s_dynamic_snippet*。
43. **Hero 版型規則：** 背景主視覺內層必用 row/col 總和 12，可用 3:9、4:8、5:7、6:6 等比例；同一輪播需維持一致高度策略避免 CLS；小螢幕看不到的裝飾元素可直接隱藏，不強制保留。
44. **輪播效果來源規則：** 若需求涉及輪播/slider 視覺效果，優先對照 `templates/base/base-Static-Snippet.xml` 內既有對應結構後再生成，避免自創不相容輪播骨架。

## 依需求讀取的知識庫

核心知識資源位於 `./.agent/skills/icb_page_generator/resources/`

| 任務 | 讀取文件 |
|------|---------|
| 關鍵字 / triggers 查不到 knowledge_map 時，查 L2 索引 | `.agent/skills/icb_page_generator/resources/indexes/search_index.json` |
| 區塊間距規則（預設配方 + col pt0 + 例外情境） | `.agent/skills/icb_page_generator/resources/spacing_rules.md` |
| 自訂結構可編輯性七條紅線 + 可點卡片 overlay | `.agent/skills/icb_page_generator/resources/editability_rules.md` |
| /create 三階段流程、brief.json schema、designMoves、抓站規則 | `.agent/skills/icb_page_generator/resources/create_workflow.md` |
| /create 外部網址自動化驗證清單（抽樣頁面、動態區塊、QWeb 外框、RWD） | `.agent/skills/icb_page_generator/resources/create_external_validation_checklist.md` |
| design-director 代理分工契約（觸發條件/輸入輸出/fallback） | `.agent/skills/icb_page_generator/resources/design_director_contract.md` |
| design-director 驗證案例（2 觸發 + 2 不觸發） | `.agent/skills/icb_page_generator/resources/design_director_validation.md` |
| 選擇 Snippet / 了解嵌套規則 | `.agent/skills/icb_page_generator/resources/snippet_rules.md` |
| 生成動態產品 / 部落格區塊 | `.agent/skills/icb_page_generator/resources/dynamic_rules.md` |
| 套用按鈕風格 | `.agent/skills/icb_page_generator/resources/button_styles.md` |
| 加入互動 JS 元件 | `.agent/skills/icb_page_generator/resources/component_library.md` |
| 設計版面配置 | `.agent/skills/icb_page_generator/resources/layout_patterns.md` |
| 查詢 SCSS 變數 / Mixin / 斷點 | `.agent/skills/icb_page_generator/resources/scss_reference.md` |
| 呼叫歷史客製化區塊 | `.agent/skills/icb_page_generator/resources/custom_blocks.md` |
| 套用首頁樣板配方 (Home 1~4)，查詢各區塊 data-snippet / s_custom_* / data-* 屬性 | `.agent/skills/icb_page_generator/resources/home_recipes.md` |
| 了解首頁配方索引與使用方式 | `.agent/skills/icb_page_generator/resources/page_templates.md` |
| Header SCSS 覆寫 / Footer XML+SCSS 生成 | `.agent/skills/icb_page_generator/resources/header_footer_rules.md` |
| 聯絡表單佈局與 SCSS 覆寫 | `.agent/skills/icb_page_generator/resources/form_rules.md` |
| Blog / Shop 系統頁面 SCSS 覆寫 | `.agent/skills/icb_page_generator/resources/system_pages_scss.md` |
| 了解 Skill 開發流程、角色分工、自動化部署（CI/CD） | `.agent/skills/icb_page_generator/resources/skill_devops_process.md` |
| 模板索引與快速定位 | `.agent/skills/icb_page_generator/resources/indexes/templates_index.json` |
| data-custom-name 屬性規範（元素限制 / Token 格式 / 同步規則） | `.agent/skills/icb_page_generator/resources/data_custom_name_spec.md` |
| 防範 AI 知識衝突 / 各模型角色職責 / 自動 context 修正規則 | `.agent/skills/icb_page_generator/resources/ai_conflict_prevention.md` |
| 了解 data-custom-name 屬性規範與使用規則 | `.agent/skills/icb_page_generator/resources/data_custom_name_spec.md` |
| /create 模式生成歷史沿革（三種結構家族、RWD 規則、左右交錯邏輯） | `.agent/skills/icb_page_generator/resources/timeline_rules.md` |

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
| `/page-home` | 首頁套版模式（自動帶入 pageName 專屬結構，參考 home-recipes 1–4 配方） |
| `/create-home` | 首頁創作模式（三階段：Phase 0 brief JSON → Phase A 骨架 → Phase B 生成 XML+SCSS 並合併為單一 full 檔，首頁需 pageName + Footer 獨立輸出） |

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
├── home_recipes.md
├── header_footer_rules.md
├── form_rules.md
├── system_pages_scss.md
├── indexes/templates_index.json
├── skill_devops_process.md
├── design_director_contract.md
├── design_director_validation.md
├── timeline_rules.md
└── create_external_validation_checklist.md
```
