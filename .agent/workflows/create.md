---
description: 創作全新 Odoo 版面（支援純文字描述或外部網址/截圖作為靈感），受嚴格 Odoo 結構管轄。
---

# /create

創作全新頁面結構。與 `/page`（套版模式）不同，此指令要求 AI **自行設計排版**。
使用者可以提供**純文字描述**，或者提供**外部網站網址/截圖**作為佈局參考。但無論輸入為何，產出都必須遵守 Odoo 的「承重牆規則」，將設計轉換為正確的 `Bootstrap Grid` 結構。

## Phase A：規劃骨架（先輸出，等待確認）

### 1. 讀取 Skill
// turbo
**MUST** 讀取 Skill 主檔：`.agent/skills/icb_page_generator/SKILL.md`

### 2. 讀取專案配色
// turbo
讀取 `docs/design/PROJECT_THEME.css`

### 3. 輸入解析與盤點 (Input Analysis)
判斷使用者的輸入類型：
- **若是純文字描述**：
  // turbo
  讀取 `.agent/skills/icb_page_generator/resources/custom_blocks.md` 了解 templates/ 有哪些積木屬性做為 Odoo 語法或屬性參考。
- **若是外部網址/截圖**：
  // turbo-all
  必須先使用 Browser MCP (如 Playwright, Google Chrome DevTools 等) 或 `curl` 抓取目標網址的 HTML（存入 `outputs/`）。
  👉 **鐵律：嚴禁直接複製抓取下來的 HTML 原碼。** 解析其視覺邏輯後，必須對應為 Bootstrap 4 Grid（`.container`, `.row`, `.col-lg-*`）與 Odoo 區塊結構。

### 4. 輸出文字骨架
產出每個 section 的規劃（類型、Bootstrap 佈局對應、設計概念、與 Odoo 原生框架的融合方式）。
**⛔ Phase A 嚴禁輸出任何 XML 或 SCSS 程式碼。這只是概念審查。**

## 🚦 Gate：等待使用者「確認 / 調整」

---

## Phase B：生成 XML + SCSS（確認後才執行）

### 5. 結構轉換與生成 (Structure Conversion)
- **QWeb 母節點**：最外圍被 `<t t-name="website.customized-[name]"><t t-call="website.layout"><div id="wrap" class="oe_structure oe_empty">` 包覆。
- **動態區塊轉接**：若含有「產品列表」或「部落格」，**嚴禁**寫死假資料卡片。必須對接原生 `s_dynamic_snippet` 鎖定結構。
- **絕對位置保護**：若區塊包含會互相疊加的絕對定位，外層 ID 必須加上 `#wrapwrap:not(.odoo-editor-editable)`。
- **還原轉義字元**：XML 提取出來的 SCSS，必須將 `&amp;` 還原為 `&`，`&gt;` 還原為 `>`。

### 6. Sandbox 輸出 (皮肉分離)
- ✅ 預設只產出當下專案草稿，**絕對不可**直接寫入 `templates/`。這只是實驗沙盒。
- ✅ **絕對不可**在 XML 中寫 `<style id="scss-code">`。
- 必須分別產出兩個檔案，放在 `outputs/` 目錄：
  - `outputs/draft-[name].xml`：只有純淨的 Odoo QWeb 結構。
  - `outputs/draft-[name].scss`：包含所有的變數、版塊佈局與動畫樣式。

## 禁止事項
- ❌ 未經確認就產出完整程式碼
- ❌ 直接複製外部網站的自訂 HTML 結構而不轉譯為 Bootstrap Grid
- ❌ 直接複製內部 templates/ 的完整結構充數
- ❌ 在 `/create` 階段就擅自將檔案寫入 `templates/`（違反晉升保守策略）
