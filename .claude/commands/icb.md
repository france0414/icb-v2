# icb (ICB Odoo 15)

ICB 的 Odoo 15 WebBuilder 知識入口與工作流程。

## When

- 生成頁面（XML + SCSS）、加入 Snippet、動態產品/部落格區塊、按鈕風格、互動 JS
- 釐清 Odoo 15 前端規範（容器、RWD、編輯器可編輯性、動態鎖定結構）

## Steps

1. 先讀 `AGENTS.md`（硬規則、輸出規則、可用指令）
2. 再讀 `TODO.md`（尚未完成的知識庫補充工作）
3. 讀 `docs/PROJECT_THEME.css`（配色）
4. 需要 Snippet/動態/按鈕/JS/版面/SCSS 查詢時，讀 ` .agent/skills/icb_page_generator/resources/` 對應文件
5. 產出檔案一律放 `outputs/`，檔名包含日期時間

## Hard Rules

- 所有頁面 XML 必須有 QWeb 外框（`<t t-name>` + `website.layout` + `#wrap`）
- 每個 `<section>` 內必須明確使用 `.container` 或 `.container-fluid`
- 不要在 XML 內寫 `<style>`；新樣式放 SCSS
- 動態產品/新聞有 locked 結構：只能套 class/設定 data-*，不可手刻卡片內部結構
