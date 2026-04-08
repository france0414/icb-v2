# Odoo Dynamic Snippet Rules (STRICT)

> [!IMPORTANT]
> 動態區塊只允許使用 Odoo 的既有 XML 骨架與 TEMPLATE_KEY。
> **禁止手刻 inner DOM**，只能在 `<section>` 上加 class / data-custom-name。

---

## 1) Snippet 類型與用途

| Content Type | Display | `data-snippet` | Filter ID |
|---|---|---|---|
| Products | Grid / List | `s_dynamic_snippet_products` | `3` |
| Products | Carousel | `s_dynamic_snippet_carousel` | `3` |
| Blogs / News | Grid / List | `s_dynamic_snippet` | `1` |
| Blogs / News | Carousel | `s_dynamic_snippet_carousel` | `1` |

---

## 2) XML 結構（不可改內部）

> 只允許在 `<section>` 上新增 class 與 data-custom-name。
> **禁止新增/刪除 inner DOM**，也不要把卡片結構手寫進去。

### Products
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

### Blogs / News
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

---

## 3) TEMPLATE_KEY 對照表

### Products
| Style | TEMPLATE_KEY | TEMPLATE_CLASS |
|---|---|---|
| Borderless Card 1 | `website_sale.dynamic_filter_template_product_product_borderless_1` | `s_product_product_borderless_1` |
| Borderless Card 2 | `website_sale.dynamic_filter_template_product_product_borderless_2` | `s_product_product_borderless_2` |
| Centered Product | `website_sale.dynamic_filter_template_product_product_centered` | `s_product_product_centered` |
| Classic Card | `website_sale.dynamic_filter_template_product_product_add_to_cart` | `s_product_product_add_to_cart` |
| Detailed Product | `website_sale.dynamic_filter_template_product_product_view_detail` | `s_product_product_view_detail` |
| Horizontal Card | `website_sale.dynamic_filter_template_product_product_horizontal_card` | `s_product_product_horizontal_card` |
| Large Banner | `website_sale.dynamic_filter_template_product_product_banner` | `s_product_product_banner` |
| Image Only | `website_sale.dynamic_filter_template_product_product_mini_image` | `s_product_product_mini_image` |
| Image w/ Name | `website_sale.dynamic_filter_template_product_product_mini_name` | `s_product_product_mini_name` |

### Blogs / News
| Style | TEMPLATE_KEY | TEMPLATE_CLASS |
|---|---|---|
| Big Picture | `website_blog.dynamic_filter_template_blog_post_big_picture` | `s_blog_post_big_picture` |
| Card Layout | `website_blog.dynamic_filter_template_blog_post_card` | `s_blog_post_card` |
| Horizontal | `website_blog.dynamic_filter_template_blog_post_horizontal` | `s_blog_post_horizontal` |
| List Layout | `website_blog.dynamic_filter_template_blog_post_list` | `s_blog_post_list` |

---

## 4) 可用 Custom Classes

> 使用方式：class 與 data-custom-name **同步加入**。

### Products (Custom Classes)
- `scaleL` / `scaleS`
- `nameHoverUnderLine`
- `imgNoMargin`
- `arrowRight`
- `titleHoverFull`

### Blogs / News (Custom Classes)
- `cardRadius`
- `cardRadiusS`
- `borderHover`
- `hoverUnderLine`
- `titleLine`
- `blockLine`
- `picTop`
- `picBottom`
- `dateTop`

---

## 5) 使用限制（必遵守）

- **禁止改 inner DOM**：`dynamic_snippet_template` 內的卡片由 Odoo 動態生成。
- **禁止包多餘 div**：只能用既有 snippet 結構。
- **允許的父層**：若需多欄，只能放在 `s_text_block` 或 `s_column_layout` 內。
- **樣式覆寫**：需改視覺效果請寫 SCSS，不要改 XML 結構。
