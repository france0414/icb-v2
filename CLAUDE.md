# Worktree Policy

請不要在此專案使用 git worktree。

- 直接在專案根目錄工作，不要建立 `.worktrees/` 或其他 worktree 目錄
- 若工具詢問 worktree 位置，請選擇「不使用 worktree / 直接在主專案」
- 目的：避免多人環境混淆與多餘的分支/目錄管理成本








<!-- ICB_SKILL_INSTRUCTIONS_START -->
## Odoo AI Development Rules (Auto-synced)

1. 此專案的 Odoo skill 採用統一知識來源：AGENTS.md + TODO.md + .agent/skills/icb_page_generator/resources/。
2. 如需 Odoo 頁面、Snippet、按鈕、動態區塊、互動元件規則，先對照 .agent/skills/icb_page_generator/SKILL.md。
3. 規劃呈現：除 /create Phase A 文字骨架外，禁止輸出 plan.md 或任何規劃檔；規劃僅在對話中簡短說明，使用者確認後直接執行。
4. 請先讀以下兩份文件，了解專案規則與待辦工作：
5. 1. AGENTS.md（全域規則：XML 結構、輸出規則、可用指令）
6. 2. TODO.md（目前尚未完成的知識庫補充工作）
7. 接著讀 docs/design/PROJECT_THEME.css 了解專案配色。
8. 若使用者提供參考文字、圖片、PPT、Excel 或其他素材，優先從 clientInfo/ 讀取；公版結構參考從 templates/ 讀取。
9. 所有 Odoo 相關快捷指令定義在 .claude/commands/ 目錄中：
10. - page.md → 套版模式快速生成頁面
11. - create.md → 創作模式（先文字骨架，確認後才生成 HTML/XML+SCSS。支援純文字或外部網址輸入）
12. - dynamic.md → 加入動態區塊
13. - btn.md → 套用按鈕風格
14. - js.md → 加入互動 JS 元件
15. - block.md → 呼叫已整理的客製化歷史區塊
16. /page 為套版模式，允許依配方快速組裝；/create 為創作全新頁面，必須先輸出文字骨架並等待使用者確認，再生成 XML+SCSS。
17. 深度知識庫（SCSS參考、按鈕風格等）位於 .agent/skills/icb_page_generator/resources/ 目錄中。
18. 模板索引用於快速定位模板：.agent/skills/icb_page_generator/resources/indexes/templates_index.json。
19. AI 新生成的 XML、SCSS 與其他交付檔，統一輸出到 outputs/，檔名需包含日期時間。
20. 抓站轉化（/create 外部網址）：嚴禁將轉化的草稿直接放入 templates/，且必須分離 XML/SCSS，必定遵守 QWeb 外框與動態 Snippet 規則，產出在 outputs/ 沙盒中。
21. /create 抓站規則：請優先呼叫本地的 Fetch 或 Browser MCP (如 Playwright, Google Chrome DevTools MCP) 抓回 HTML。目前暫時不啟用 Firecrawl。
22. 本專案禁止使用 git worktree；不得建立 .worktrees/ 或任何 worktree 目錄。
23. 抽出 SCSS：從 XML 提取 SCSS 獨立成檔案時，絕對必須將 HTML 跳脫字元（如 &amp;, &gt;）還原（如 &, >），避免 SCSS 編譯錯誤。
24. 若需求屬於 Header、Footer、Blog、Shop 或其他 Odoo 系統自動生成頁面，預設只能輸出 SCSS，不可直接輸出 XML。

<!-- ICB_SKILL_INSTRUCTIONS_END -->
