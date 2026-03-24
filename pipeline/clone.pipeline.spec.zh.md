# ICB /clone Pipeline Spec（中文版）

## 目標
將外部版型轉為 Odoo 相容草稿，僅輸出到 `outputs/`，不晉升模板。

## 步驟
1. **辨識意圖**
   - 確認指令為 `/clone`。
   - 取得目標 URL 與範圍。

2. **載入 System 規則（Layer 1）**
   - 套用抓站沙盒規則（只輸出到 outputs/）。
   - 保留 QWeb 外框與動態 Snippet 規則。

3. **最小檢索（Layer 2）**
   - 預設使用 Playwright MCP。
   - 未明確要求時不啟用付費抓取。

4. **結構優先轉譯**
   - 先用 Bootstrap row/col 還原布局。
   - 結構無法達成時再補 SCSS。

5. **建立任務契約（Layer 3）**
   - 生成符合 `schema/page_task.schema.json` 的 task。
   - 若含動態，套用 lock。

6. **產出**
   - 輸出 XML/SCSS 到 `outputs/`。

7. **驗證**
   - 禁止假卡片替代動態 Snippet。
   - 確保 QWeb 外框完整。

8. **交付**
   - 回傳輸出路徑。

## 備註
- 預設只產草稿，不晉升模板。
