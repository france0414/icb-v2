# create-home（🎨 首頁創作模式 / 三階段）

設計全新首頁。結合 /create 三階段 + /page-home 首頁專屬規範。

## Hard Rules
- 首頁 XML 必須在 `website.layout` 內加入 `<t t-set="pageName" t-value="'homepage'"/>`，切勿遺漏。
- Footer 必須**獨立輸出**（Odoo footer 為獨立 xpath 繼承區）。
- 禁止 git worktree；禁止硬編字級；禁止 stretched-link / 手刻假卡片。

## Steps

### Phase 0：內容解析
0. **Preview 前置資訊收集（必做）**：若任務後續會牽涉 layout preview、正式 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，必須先主動要求使用者直接貼上**目前案件前台網址**，不可只做選項題而沒有文字輸入空間。建議提示文字：`請直接貼上目前網站前台網址（例如 https://example.com ）`。若使用者暫時沒有網址，需明確告知：可以先做灰階 / fallback 骨架，但正式 preview 前仍必須補網址。
1. **Terse prompt 偵測（experimental）**：輸入少於 20 字或僅抽象形容詞時，若環境支援 subagent 則呼叫 `design-director` 先反問 3 題；若環境不支援 subagent，則由主流程直接反問同一組 3 題後再產 brief。
2. 讀 Skill 主檔、`docs/design/PROJECT_THEME.css`、`docs/design/user_custom_rules.scss`
3. `home_recipes.md` 僅作靈感參考，非強制套用
4. 輸出 `outputs/<日期時間>_brief.json`，停下等確認

### Phase A：文字骨架
5. 從 brief 推導版面；首頁建議順序可用 Hero → 服務亮點 → 產品/案例 → 解決方案/產業應用 → 關於我們 → Blog
6. 若使用者表示骨架想直接看版型，應優先提供 layout-only HTML
7. 每個區塊說明 Bootstrap Grid 對應、間距、Snippet 類型；停下等確認

### Phase B：分段生成頁面內容（只處理 `<div id='wrap'>` 內 sections，不含 Footer）
   - section ≤ 4：一次到位
   - section 5–7：拆 B1 上半頁 / B2 下半頁
   - section ≥ 8：拆 B1 / B2 / B3（每段 2–3 個 section）
6. `<t t-call="website.layout">` 內加 `<t t-set="pageName" t-value="'homepage'"/>`
7. 外層 section 用 pt/pb 預設配方（pt96/pt80/pt64/pt48），內層 col 預設 pt0 pb0；詳見 resources/spacing_rules.md
8. 標題字級 var(--h1)~var(--h6)，禁止硬編 clamp/rem；禁止 font-family 覆蓋；媒體查詢用 Bootstrap mixin
9. 可點卡片：父層 s_custom_clickableCard + 既有 <a> 加 s_custom_cardLink，SCSS 用 #wrapwrap:not(.odoo-editor-editable) ::before overlay
10. 產品/Blog 區塊若未明確要求動態資料，預設用靜態 sheet + row/col
11. 每段 preview 確認再下一段

### Phase C：Footer 獨立輸出（首頁專屬，不屬於 Phase B 任一段）
12. 另產 `outputs/<時間>_footer.xml` + `.scss`
13. 用 `<data inherit_id="website.layout" name="..." active="False"><xpath expr="//div[@id='footer']" position="replace">` 包覆
14. 依專案內容客製欄位（不照抄公版選單）

### 預覽
15. `PYTHONIOENCODING=utf-8 python scripts/build_preview.py outputs/<產出檔>.xml`
