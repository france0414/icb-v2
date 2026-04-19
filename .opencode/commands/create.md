# create（🎨 創作模式 / 三階段）

創作全新頁面。三階段流程：Phase 0 內容解析 → Phase A 文字骨架 → Phase B 分段 XML+SCSS。輸入可為純文字或外部網址/截圖。

## Hard Rules
- ❌ 本專案禁止 git worktree；不得建立 `.worktrees/`。
- ❌ 未經 Bootstrap 4 Grid + Odoo QWeb 翻譯不得輸出原代碼。
- ❌ 動態區塊禁止自創 HTML 假卡片，必須對接 s_dynamic_snippet*。
- ❌ 標題字級禁止硬編 clamp/rem/px，一律用 var(--h1)~var(--h6)。

## Phase 0：內容解析（中介層）
1. 讀 `.agent/skills/icb_page_generator/SKILL.md`、`docs/design/PROJECT_THEME.css`、`docs/design/user_custom_rules.scss`
2. 解析輸入（純文字 / 抓站 HTML），抽出 business / keyAssets / mustHaves / excluded / visualDirection
3. 輸出 `outputs/<日期時間>_brief.json`
4. 🚦 **停下等使用者確認**

## Phase A：文字骨架
5. 從 brief 推導版面，每個區塊選擇必須引用 brief 欄位說明理由
6. 列出 section 類型、Bootstrap Grid 對應、間距（pt-*/pb-*）、Snippet 類型
7. 🚦 **停下等使用者確認**

## Phase B：分段生成 XML + SCSS
8. 拆 2–3 段，每段寫完 preview 確認再下一段；骨架先行、文案後填
9. 每個 section 明確 pt-*/pb-* 間距（8 倍數，含斷點變體）
10. 標題字級 var(--h1)~var(--h6)；既有 user_custom_rules.scss 的 class 優先套用
11. 重疊/絕對定位 SCSS 必加 `#wrapwrap:not(.odoo-editor-editable)` 守護
12. 可點卡片：父層 s_custom_clickableCard + 既有 <a> 加 s_custom_cardLink + ::before overlay
13. 沙盒原則：**強制**寫入 `outputs/`，嚴禁寫入 `templates/`
