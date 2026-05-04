# page (套版模式)

依照現有樣板配方或 Snippet 規則，快速生成頁面（XML + SCSS）。若需全新設計改用 `create`。

## Steps

0. **Preview 前置資訊收集（必做）**：若任務後續會牽涉 layout preview、正式 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，必須先主動要求使用者直接貼上**目前案件前台網址**，不可只做選項題而沒有文字輸入空間。建議提示文字：`請直接貼上目前網站前台網址（例如 https://example.com ）`。若使用者暫時沒有網址，需明確告知：可以先做灰階 / fallback 骨架，但正式 preview 前仍必須補網址。
1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. 讀 `docs/design/PROJECT_THEME.css`（配色，務必以此為準）
3. 讀 `resources/page_templates.md`，依下方決策樹選定配方
4. 依需求讀 `resources/snippet_rules.md`（Snippet 骨架細節）
5. 需要動態區塊時，讀 `resources/dynamic_rules.md`，並遵守 `templates/base/base-dynamic-*.xml` 的 locked 結構
6. 若使用者想先看版型而非直接產正式碼，可先提供 layout-only HTML 骨架確認
7. 輸出到 `outputs/`（XML + SCSS）

## 配方快速決策

先判斷使用者要做的頁面類型，直接套對應配方：

| 使用者說的 | 對應配方 | 核心 Snippet 組合 |
|-----------|---------|-----------------|
| 服務介紹、解決方案（單一） | **SP-01** | s_cover → s_text_block → s_features → s_call_to_action |
| 多項服務、左右交錯介紹 | **SP-02** | s_cover → s_text_image ↔ s_image_text（交替）→ s_call_to_action |
| 關於我們、公司介紹（完整）| **AB-01** | s_cover → s_text_block → s_numbers → s_three_columns → s_references → s_call_to_action |
| 關於我們（精簡版） | **AB-02** | s_title → s_text_image → s_features → s_numbers → s_call_to_action |
| 聯絡我們（含表單） | **CT-01** | s_title → row(聯絡資訊 + s_website_form) → s_map |
| 聯絡我們（多據點） | **CT-02** | s_cover → 據點列表 → s_map → s_website_form |
| 新聞列表、媒體報導 | **NL-01** | s_title → s_static_snippet(s_blog_post_card) → s_call_to_action |
| 產品列表、型錄 | **NL-02** | s_cover → s_static_snippet(s_product_product_borderless_1) → s_call_to_action |
| 首頁 | **home-1~4** | 讀 `resources/home_recipes.md` |

## 色彩節奏（此專案專用）

```
Hero → o_cc1(白) → o_cc2(淺灰) → o_cc1(白) → o_cc4(主色藍 CTA)
```

⚠️ 此專案 o_cc4 = 主色藍（CTA），o_cc3 = 次色金（區隔），與 Odoo 預設不同。

## 輸出規格

- XML：QWeb 外框（`<t t-name><t t-call="website.layout">`）
- SCSS：獨立 .scss 檔
- 檔名：`outputs/YYYYMMDD_HHMM_<頁面名>.xml` + `.scss`
