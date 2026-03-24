---
description: 快速加入動態產品或動態消息區塊
---

# /dynamic

快速生成 Odoo 動態 Snippet（產品 / 部落格）的 XML 代碼。

## 1. 讀取規則
// turbo
**MUST**1. 讀取 `.agent/skills/icb_page_generator/resources/dynamic_rules.md`
2. 確認使用者要生成的是 **動態產品 (Products)** 還是 **動態消息/部落格 (Blogs)**。

### 👉 動態產品 (Products) 參數表
| 模板名稱 (Template) | Template Key (部分) |
|---|---|
| Borderless Card 1 | `...borderless_1` |
| Centered Product | `...centered` |
| Classic Card | `...add_to_cart` |
| Horizontal Card | `...horizontal_card` |

*可選附掛類別 (Custom Classes)*: `scaleL`, `scaleS`, `nameHoverUnderLine`, `imgNoMargin`, `arrowRight`, `titleHoverFull`

### 👉 動態消息/部落格 (Blogs) 參數表
| 模板名稱 (Template) | Template Key (部分) |
|---|---|
| Card Layout | `...blog_post_card` |
| Big Picture | `...blog_post_big_picture` |
| Horizontal | `...blog_post_horizontal` |
| List Layout | `...blog_post_list` |

*可選附掛類別 (Custom Classes)*: `cardRadius`, `borderHover`, `hoverUnderLine`, `titleLine`, `picTop`, `picBottom`, `dateTop`

3. 根據上面挑選的參數，依照嚴格的 XML 結構指引輸出代碼。

### 產品模板
| 模板 | Template Key | Class |
|------|-------------|-------|
| Borderless 1 | `website_sale.dynamic_filter_template_product_product_borderless_1` | `s_product_product_borderless_1` |
| Borderless 2 | `website_sale.dynamic_filter_template_product_product_borderless_2` | `s_product_product_borderless_2` |
| Centered | `website_sale.dynamic_filter_template_product_product_centered` | `s_product_product_centered` |
| Classic | `website_sale.dynamic_filter_template_product_product_add_to_cart` | `s_product_product_add_to_cart` |

### 部落格模板
| 模板 | Template Key | Class |
|------|-------------|-------|
| Card | `website_blog.dynamic_filter_template_blog_post_card` | `s_blog_post_card` |
| Big Picture | `website_blog.dynamic_filter_template_blog_post_big_picture` | `s_blog_post_big_picture` |

## 4. 選擇樣式 Class

常用自訂 class（可多選，空格分隔）：
- `s_custom_scaleL` — Hover 放大效果
- `s_custom_nameHoverUnderLine` — 標題 hover 底線
- `s_custom_cardRadius` — 圓角 20px
- `s_custom_hoverUnderLine` — Hover 底線
- `s_custom_noPic` — 隱藏圖片

## 5. 輸出 XML

依照規則文件中的嚴格結構產出 XML。
