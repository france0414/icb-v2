---
name: page
description: 生成 Odoo 14 頁面（靜態 / 動態 / 整頁樣板）
---

# /page（🏷️ 套版模式）

依照現有樣板配方或 Snippet 規則，快速生成頁面（XML + SCSS）。
若需要全新設計，請改用 `/create`（創作模式）。

## 用法範例

```
/page 關於我們              → 生成 About 頁面
/page 首頁                  → 生成完整 Landing Page
/page 產品列表              → 生成動態產品頁
```

## 執行步驟

### 1. 讀取 Skill
讀取 `.agents/skills/icb_page_generator/SKILL.md`

### 2. 讀取專案配色
讀取 `docs/PROJECT_THEME.css`

### 3. 分析需求

判斷頁面類型：
- **完整首頁/Landing Page** → 讀取 `resources/page_templates.md`
- **單一靜態頁面** → 參考 `resources/snippet_catalog.md`
- **動態列表** → 讀取 `resources/dynamic_rules.md`
- **靜態導航** → 使用靜態 Snippet，禁止動態

### 4. 選擇 Snippet 組合

- 遵守嵌套規則：`#wrap > section[data-snippet] > .container > .row > .col > content`
- 客製化區塊讀取 `resources/custom_blocks.md`

### 5. 按鈕風格檢查

需要特殊按鈕？→ 讀取 `resources/button_styles.md`

### 6. 輸出

產出兩個區塊：
1. **XML** — QWeb 模板（圖片用 `https://picsum.photos/`）
2. **SCSS** — 自訂樣式

輸出到 `outputs/` 目錄，檔名含日期時間。
