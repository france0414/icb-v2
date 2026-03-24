---
description: 以 templates/ 為靈感庫，創作全新 ICB 頁面（禁止直接複製任何 template 結構）
---

# /create

以 ICB 元件為靈感，**重新設計**全新頁面結構。與 `/page`（套版模式）不同，此指令要求 AI 自行創作排版。

## Phase A：規劃骨架（先輸出，等待確認）

### 1. 讀取 Skill
// turbo
**MUST** 讀取 Skill 主檔：`.agent/skills/icb_page_generator/SKILL.md`

### 2. 讀取專案配色
// turbo
讀取 `docs/PROJECT_THEME.css`

### 3. 詢問 / 確認需求
若使用者未明確說明，需先確認：產業類型、視覺風格、重點訴求、是否需要動態區塊。

### 4. 盤點可用積木
// turbo
讀取 `resources/custom_blocks.md` 了解 templates/ 有哪些積木類型（**僅作語法參考，不作直接來源**）。

### 5. 輸出文字骨架
產出每個 section 的規劃（類型、設計概念、參考積木、與既有差異）。
**⛔ Phase A 嚴禁輸出任何 XML 或 SCSS 程式碼。**

## 🚦 Gate：等待使用者「確認 / 調整」

## Phase B：生成 XML + SCSS（確認後才執行）

### 6. 生成程式碼
- 靜態區塊：自由創作 XML
- 輪播 Banner：外框用系統輪播結構，slide 內容自由
- 動態產品/消息：使用 `s_dynamic_snippet`，只寫 SCSS
- SCSS：只包含實際使用的樣式，禁止整包複製

### 7. 輸出
XML + SCSS 輸出到 `outputs/`，檔名含日期時間。

## 禁止事項
- ❌ 直接複製 templates/ 完整結構
- ❌ 照搬 page_templates.md 配方順序
- ❌ Phase A 輸出程式碼
- ❌ 動態區塊自創 HTML
