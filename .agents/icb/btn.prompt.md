---
name: btn
description: 套用按鈕風格到網站
---

# /btn

套用或創建按鈕風格。支援「選單」、「名字/數字」、「關鍵字」、「網址仿製」四種使用方式。

## 用法範例

```
/btn                        → 顯示選單，引導選擇
/btn flash                  → 直接輸出「閃光」風格
/btn 5                      → 直接輸出第 5 套
/btn 我要箭頭效果            → 關鍵字配對推薦
/btn flash 顏色改成 #FF5500  → 指定風格 + 自訂顏色
```

## 6 套按鈕風格庫

| # | 名稱 | 中文 | 效果 |
|---|------|------|------|
| 1 | `skew` | 斜切 | 右下角缺角遮罩 |
| 2 | `arrow` | 普通箭頭 | FA 箭頭 + 彈跳 |
| 3 | `thin-arrow` | 細箭頭 | CSS 折線箭頭 |
| 4 | `dot` | 圓點放大 | 圓點膨脹填滿 |
| 5 | `flash` | 閃光 | 光影掃過 |
| 6 | `skew-fill` | 傾斜填滿 | 背景斜向展開 |

## 執行步驟

1. **判斷輸入類型**
   - 無參數 → 顯示選單
   - 名字/數字 → 直接輸出對應風格
   - 關鍵字 → 配對推薦
   - 網址 → 分析仿製

2. **確認顏色偏好**（預設使用 o_cc 變數，可改固定色）

3. **讀取按鈕樣式** → `.agent/skills/icb_page_generator/resources/button_styles.md`

4. **取得完整 SCSS** → 從 `templates/btn-style.xml` 中對應風格的 `<pre id="scss-code">` 複製完整版 SCSS（含 o_cc1~o_cc5 色彩變數）

5. **輸出完整 SCSS**（含開頭結尾標記 `// 按鈕區 開始` ~ `// 按鈕區 結束`）
   - ⚠️ SCSS 為**全域套用**，直接作用於 `#wrapwrap .btn` 等選擇器，**不需要** `s_custom_btn0x` 包裹 class
   - `btn-style.xml` 中的 `s_custom_btn0x` class 僅用於預覽頁面的樣式隔離

6. 若是新風格，詢問是否命名並存入庫

