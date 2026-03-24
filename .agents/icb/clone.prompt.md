---
name: clone
description: 抓取競品頁面並轉為 Odoo 草稿（預設不晉升公版元件）
---

# /clone

將外部參考網站拆解為可維護的 Odoo 14 結構草稿。

## 執行策略（Free-First）

1. 預設優先使用 `Playwright MCP`（或等價瀏覽器抓取工具）做渲染後分析。
2. 只有使用者明確提供 `FIRECRAWL_API_KEY` 且要求批次抓取時，才使用 Firecrawl。
3. 預設只輸出專案草稿，禁止自動元件化與公版晉升。

## 輸出規範

- XML 必須使用 Odoo QWeb 母節點外框。
- 樣式只放 SCSS。
- 動態資料區改用 `s_dynamic_snippet`。
- 輸出到 `outputs/`，檔名包含日期時間。

## 嚴禁

- 直接複製外站完整 HTML 結構。
- 未經明確授權寫入 `templates/`。
- 在 XML 內嵌 `<style>`。
