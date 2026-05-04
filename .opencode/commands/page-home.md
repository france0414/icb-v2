# page-home（首頁套版模式）

專為首頁設計的快速生成指令。讀取 home_recipes.md 配方後直接組裝 XML + SCSS。

## Hard Rules

- 首頁 XML 必須在 `website.layout` 內加入 `<t t-set="pageName" t-value="'homepage'"/>`，切勿遺漏。
- 禁止 git worktree；禁止 stretched-link；禁止硬編 clamp/rem/px 覆蓋標題字級。
- home_recipes.md 為配方參考，不得直接複製，須替換內容與配色。

## Steps

0. **Preview 前置資訊收集（必做）**：若任務後續會牽涉 layout preview、正式 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，必須先主動要求使用者直接貼上**目前案件前台網址**，不可只做選項題而沒有文字輸入空間。建議提示文字：`請直接貼上目前網站前台網址（例如 https://example.com ）`。若使用者暫時沒有網址，需明確告知：可以先做灰階 / fallback 骨架，但正式 preview 前仍必須補網址。
1. 讀 Skill 主檔、`docs/design/PROJECT_THEME.css`、`docs/design/user_custom_rules.scss`
2. 讀 `resources/home_recipes.md`（指定版型 1–4 或自動選擇）
3. 依需求讀 `resources/snippet_rules.md`
4. 動態區塊依 `resources/dynamic_rules.md`，遵守 base-dynamic-*.xml locked 結構
5. 若使用者想先看版型而非直接產正式碼，可先提供 layout-only HTML 骨架確認
6. **可點卡片**：父層 s_custom_clickableCard + 既有 <a> 加 s_custom_cardLink，SCSS 用 `#wrapwrap:not(.odoo-editor-editable) .s_custom_cardLink::before { inset:0; position:absolute; }` overlay
7. **Footer 獨立輸出**：另產 `outputs/<時間>_footer.xml` + `.scss`，用 `<data inherit_id="website.layout"><xpath expr="//div[@id='footer']" position="replace">` 包覆，依專案客製欄位
8. 每個 section 明確使用 pt-*/pb-* 間距 utility（含斷點變體），8 的倍數
9. 標題字級一律 var(--h1)~var(--h6)，禁止硬編
10. 輸出 XML + SCSS 到 `outputs/`（檔名含日期時間）
