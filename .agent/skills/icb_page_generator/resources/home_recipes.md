# Home 頁面配方 (Home Recipes)

> AI 使用說明：每個配方列出各區塊的 `data-snippet`、關鍵 class、重要 `data-*` 屬性，
> 直接照此組裝 XML，不需要再回查 home-recipes 目錄（已移除）。
> SCSS 請依各區塊的 `s_custom_*` 名稱到對應元件檔取樣。

---

## home-1

**區塊順序：**

### 1. Banner — `bannerGeometricTriangle`
```
data-snippet="s_carousel"
class: s_carousel_wrapper o_full_screen_height s_custom_bannerGeometricTriangle
data-custom-name="bannerGeometricTriangle"
container: oe_unremovable container（內層）
SCSS: banners/banner.scss
```

### 2. Feature Icons — `iconCardHorizontal 1x1`
```
data-snippet="s_static_snippet"
class: s_static_snippet o_colored_level s_custom_iconCardHorizontal s_custom_1x1
data-staticsnippet-template="horizontal"
data-custom-name="iconCardHorizontal 1x1"
container: container（4 欄 col-lg-6，橫式 icon 卡）
SCSS: content-sections/content-sections.scss
```

### 3. Products — `upperNext + products01`
```
外層 data-snippet="s_column_layout"
class: s_column_layout o_colored_level s_custom_upperNext s_custom_fullContainer s_custom_hasArrowL
data-custom-name="upperNext fullContainer hasArrowL"
container: container-fluid，左欄 col-lg-8 offset-lg-2 + 右欄 col-lg-10

  內層動態產品：
  data-snippet="s_dynamic_snippet_products"
  class: s_dynamic_snippet_products s_dynamic o_colored_level s_product_product_borderless_1
         s_custom_products01 s_custom_titleUp s_custom_nameHoverUnderLine
         s_custom_arrowRight s_custom_arrowL s_custom_arrowNoSeparate s_custom_arrowNoGap
         s_custom_noGap s_custom_scaleL s_custom_fullContainer s_custom_default
  data-template-key="website_sale.dynamic_filter_template_product_product_borderless_1"
  data-number-of-elements="4"  data-number-of-records="16"
  data-custom-name="products01 titleUp nameHoverUnderLine arrowRight arrowL scaleL fullContainer default"
SCSS: dynamic/products/customized-dynamic-products.scss
```

### 4. Carousel — `carouselHoverBgEffect`
```
data-snippet="s_static_carousel"
class: s_static_carousel o_colored_level s_custom_carouselHoverBgEffect s_custom_arrowTop s_custom_arrowRight s_custom_default
data-number-of-elements="3"  data-number-of-elements-small-devices="1"
data-custom-name="carouselHoverBgEffect arrowTop arrowRight default"
container: container
SCSS: carousels/customized-static-carousel.scss
```

### 5. 圖文區 — `s_text_image + titleUnderLine`
```
data-snippet="s_image_text" （parallax 背景）
class: s_text_image o_colored_level s_custom_titleUnderLine
data-custom-name="titleUnderLine"
container: container，row 左圖 col-lg-6 + 右文 col-lg-6
SCSS: docs/design/user_custom_rules.scss
```

### 6. News — `newsSummary + hoverUnderLine`
```
外層 data-snippet="s_column_layout"，左欄 col-lg-5 + 右欄 col-lg-7

  左欄：大圖部落格
  data-snippet="s_blog_posts"
  class: s_blog_posts s_dynamic_snippet_blog_posts s_dynamic o_colored_level
         s_blog_post_big_picture s_custom_hoverUnderLine
  data-template-key="website_blog.dynamic_filter_template_blog_post_big_picture"
  data-number-of-elements="1"  data-number-of-records="1"
  data-custom-name="hoverUnderLine"

  右欄：條列新聞
  data-snippet="s_blog_posts"
  class: s_blog_posts s_dynamic_snippet_blog_posts s_dynamic o_colored_level
         s_blog_post_card s_custom_newsSummary s_custom_noPic s_custom_hoverUnderLine
         s_custom_dateLeft s_custom_default
  data-template-key="website_blog.dynamic_filter_template_blog_post_card"
  data-number-of-elements="1"  data-number-of-records="4"
  data-custom-name="newsSummary noPic hoverUnderLine dateLeft default"
SCSS: dynamic/news/customized-dynamic-news.scss
```

---

## home-2

**區塊順序：**

### 1. Banner — Odoo 原生輪播
```
data-snippet="s_carousel"
class: s_carousel_wrapper（無自訂 class，使用系統預設）
container: oe_unremovable container
```

### 2. Feature Icons — `iconCardHorizontal 1x1`
```
data-snippet="s_static_snippet"
class: s_static_snippet o_colored_level s_custom_iconCardHorizontal s_custom_1x1
data-staticsnippet-template="horizontal"
data-custom-name="iconCardHorizontal 1x1"
SCSS: content-sections/content-sections.scss
```

### 3. 三段式背景穿插 — `threeChains`
```
外層 s_column_layout 或 s_vertical_layout
class: s_custom_threeChains s_custom_fullContainer
data-custom-name="threeChains fullContainer"
內含：圖文區 s_custom_textInnerBg + titleUnderLine、s_custom_horizontalWrap
SCSS: content-sections/content-sections.scss
```

### 4. Carousel — `staticCarousel2`
```
data-snippet="s_static_carousel"
class: s_static_carousel o_colored_level s_custom_staticCarousel2 s_custom_fullContainer
       s_custom_inherit s_custom_arrowTop s_custom_arrowRight s_custom_default s_custom_imgNoMargin
data-number-of-elements="4"  data-number-of-elements-small-devices="1"
data-custom-name="staticCarousel2 fullContainer inherit arrowTop arrowRight default imgNoMargin"
SCSS: carousels/customized-static-carousel.scss
```

### 5. 視差背景品牌區 + Counter — `counterPrimary`
```
data-snippet="s_vertical_layout"（parallax 背景）
  內層 counter：
  class: s_text_block o_colored_level s_custom_counterPrimary
  data-custom-name="counterPrimary"
  使用 s_counting data-count-to="30/200/45"
SCSS: content-sections/content-sections.scss
```

### 6. 動態部落格 News
```
data-snippet="s_dynamic_snippet_carousel"
class: s_dynamic_snippet_carousel s_dynamic o_colored_level s_blog_post_card
       s_custom_arrowRight s_custom_arrowTop
data-template-key="website_blog.dynamic_filter_template_blog_post_card"
data-number-of-elements="4"  data-number-of-records="16"
data-custom-name="arrowRight arrowTop"
SCSS: dynamic/news/customized-dynamic-news.scss
```

---

## home-3

**區塊順序：**

### 1. Banner — `text-left-middle`（左文影片背景）
```
data-snippet="s_carousel"
class: s_carousel_wrapper o_full_screen_height s_custom_textleftmiddle
data-custom-name="text-left-middle"
SCSS: banners/banner.scss
```

### 2. 文字介紹 + Counter — `insertBelow`
```
data-snippet="s_column_layout"
class: s_column_layout o_colored_level s_custom_insertBelow s_custom_fullContainer
data-custom-name="insertBelow fullContainer"
  右欄 counter：s_custom_fullContainer，使用 s_counting data-count-to="70/500/300"
SCSS: content-sections/content-sections-2.scss
```

### 3. 靜態分類卡片 — `fullWrapProduct`（靜態）
```
data-snippet="s_static_snippet"
class: s_static_snippet o_colored_level s_custom_fullWrapProduct s_custom_imgNoMargin s_custom_fullContainer s_custom_default
data-staticsnippet-template="default"
data-custom-name="fullWrapProduct imgNoMargin fullContainer default"
SCSS: dynamic/products/customized-dynamic-products.scss
```

### 4. 動態產品 — `fullWrapProduct`（動態版）
```
data-snippet="s_dynamic_snippet"
class: s_dynamic_snippet s_dynamic o_colored_level s_product_product_centered
       s_custom_fullWrapProduct s_custom_fullContainer s_custom_default
data-template-key="website_sale.dynamic_filter_template_product_product_centered"
data-number-of-elements="4"  data-number-of-records="8"
data-custom-name="fullWrapProduct fullContainer default"
SCSS: dynamic/products/customized-dynamic-products.scss
```

### 5. 交錯磚牆卡片 — `staggerBricks`
```
data-snippet="s_static_snippet"
class: s_static_snippet o_colored_level s_custom_staggerBricks s_custom_default
data-custom-name="staggerBricks default"
SCSS: content-sections/content-sections-2.scss
```

### 6. 全螢幕視差 × 2 — `fullScreenParallax`
```
data-snippet="s_parallax"
class: s_parallax parallax s_parallax_is_fixed o_colored_level o_auto_screen_height
（無 s_custom_，使用系統 parallax 結構）
SCSS: carousels/customized-Static-Snippet.scss
```

### 7. 動態部落格 News
```
data-snippet="s_dynamic_snippet_carousel"
class: s_dynamic_snippet_carousel s_dynamic o_colored_level s_blog_post_card
data-template-key="website_blog.dynamic_filter_template_blog_post_card"
data-number-of-elements="4"  data-number-of-records="16"  data-carousel-interval="5000"
SCSS: dynamic/news/customized-dynamic-news.scss
```

---

## home-4

**區塊順序：**

### 1. Banner — `pureVideoBanner`（純影片滿版）
```
data-snippet="s_carousel"
class: s_carousel_wrapper s_custom_pureVideoBanner
data-custom-name="pureVideoBanner"
  內層輪播張數：data-snippet="s_static_carousel" s_custom_default，data-number-of-elements="1"
SCSS: banners/banner.scss
```

### 2. 固定側欄最新消息 — `exhibitionUpdates fixed`
```
data-snippet="s_vertical_layout"
class: s_vertical_layout o_colored_level s_custom_exhibitionUpdates s_custom_fixed
data-custom-name="exhibitionUpdates fixed"
  控制列：s_custom_controlBtn
  隱藏區：s_custom_hidden
SCSS: content-sections/content-sections-3.scss
```

### 3. 靜態卡片 + 動態產品輪播 — `productRightScroll`
```
data-snippet="s_vertical_layout"

  靜態骨架：
  data-snippet="s_static_snippet"
  class: s_static_snippet o_colored_level s_custom_productRightScroll
  data-custom-name="productRightScroll"

  動態產品：
  data-snippet="s_dynamic_snippet"
  class: s_dynamic_snippet s_dynamic o_colored_level s_product_product_borderless_1 s_custom_productRightScroll
  data-template-key="website_sale.dynamic_filter_template_product_product_borderless_1"
  data-number-of-elements="4"  data-number-of-records="6"
  data-custom-name="productRightScroll"
SCSS: content-sections/content-sections-js.scss + dynamic/products/customized-dynamic-products-js.scss
```

### 4. Counter — `counterAfterColor`
```
data-snippet="s_text_block"
class: s_text_block o_colored_level s_custom_counterAfterColor
data-custom-name="counterAfterColor"
使用 s_counting data-count-to="70/18/25"，搭配 s_text 說明文字
SCSS: content-sections/content-sections-3.scss
```

### 5. 互動地圖 — `map-Effect`
```
data-snippet="s_text_block"
class: s_text_block o_colored_level s_custom_mapEffect
data-custom-name="map-Effect"
  內層結構：
  - div.s_text.map-brief-description（地圖標示區 × N）
  - div.s_text.map-img（地圖圖片）
  - div.s_text.map-info（內容小區 × N）
SCSS: content-sections/content-sections-js.scss
```

### 6. 交錯輪播 — `interlace-Carousel`
```
data-snippet="s_static_carousel"
class: s_static_carousel o_colored_level s_custom_interlaceCarousel s_custom_arrowTop s_custom_arrowRight s_custom_scaleS
data-number-of-elements="3"  data-number-desktop="3"
data-custom-name="interlace-Carousel arrowTop arrowRight scaleS"
SCSS: carousels/customized-Static-Snippet.scss
```

### 7. 動態部落格 News — `text-Upper`
```
data-snippet="s_dynamic_snippet_carousel"
class: s_dynamic_snippet_carousel s_dynamic o_colored_level s_blog_post_card
       s_custom_textUpper s_custom_default s_custom_arrowTop s_custom_arrowRight
data-template-key="website_blog.dynamic_filter_template_blog_post_card"
data-number-of-elements="3"  data-number-of-records="9"  data-carousel-interval="8000"
data-custom-name="text-Upper default arrowTop arrowRight"
SCSS: dynamic/products/customized-dynamic-products.scss
```

### 8. CTA 字壓圖 — `titleUpperBg2`
```
data-snippet="s_text_block" 或 s_vertical_layout
class: s_custom_titleUpperBg2 s_custom_scaleL s_custom_default
data-custom-name="titleUpperBg2 scaleL default"
SCSS: content-sections/content-sections-3.scss
```
