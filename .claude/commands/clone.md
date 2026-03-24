# clone (外站翻譯草稿)

把外部網站區塊翻譯成 Odoo 14 相容的草稿（預設不晉升公版元件）。

## Steps

1. 先以結構還原為主（容器/row/col），能用結構就不要多寫 SCSS
2. 動態內容（產品/新聞）必須對接 `s_dynamic_snippet*`，不可手刻假卡片
3. 抓站結果只落在 `outputs/`，不要寫入 `templates/`
4. SCSS 盡量從 `templates/` 同名 `.scss` 精準提取（不要通靈發明）
