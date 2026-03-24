# ICB /block Pipeline Spec（中文版）

## 目標
回傳單一區塊，預設只輸出 `<section>`。

## 步驟
1. **辨識意圖**
   - 確認指令為 `/block`。
   - 確定要使用的區塊或歷史客製參考。

2. **載入 System 規則（Layer 1）**
   - 套用核心規則（禁止內嵌 `<style>`、SCSS 需分離）。

3. **最小檢索（Layer 2）**
   - 只讀取對應區塊/資源。

4. **建立任務契約（Layer 3）**
   - 生成符合 `schema/page_task.schema.json` 的 task。

5. **產出**
   - 只輸出區塊 `<section>`（不含 QWeb 外框）。
   - 若需要樣式，另輸出 SCSS。

6. **驗證**
   - 執行：`python scripts/validate_dynamic_lock.py outputs/ --no-qweb-check`

7. **交付**
   - 回傳輸出路徑。

## 備註
- `/block` 預設為 section-only 輸出。
