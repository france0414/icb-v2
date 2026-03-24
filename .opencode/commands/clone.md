# clone

抓取外部參考網站並轉成 Odoo 14 可用草稿（預設非公版、非元件化）。

## Free-First（預設）

1. 先用 `Playwright MCP`（或現有 chrome-devtools）抓渲染後頁面與互動狀態。
2. 只在使用者明確提供 `FIRECRAWL_API_KEY` 且要求批次抓整站時，才啟用 Firecrawl。
3. 未明確要求前，禁止自動晉升成 templates 公版元件。

## Steps

1. 抓取目標頁（hero、產品區、新聞區、CTA）並拆解為 section 語義。
2. 將外站結構改寫為 Odoo + Bootstrap 4.5（`.container` / `.row` / `.col-*`）。
3. 動態資料區（產品/新聞）必須改為 `s_dynamic_snippet` 系統結構。
4. 產出草稿到 `outputs/`：
   - `draft-[name]-[YYYYMMDD-HHMM].xml`
   - `draft-[name]-[YYYYMMDD-HHMM].scss`
5. 說明哪些區塊是 1:1 還原、哪些區塊因 Odoo 限制做了等價替換。

## 禁止事項

- ❌ 直接複製外站 HTML 原碼
- ❌ 在 XML 內寫 `<style>` 或 `style id="scss-code"`
- ❌ 未經明確要求自動寫入 `templates/` 或自動元件化
- ❌ 動態區塊寫死假卡片
