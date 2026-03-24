---
name: dynamic
description: 快速加入動態產品或部落格區塊
---

# /dynamic

快速加入動態產品（Dynamic Products）或動態部落格（Dynamic Blog）區塊。

## 用法範例

```
/dynamic products           → 動態產品區塊
/dynamic blog               → 動態部落格區塊
/dynamic 最新消息            → 關鍵字配對
```

## 執行步驟

### 1. 讀取動態規則

讀取 `.agent/skills/icb_page_generator/resources/dynamic_rules.md`

### 2. 判斷類型

| 關鍵字 | 類型 |
|--------|------|
| products, 產品, 商品 | Dynamic Products |
| blog, 部落格, 新聞, 消息 | Dynamic Blog |

### 3. 輸出

產出包含正確 `data-snippet` 和動態屬性的 XML 區塊。

動態區塊必備屬性：
- `data-snippet="s_dynamic_snippet_products"` 或 `s_dynamic_snippet_blog`
- `data-filter-by-*` 屬性
- `data-number-of-records`

輸出到 `outputs/` 目錄。
