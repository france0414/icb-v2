# create（🎨 創作模式 / 三階段）

創作全新頁面。三階段流程：Phase 0 內容解析 → Phase A 文字骨架 → Phase B 分段 XML+SCSS。輸入可為純文字或外部網址/截圖。

## Hard Rules
- ❌ 本專案禁止 git worktree；不得建立 `.worktrees/`。
- ❌ 未經 Bootstrap 4 Grid + Odoo QWeb 翻譯不得輸出原代碼。
- ❌ 標題字級禁止硬編 clamp/rem/px，一律用 var(--h1)~var(--h6)。

## Phase 0：內容解析（中介層）
0. **Preview 前置資訊收集（必做）**：若任務後續會牽涉 layout preview、正式 preview、樣式對齊、1:1 還原或外部設計轉 Odoo，必須先主動要求使用者直接貼上**目前案件前台網址**，不可只做選項題而沒有文字輸入空間。建議提示文字：`請直接貼上目前網站前台網址（例如 https://example.com ）`。若使用者暫時沒有網址，需明確告知：可以先做灰階 / fallback 骨架，但正式 preview 前仍必須補網址。
1. **Terse prompt 偵測（experimental）**：輸入少於 20 字或僅抽象形容詞時，若環境支援 subagent 則呼叫 `design-director` 先反問 3 題；若環境不支援 subagent，則由主流程直接反問同一組 3 題後再產 brief。
2. 讀 `.agent/skills/icb_page_generator/SKILL.md`、`docs/design/PROJECT_THEME.css`、`docs/design/user_custom_rules.scss`
3. 解析輸入（純文字 / 抓站 HTML），抽出 business / keyAssets / mustHaves / excluded / visualDirection
4. 輸出 `outputs/<日期時間>_brief.json`
5. 🚦 **停下等使用者確認**

## Phase A：文字骨架
6. 若使用者明確指定 Layout-first，先做灰色色塊占位對稿版；未指定則維持一般骨架流程
7. 若使用者表示骨架想直接看版型，應優先提供 layout-only HTML
8. 從 brief 推導版面，每個區塊選擇必須引用 brief 欄位說明理由
9. 列出 section 類型、Bootstrap Grid 對應、間距（pt-*/pb-*）、Snippet 類型
10. 🚦 **停下等使用者確認**

## Phase B：分段生成 XML + SCSS
9. 拆 2–3 段，每段寫完 preview 確認再下一段；骨架先行、文案後填
10. 每個 section 明確 pt-*/pb-* 間距（8 倍數，含斷點變體）
11. 標題字級 var(--h1)~var(--h6)；既有 user_custom_rules.scss 的 class 優先套用
12. 重疊/絕對定位 SCSS 必加 `#wrapwrap:not(.odoo-editor-editable)` 守護
13. 可點卡片：父層 s_custom_clickableCard + 既有 <a> 加 s_custom_cardLink + ::before overlay
14. 產品/Blog 區塊預設可先用靜態 sheet + row/col；僅在明確要求動態資料時才對接 `s_dynamic_snippet*`
15. 沙盒原則：**強制**寫入 `outputs/`，嚴禁寫入 `templates/`
