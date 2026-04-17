# Dynamic Products Matrix (Base-First)

> 目的：把動態產品區塊拆成「固定骨架」與「可變參數」，讓樣板可以快速組裝。
> 主結構來源：`templates/base/base-dynamic-products.xml`

---

## A. 固定骨架（不可改）

```xml
<section data-snippet="s_dynamic_snippet_products | s_dynamic_snippet_carousel" ...>
  <div class="o_not_editable container">
    <div class="css_non_editable_mode_hidden">
      <div class="missing_option_warning alert alert-info rounded-0 fade show d-none d-print-none o_default_snippet_text"/>
    </div>
    <div class="dynamic_snippet_template"/>
  </div>
</section>
```

---

## B. 可變參數欄位

- `data-snippet`: `s_dynamic_snippet_products` / `s_dynamic_snippet_carousel`
- `data-template-key`: product template key
- `data-filter-id`: Products 建議 `3`
- `data-product-category-id`: 通常 `all`
- `data-number-of-elements`
- `data-number-of-elements-small-devices`
- `data-number-of-records`
- `data-carousel-interval`（carousel 常用）
- `class` 上的 `s_custom_*`
- `data-custom-name`（需與 `s_custom_*` token 同步）

---

## C. Products 變體對照（第一版）

來源：`templates/base/base-dynamic-products.xml`

| Variant ID | 用途 | data-snippet | TEMPLATE_KEY | Elements | Records | Interval | 主要 Class / Token |
|---|---|---|---|---:|---:|---:|---|
| `prod_borderless_1_grid` | Borderless n1 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_borderless_1` | 4 | 16 | 200000 | `s_product_product_borderless_1` |
| `prod_borderless_1_carousel` | Borderless n1 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_borderless_1` | 4 | 16 | 10000 | `s_product_product_borderless_1`, `nameHoverUnderLine`, `scaleL`, `arrowRight`, `titleHoverFull` |
| `prod_borderless_2_grid` | Borderless n2 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_borderless_2` | 4 | 16 | 5000 | `s_product_product_borderless_2`, `scaleL`, `nameHoverUnderLine` |
| `prod_borderless_2_carousel` | Borderless n2 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_borderless_2` | 4 | 16 | 5000 | `s_product_product_borderless_2`, `scaleL` |
| `prod_centered_grid` | Centered 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_centered` | 4 | 16 | 5000 | `s_product_product_centered`, `nameHoverUnderLine`, `scaleL` |
| `prod_centered_carousel` | Centered 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_centered` | 4 | 16 | 5000 | `s_product_product_centered`, `nameHoverUnderLine`, `scaleL` |
| `prod_classic_carousel_fx` | Classic 輪播（含特效） | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_add_to_cart` | 4 | 16 | 5000 | `s_product_product_add_to_cart`, `imgNoMargin`, `nameHoverUnderLine`, `scaleL` |
| `prod_classic_carousel_basic` | Classic 輪播（基礎） | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_add_to_cart` | 4 | 16 | 50000 | `s_product_product_add_to_cart` |
| `prod_detail_grid` | Detailed 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_view_detail` | 4 | 16 | 5000 | `s_product_product_view_detail`, `scaleL`, `nameHoverUnderLine` |
| `prod_detail_carousel` | Detailed 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_view_detail` | 4 | 16 | 50000 | `s_product_product_view_detail`, `scaleL`, `nameHoverUnderLine` |
| `prod_horizontal_grid` | Horizontal 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_horizontal_card` | 3 | 16 | 5000 | `s_product_product_horizontal_card`, `textTop`, `scaleL` |
| `prod_horizontal_carousel` | Horizontal 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_horizontal_card` | 3 | 16 | 5000 | `s_product_product_horizontal_card`, `textTop`, `scaleL` |
| `prod_mini_image_grid` | Image only 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_mini_image` | 4 | 16 | 5000 | `s_product_product_mini_image`, `scaleL` |
| `prod_mini_image_carousel` | Image only 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_mini_image` | 4 | 16 | 5000 | `s_product_product_mini_image`, `scaleL` |
| `prod_mini_name_grid` | Image+Name 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_mini_name` | 4 | 16 | 5000 | `s_product_product_mini_name`, `scaleL` |
| `prod_mini_name_carousel` | Image+Name 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_mini_name` | 4 | 16 | 5000 | `s_product_product_mini_name`, `scaleL` |
| `prod_mini_price_grid` | Image+Price 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_mini_price` | 4 | 16 | 5000 | `s_product_product_mini_price`, `scaleL` |
| `prod_banner_grid` | Large Banner 區塊 | `s_dynamic_snippet_products` | `website_sale.dynamic_filter_template_product_product_banner` | 1 | 16 | 5000 | `s_product_product_banner`, `scaleL`, `nameHoverUnderLine` |
| `prod_banner_carousel` | Large Banner 輪播 | `s_dynamic_snippet_carousel` | `website_sale.dynamic_filter_template_product_product_banner` | 1 | 16 | 200000 | `s_product_product_banner`, `scaleL`, `imgNoMargin`, `nameHoverUnderLine` |

---

## D. 套用規則

1. 先用 `base-dynamic-products.xml` 的父層 section 版型（標題/分段容器）。
2. 動態 section 僅調整參數，不改 `dynamic_snippet_template` 內部。
3. 優先使用既有 `s_custom_*` token；無對應時再補 SCSS。
4. `data-custom-name` 必須與 class token 對應，避免重複 token。

---

## E. 清理注意事項

- 若看到空 token（例如 `s_custom_`）視為噪音，不應再新增。
- 若 `data-custom-name` 重複詞（例如 `nameHoverUnderLine` 連續重複）可在整理版修正為唯一值。
- 保留 Odoo 動態欄位（`data-filter-id`、`data-template-key`、`data-number-of-records` 等），不要因精簡而刪除。
