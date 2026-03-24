# ICB /page Pipeline Spec（中文版）

## 目標
以固定、低 token 的流程完成 `/page` 生成，將政策、檢索、任務契約、生成與驗證拆開。

## 步驟
1. **辨識意圖**
   - 確認指令為 `/page`。
   - 解析頁面類型與使用者指定的模板。

2. **載入 System 規則（Layer 1）**
   - 使用不可變規則（QWeb 外框、輸出路徑、動態鎖定、header/footer 限制）。

3. **最小檢索（Layer 2）**
   - 讀取 `templates_index.json`。
   - 只選取需要的模板（依名稱/分類/usage）。
   - 若包含動態區塊，優先使用 base dynamic 模板並套用 `structure_locked`。

4. **建立任務契約（Layer 3）**
   - 生成符合 `schema/page_task.schema.json` 的 task。
   - 帶入 index 的 `locks` 與 allowed/forbidden ops。
   - 明確列出預期輸出檔案（XML/SCSS）。

5. **產出**
   - 依契約生成 XML/SCSS。
   - 不擴張檢索範圍（維持最小集合）。

6. **驗證**
   - 檢查 `structure_locked` 是否未被破壞。
   - 若含 footer，必須為 XPath 輸出。
   - 若含 header，只能輸出 SCSS。

7. **交付**
   - 將 XML/SCSS 輸出到 `outputs/`，檔名含時間戳。

## 備註
- `/page` 執行期間不產出 plan 檔。
- 動態區塊的 HTML 參考僅用於 class 命名與 SCSS 設計。
