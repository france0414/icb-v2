# create

創作全新頁面。無論使用者輸入為**純文字描述**或**外部網址/截圖**，AI 均須解析輸入並設計排版，同時轉換為符合 Odoo「承重牆規則」的架構。與 /page（套版模式）不同，此指令要求 AI 放下原有版塊，自行創作。

## Steps

### Phase A：規劃骨架（先輸出，等待確認）
1. 讀取 Skill 主檔：`.agent/skills/icb_page_generator/SKILL.md`
2. 讀取專案配色：`docs/design/PROJECT_THEME.css`
3. 解析輸入類型：
   - **若是純文字**：讀取 `.agent/skills/icb_page_generator/resources/custom_blocks.md` 盤點可用積木（僅作語法參考）。
   - **若是外部網址/截圖**：嚴禁直接複製原碼。必須先抓取網頁，翻譯為 Bootstrap 4 Grid (`.container`, `.row`, `.col-*`)，整理設計概念。
4. 輸出文字骨架：每個 section 的類型、佈局對應、設計概念。
5. ⛔ Phase A 嚴禁輸出 XML 或 SCSS 程式碼。

### 🚦 Gate：等待使用者確認或調整

### Phase B：生成 XML + SCSS（確認後才執行）
6. 靜態區塊自由創作 XML；動態區塊必須對接原生 `s_dynamic_snippet`，嚴禁寫死前端假卡片結構。
7. 從 XML 提取對應的獨立 SCSS 樣式；若有重疊層級，務必加 `#wrapwrap:not(.odoo-editor-editable)` 前綴。
8. 沙盒原則：產出 **強迫** 寫入 `outputs/`（含日期檔名），除非明確要求，**嚴禁** 寫入 `templates/`。

## 禁止事項
- ❌ Phase A 輸出程式碼
- ❌ 未經 Bootstrap 與 Odoo QWeb 翻譯即輸出原代碼
- ❌ 動態區塊自創 HTML 面板
