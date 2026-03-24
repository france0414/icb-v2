---
name: js
description: 加入互動 JS 元件
---

# /js

加入互動 JavaScript 元件到頁面。

## 用法範例

```
/js carousel                → 輪播元件
/js accordion               → 手風琴元件
/js tabs                    → 分頁元件
/js counter                 → 數字計數器
```

## 執行步驟

### 1. 讀取元件庫

讀取 `.agent/skills/icb_page_generator/resources/component_library.md`

### 2. 選擇元件

常用 JS 元件：
| 名稱 | 說明 |
|------|------|
| carousel | 圖片/內容輪播 |
| accordion | 可收合手風琴 |
| tabs | 分頁切換 |
| counter | 數字動畫計數 |
| lightbox | 圖片燈箱 |
| scroll-reveal | 滾動顯示動畫 |

### 3. 輸出

產出：
1. **XML** — 元件結構（含必要 data 屬性）
2. **SCSS** — 元件樣式
3. **JS**（如需要）— 自訂互動邏輯

輸出到 `outputs/` 目錄。
