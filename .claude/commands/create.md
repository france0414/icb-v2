# create (創作模式)

設計新版面。輸入可以是「純文字描述」或「外部參考網址」。

## Steps

1. 讀 `.agent/skills/icb_page_generator/SKILL.md`
2. 先產出文字骨架 (Phase A)：解析排版結構，並說明如何用 Bootstrap Grid (`.container`, `.row`, `.col-*`) 與 Odoo 原生骨架重現。
3. 使用者確認後才生成 XML + SCSS (Phase B)。
4. 動態內容（產品/新聞）必須對接 `s_dynamic_snippet*`，不可手刻假卡片。
5. 嚴禁覆蓋既有 `templates/`，產出存放於 `outputs/`。
