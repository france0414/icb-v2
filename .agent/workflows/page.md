---
description: 生成 Odoo 14 頁面（靜態 / 動態 / 整頁樣板）
---

# /page（🏷️ 套版模式）

依照現有樣板配方或 Snippet 規則，快速生成頁面（XML + SCSS）。
若需要全新設計，請改用 `/create`（創作模式）。

本專案**不使用** git worktree，請直接在專案根目錄工作。

## 1. 讀取 Skill
// turbo
**MUST** 讀取 Skill 主檔：`.agent/skills/icb_page_generator/SKILL.md`

## 2. 讀取專案配色
// turbo
讀取 `docs/PROJECT_THEME.css`，了解 `--primary`、`o_cc1`~`o_cc5` 等色彩變數。

## 3. 分析需求

判斷使用者要求的頁面類型：
- **完整首頁/Landing Page 樣板** → **MUST** 讀取 `resources/page_templates.md`，並依照裡面的「配方 (Recipe)」順序組裝多個 Snippet。
- **單一靜態頁面/區塊**（About / Landing）→ 參考 `resources/snippet_catalog.md` 選擇標準 Snippet。
- **動態列表**（最新產品 / 新聞）→ 讀取 `resources/dynamic_rules.md`。
- **靜態導航**（產品分類卡片）→ 使用 `s_three_columns` 等靜態 Snippet，**禁止**用動態 Snippet。

## 4. 選擇 Snippet 組合與特殊區塊

- 若使用樣板配方，請參照配方列出的 `data-snippet` 順序進行結構堆疊。
- 若配方中含有客製化區塊（如交錯磚塊、影片 Banner 等），或是使用者明確要求，請務必讀取 `resources/custom_blocks.md` 獲取結構。
- 遵守嵌套規則：`#wrap > section[data-snippet] > .container > .row > .col > content`

## 5. 按鈕風格檢查

需要特殊按鈕？→ 讀取 `resources/button_styles.md`
不需要？→ 使用 `btn-primary` / `btn-outline-secondary`

## 6. 輸出

產出兩個區塊：
1. **XML** — QWeb 模板（圖片使用 `https://picsum.photos/`）
2. **SCSS** — 自訂樣式（針對複雜的版塊或配方所需的客製化撰寫 SCSS）
