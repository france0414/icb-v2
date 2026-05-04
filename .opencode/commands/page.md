# page（🏷️ 套版模式）

依照現有樣板配方或 Snippet 規則，快速生成頁面（XML + SCSS）。若需全新設計改用 /create。

## Hard Rules

- 執行 `/page` 時，禁止使用 Superpowers skills 或其他外部技能流程；只允許使用本專案 ICB 規則與資源。
- 本專案禁止使用 git worktree；不得建立 `.worktrees/` 或任何 worktree 目錄。

## Steps

0. **Preview 前置資訊收集（必做）**：若任務後續會牽涉 layout preview、正式 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，必須先主動要求使用者直接貼上**目前案件前台網址**，不可只做選項題而沒有文字輸入空間。建議提示文字：`請直接貼上目前網站前台網址（例如 https://example.com ）`。若使用者暫時沒有網址，需明確告知：可以先做灰階 / fallback 骨架，但正式 preview 前仍必須補網址。
1. 讀取 Skill 主檔：`.agent/skills/icb_page_generator/SKILL.md`
2. 讀取專案配色：`docs/design/PROJECT_THEME.css`
3. 判斷頁面類型：完整首頁樣板(配方) / 靜態頁面 / 動態列表 / 靜態導航
4. 若為完整樣板，讀取 `resources/page_templates.md` 依照配方組裝。若含客製區塊讀取 `resources/custom_blocks.md`。
5. 若為一般頁面，從 `resources/snippet_rules.md` 選擇 Snippet 組合。
6. 檢查是否需要特殊按鈕風格（→ `resources/button_styles.md`）
7. 若使用者想先看版型而非直接產正式碼，可先提供 layout-only HTML 骨架確認
8. 輸出 XML + SCSS（圖片使用 `https://picsum.photos/`）
