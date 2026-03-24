# ICB /create Pipeline Spec（中文版）

## 目標
先產出文字骨架，經使用者確認後再生成 XML/SCSS。

## 步驟
1. **辨識意圖**
   - 確認指令為 `/create`。
   - 取得頁面類型、風格需求與動態區塊需求。

2. **載入 System 規則（Layer 1）**
   - 使用不可變規則（QWeb 外框、輸出路徑、動態鎖定、header/footer 限制）。

3. **最小檢索（Layer 2）**
   - 讀取 `templates_index.json` 作為參考。
   - 不可整段套用模板，只能參考結構寫法。

4. **Phase A：文字骨架**
   - 逐段輸出文字骨架。
   - 等待使用者確認。

5. **建立任務契約（Layer 3）**
   - 生成符合 `schema/page_task.schema.json` 的 task。
   - 帶入必要 lock 與輸出格式。

6. **產出**
   - 依確認後的骨架產出 XML/SCSS。

7. **驗證**
   - 動態鎖定區塊不可改結構。
   - Header 只能 SCSS；Footer 必須 XPath。

8. **交付**
   - 輸出到 `outputs/`，檔名含時間戳。

## 備註
- `/create` 只做文字骨架，不產出 plan 檔。
