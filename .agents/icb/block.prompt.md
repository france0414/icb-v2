---
name: block
description: 呼叫歷史開發過的優良區塊與版面配置
---

# /block

呼叫已整理的客製化歷史區塊與公版結構庫，快速重用過去開發的版塊。

## 用法範例

```
/block                      → 列出所有可用區塊分類
/block zigzag               → 呼叫交錯磚塊
/block video-banner         → 呼叫影片 Banner
/block static-cards         → 呼叫靜態卡片 (basd-Static-Snippet.xml)
/block carousel             → 呼叫輪播版型 (Static-Snippet-carousel.xml)
/block tab-effect           → 呼叫出血頁籤切換 (customized-Static-Snippet.xml)
```

## 執行步驟

### 1. 讀取客製化區塊庫

讀取 `.agent/skills/icb_page_generator/resources/custom_blocks.md`
（文件尾部含 **Templates 公版結構庫** 完整檔案對照表）

### 2. 查找公版結構 (templates/)

若使用者需求與某個公版結構接近，到 `templates/` 讀取對應 XML 骨架：
- **靜態版型** → `basd-Static-Snippet.xml`, `customized-Static-Snippet.xml`
- **靜態輪播** → `Static-Snippet-carousel.xml`, `customized-static-carousel.xml`
- **動態產品** → `dynamic-products.xml`, `customized-dynamic-products.xml`, `customized-dynamic-products-js.xml`
- **動態新聞** → `dynamic-news.xml`, `customized-dynamic-news.xml`

### 3. 無參數時列出清單

顯示所有可用的客製化區塊名稱與簡述，包含 custom_blocks.md 中的區塊 + templates/ 公版。

### 4. 帶參數時輸出區塊

根據名稱找到對應區塊，輸出：
1. **XML** — 區塊結構（圖片路徑替換為 `https://picsum.photos/[w]/[h]`）
2. **SCSS** — 區塊樣式

### 5. 輸出位置

輸出到 `outputs/` 目錄，檔名含日期時間。
