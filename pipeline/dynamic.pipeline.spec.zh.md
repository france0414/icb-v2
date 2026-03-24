# ICB /dynamic Pipeline Spec（中文版）

## 目標
使用鎖定的 base dynamic 模板插入動態區塊，避免修改內部結構。

## 步驟
1. **辨識意圖**
   - 確認指令為 `/dynamic`。
   - 判斷目標為 products 或 news/blog。

2. **載入 System 規則（Layer 1）**
   - 套用動態結構鎖定規則。

3. **最小檢索（Layer 2）**
   - 讀取 `templates_index.json`。
   - 選取 `base-dynamic-products` 或 `base-dynamic-news`。
   - 對應 HTML 僅用於 class 掃描。

4. **建立任務契約（Layer 3）**
   - 生成符合 `schema/page_task.schema.json` 的 task。
   - 帶入 `structure_locked` 與 allowed/forbidden ops。

5. **產出**
   - 產出 XML 到 `outputs/`。
   - 若只回傳單一區塊，可僅輸出 `<section>`（不含 QWeb 外框）。
   - 只在 section 層新增 class 或 `data-custom-name`。
   - 若有新樣式需求，輸出 SCSS。

6. **驗證**
   - 確保 inner DOM 未改動。
   - 確保 `data-template-key` 不被更改。
   - 執行：`python scripts/validate_dynamic_lock.py outputs/`
   - 若為 section-only 輸出，需加 `--no-qweb-check`。

7. **交付**
   - 回傳 XML/SCSS 路徑。

## 備註
- `/dynamic` 執行期間不產出 plan 檔。
- HTML 參考僅用於 class 命名，不應導入 DOM。
