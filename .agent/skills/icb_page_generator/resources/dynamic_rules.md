# Odoo Dynamic Snippet Rules (STRICT)

> [!IMPORTANT]
> This file is the **SINGLE SOURCE OF TRUTH** for generating Dynamic Products and Dynamic Blogs/News.
> **DO NOT** invent new structures. You **MUST** use the exact XML patterns below.

## 1. Design Consistency Rules

> [!CAUTION]
> **一個網站使用一種版型！** 選擇後全站統一，除非明確說明某區塊需要不同設計。

### Default Templates (預設版型)
| Content Type | Default Template | Class |
|--------------|------------------|-------|
| **Products** | Borderless Card 1 | `s_product_product_borderless_1` |
| **Blogs/News** | Card Layout | `s_blog_post_card` |

### When to Use Different Templates
- 使用者明確要求不同風格時
- 提供的圖片比例不適合預設版型時（例如橫幅圖適合 `horizontal`）
- 特定區塊設計需求與全站不同時（需使用者說明）

### Consistency Principle
```
選擇 s_product_product_borderless_1 作為產品版型
    → 全站所有產品區塊都使用 borderless_1 的 SCSS
    → 只有使用者明確說「這個區塊要不同」時才客製
```

## 2. Global Precautions
> [!WARNING]
> **White Background Issue**: Odoo's default `.card` and `.card-body` have a white background (`#FFFFFF`).
> - This often obscures custom colored backgrounds.
> - **Fix**: If the design requires a transparent or colored background, you **MUST** override this in SCSS or use a custom class associated with background removal.

## 3. Nesting & Placement (CRITICAL)
> [!TIP]
> **Safe Nesting**: While Dynamic Snippets are typically top-level `<section>` elements, they **CAN** be placed inside specific layout snippets if multi-column design is needed.
>
> **Allowed Parent Containers:**
> - `s_text_block` (with `.row` > `.col`)
> - `s_column_layout` (or legacy `s_three_columns`)
>
> **FORBIDDEN:**
> - **DO NOT** create custom `<div>` wrappers or random HTML grids to hold these snippets.
> - **DO NOT** wrap them in purely structural divs without a parent Snippet definition (like `s_text_block`).
> - **DO NOT MODIFY INNER HTML**: The content inside `<section>` MUST be exactly as defined in the templates. **NO adding titles, divs, or text inside the snippet section.**
> - Always rely on Odoo's standard layout structures to ensure drag-and-drop safety.

> [!WARNING]
> **嚴禁擅自修改提供的 HTML 結構 (Life or Death)**：
> 1. **不要刪減結構**：Odoo 的動態渲染引擎強烈依賴某些隱藏的 div 或 class。如果 AI 覺得某些 div "沒有用" 而把它刪掉，會導致整個板塊渲染失敗！
> 2. **不要亂加結構**：如果 AI 為了排版方便，擅自把 `<section>` 切斷，或在 `.dynamic_snippet_template` 外部包上一層新的 `<div>`，會讓 Odoo 的 Backend 編輯器完全壞掉，使用者之後無法拖拉修改該區塊。
> 3. **AI 只能**：在現有指定的 `<section>` 標籤上 **新增你需要的 `class="[你的自訂類別]"`**，剩下的排版魔法請全部**寫在 SCSS 裡面**。

---

## 4. Dynamic Products (E-Commerce)

### A. Strict XML Structure
**Snippet:** `s_dynamic_snippet_products` OR `s_dynamic_snippet_carousel`
**Filter ID:** `3` (Standard for Products) or `all` (if category specific).

```xml
<section 
    data-snippet="s_dynamic_snippet_products" 
    class="s_dynamic_snippet_products s_dynamic o_colored_level [TEMPLATE_CLASS] [CUSTOM_CLASSES]" 
    data-name="Products" 
    data-filter-id="3" 
    data-template-key="[TEMPLATE_KEY]" 
    data-product-category-id="all" 
    data-number-of-elements="4" 
    data-number-of-elements-small-devices="1" 
    data-number-of-records="16" 
    data-carousel-interval="5000" 
    data-custom-name="[CUSTOM_NAMES]">
    
    <div class="o_not_editable container">
        <div class="css_non_editable_mode_hidden">
            <div class="missing_option_warning alert alert-info rounded-0 fade show d-none d-print-none o_default_snippet_text"></div>
        </div>
        <div class="dynamic_snippet_template"></div>
    </div>
</section>
```
> [!IMPORTANT]
> **XML vs HTML 渲染差異 (極度重要)**：
> 上方的 XML 程式碼 **不包含** 實際的產品卡片 (如 `.card`, `.o_carousel_product_card_body`)！
> 在 Odoo 的邏輯中，XML 裡的 `<div class="dynamic_snippet_template"></div>` 只是一個佔位符。
> 網站載入後，系統後端與 JS 才會非同步撈取資料，並即席生成出滿滿的 `.row > .col > .card` DOM 結構塞入這個 div 裡面。
> **AI 行為守則設定**：
> - 當你(AI) 在寫 XML 排版時，你**絕對不能**手寫 `.card` 塞在裡面。
> - 當你(AI) 被要求寫這塊的 SCSS 樣式時，你需要知道最終網頁上 **會出現** `.card`、`.o_carousel_product_card_img_top` 等元素（可參考本文第 7 節），並以此編寫 SCSS！

*For Carousel version, change `data-snippet` to `s_dynamic_snippet_carousel` and class to `s_dynamic_snippet_carousel`.*

### B. Valid Template Keys (Products)
| Style Name | Template Key | Class Name |
| :--- | :--- | :--- |
| **Borderless Card 1** | `website_sale.dynamic_filter_template_product_product_borderless_1` | `s_product_product_borderless_1` |
| **Borderless Card 2** | `website_sale.dynamic_filter_template_product_product_borderless_2` | `s_product_product_borderless_2` |
| **Centered Product** | `website_sale.dynamic_filter_template_product_product_centered` | `s_product_product_centered` |
| **Classic Card** | `website_sale.dynamic_filter_template_product_product_add_to_cart` | `s_product_product_add_to_cart` |
| **Detailed Product** | `website_sale.dynamic_filter_template_product_product_view_detail` | `s_product_product_view_detail` |
| **Horizontal Card** | `website_sale.dynamic_filter_template_product_product_horizontal_card` | `s_product_product_horizontal_card` |
| **Large Banner** | `website_sale.dynamic_filter_template_product_product_banner` | `s_product_product_banner` |
| **Image Only** | `website_sale.dynamic_filter_template_product_product_mini_image` | `s_product_product_mini_image` |
| **Image w/ Name** | `website_sale.dynamic_filter_template_product_product_mini_name` | `s_product_product_mini_name` |

### C. valid Custom Classes (Products)
*Must be added to `class` AND `data-custom-name`*
- `scaleL` / `scaleS` (Hover zoom)
- `nameHoverUnderLine` (Title underline on hover)
- `imgNoMargin` (Remove image spacing)
- `arrowRight` (Arrow indicator)
- `titleHoverFull`

---

## 5. Dynamic Blogs / Latest News

### A. Strict XML Structure
**Snippet:** `s_dynamic_snippet` OR `s_dynamic_snippet_carousel`
**Filter ID:** `1` (Strictly required for Blogs)

```xml
<section 
    data-snippet="s_dynamic_snippet" 
    class="s_dynamic_snippet s_dynamic o_colored_level [TEMPLATE_CLASS] [CUSTOM_CLASSES]" 
    data-name="Dynamic Snippet" 
    data-filter-id="1" 
    data-template-key="[TEMPLATE_KEY]" 
    data-number-of-elements="4" 
    data-number-of-elements-small-devices="1" 
    data-number-of-records="4" 
    data-custom-name="[CUSTOM_NAMES]">
    
    <div class="o_not_editable container">
        <div class="css_non_editable_mode_hidden">
            <div class="missing_option_warning alert alert-info rounded-0 fade show d-none d-print-none o_default_snippet_text"></div>
        </div>
        <div class="dynamic_snippet_template"></div>
    </div>
</section>
```
> [!IMPORTANT]
> 與動態產品相同，這裡的 `<div class="dynamic_snippet_template"></div>` 在渲染後會被替換為完整的 Bootstrap Grid 結構（包含 \`.s_blog_posts_post\`, \`.card\`）。撰寫 SCSS 時請參考最終渲染 DOM 的層級。

### B. Valid Template Keys (Blogs)
| Style Name | Template Key | Class Name |
| :--- | :--- | :--- |
| **Big Picture** | `website_blog.dynamic_filter_template_blog_post_big_picture` | `s_blog_post_big_picture` |
| **Card Layout** | `website_blog.dynamic_filter_template_blog_post_card` | `s_blog_post_card` |
| **Horizontal** | `website_blog.dynamic_filter_template_blog_post_horizontal` | `s_blog_post_horizontal` |
| **List Layout** | `website_blog.dynamic_filter_template_blog_post_list` | `s_blog_post_list` |

### C. Valid Custom Classes (Blogs)
| Class Name | Description | Compatible Layouts |
| :--- | :--- | :--- |
| `cardRadius` | 20px Border Radius | All |
| `cardRadiusS` | 10px Border Radius | All |
| `borderHover` | Border color change on hover. | Card |
| `hoverUnderLine` | Title hover underline | All |
| `titleLine` | Static title underline | All |
| `blockLine` | Separator lines | List |
| `picTop` | Picture on Top | Horizontal |
| `picBottom` | Picture on Bottom | Horizontal, Card |
| `dateTop` | Date above text | Card |

---

## 6. Helper Table: Which Snippet Do I Use?

| Content Type | Display Mode | Snippet Name (`data-snippet`) |
| :--- | :--- | :--- |
| **Products** | Grid / List | `s_dynamic_snippet_products` |
| **Products** | Carousel / Slider | `s_dynamic_snippet_carousel` |
| **News / Blogs** | Grid / List | `s_dynamic_snippet` |
| **News / Blogs** | Carousel / Slider | `s_dynamic_snippet_carousel` |

---

## 7. Styling Reference (Target Selectors)

為了確保樣式一致性，AI 生成 SCSS 時必須針對以下官方結構編寫選擇器。

### A. Product (Borderless 1) - `s_product_product_borderless_1`

主要目標是 `.o_carousel_product_card`。

```scss
// 適用於 Grid & Carousel
.s_product_product_borderless_1 {
    .o_carousel_product_card {
        // 卡片容器 (預設有 p-3 padding)
    }
    .o_carousel_product_card_img_top {
        // 產品圖片
    }
    .card-title {
        // 產品標題 (.h6)
    }
    .o_carousel_product_card_alias {
        // 產品摘要/別名
    }
}
```

### B. Blog (Card Layout) - `s_blog_post_card`

主要目標是 `.s_blog_posts_post .card`。

```scss
// 適用於 Grid & Carousel
.s_blog_post_card {
    .s_blog_posts_post {
        .card {
            // 卡片容器
        }
        .s_blog_posts_post_cover {
            // 封面圖容器 (內含 background-image div)
            .o_record_cover_image {
                // 實際圖片 div
            }
        }
        .card-body {
            h4 {
                // 文章標題 (預設是 h4)
            }
            .s_blog_posts_post_teaser {
                // 文章摘要
            }
        }
        .card-footer {
            // 底部資訊 (日期、分類)
        }
    }
}
```
