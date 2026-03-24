---
description: 抓取競品網站區塊並轉化為 Odoo 14 草稿 (Scraping & Cloning)
---

# /clone

使用此指令將外部參考網站的特定區塊「抓取」並「轉化」為符合 Odoo 14 規範的前端草稿。

## 1. 抓取分析 (Scrape & Analyze)
// turbo-all
**MUST** 先使用 `curl` 抓取目標網址的 HTML，存入 `outputs/[sitename].html`。
接著分析下載的 HTML，定位使用者指定的區塊（如：首頁的 Hero 區塊、帶 Tab 的 News 區塊、或者特製的卡片輪播）。

## 2. 結構轉化規則 (Structure Conversion - 鐵律)
1. **嚴禁直接複製：** 不能將抓下來的 HTML 原封不動輸出。必須將其改寫為 Bootstrap 4 的 Grid 系統 (`.container`, `.row`, `.col-lg-*`)。
2. **遵守 Odoo 母節點：** 輸出的 XML 最外圍必須被 `<t t-name="website.customized-[name]"><t t-call="website.layout"><div id="wrap" class="oe_structure oe_empty">` 包覆。
3. **動態區塊轉接：** 如果抓取的區塊是「部落格文章」或「產品列表」，**嚴禁**寫死假資料。必須使用 `AGENTS.md` 中規定的 `s_dynamic_snippet` 結構，並透過 SCSS 攔截改寫版面。
4. **絕對位置保護：** 會造成重疊的結構，最外圍的 ID 必須是 `#wrapwrap:not(.odoo-editor-editable)`。

## 3. 輸出規範 (Output Rules - 鐵律)
1. **沙盒原則：** 轉化出來的程式碼**絕對不可以**直接寫入 `templates/`。這只是實驗性的草稿（Sandbox）。
2. **晉升保守原則：** 預設**只產出當下專案草稿**，不得自動元件化、不得自動晉升公版；只有在使用者明確指示「請晉升為公版/元件化」時，才可規劃寫入 `templates/`。
3. **皮肉分離：** **絕對不可以**在 XML 中寫 `<style id="scss-code">`。
4. **還原轉義字元 (Unescape)：** 從 XML 提取 SCSS 獨立成檔案時，**絕對必須**檢查並將 HTML 跳脫字元還原（例如：將 `&amp;` 還原為 `&`，`&gt;` 還原為 `>` 等），確保 SCSS 語法正確不會編譯錯誤。
5. 必須分別產出兩個檔案，放在 `outputs/` 目錄：
   - `outputs/draft-[name].xml`：只有純淨的 Odoo QWeb 結構。
   - `outputs/draft-[name].scss`：包含所有的變數、版塊佈局與動畫樣式。

## 4. 交付與解說
產出後，使用 `notify_user` 通知使用者。解釋你分析了目標網站的哪些特徵，以及你如何在 Odoo 的限制下（例如使用哪些原生 Snipper class 搭配 SCSS）重現了這個視覺效果。
