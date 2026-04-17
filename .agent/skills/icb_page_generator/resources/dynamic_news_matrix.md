# Dynamic News Matrix (Base-First)

> 目的：把動態消息區塊的「固定骨架」與「可變參數」拆開。
> 先用 `templates/base/base-dynamic-news.xml` 當主結構，再用本表決定每一個變體要套的參數。

---

## A. 固定骨架（不可改）

以下結構視為 contract，禁止手刻 inner DOM：

```xml
<section data-snippet="s_dynamic_snippet | s_dynamic_snippet_carousel" ...>
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

- `data-snippet`: `s_dynamic_snippet` / `s_dynamic_snippet_carousel`
- `data-template-key`: blog template key
- `data-filter-id`: 建議 News 使用 `1`
- `data-number-of-elements`
- `data-number-of-elements-small-devices`
- `data-number-of-records`
- `data-carousel-interval`（只有 carousel）
- `class` 上的 `s_custom_*`
- `data-custom-name`（需與 `s_custom_*` token 同步）

---

## C. News 變體對照（第一版）

來源：`templates/improved/dynamic/news/customized-dynamic-news.xml`

| Variant ID | 用途 | data-snippet | TEMPLATE_KEY | Filter | Elements | Records | Interval | 主要 Class / Token |
|---|---|---|---|---:|---:|---:|---:|---|
| `news_hero_big_picture` | 首則大圖 | `s_blog_posts` | `website_blog.dynamic_filter_template_blog_post_big_picture` | 9 | 1 | 1 | - | `s_blog_post_big_picture`, `s_custom_hoverUnderLine` |
| `news_summary_no_pic` | 清單摘要（右欄） | `s_blog_posts` | `website_blog.dynamic_filter_template_blog_post_card` | 1 | 1 | 4 | - | `s_blog_post_card`, `s_custom_newsSummary`, `s_custom_noPic`, `s_custom_hoverUnderLine`, `s_custom_dateLeft` |
| `news_card_carousel` | 卡片輪播 | `s_dynamic_snippet_carousel` | `website_blog.dynamic_filter_template_blog_post_card` | 1 | 3 | 9 | 8000 | `s_blog_post_card`, `s_custom_textUpper`, `s_custom_default`, `s_custom_arrowTop`, `s_custom_arrowRight` |

---

## D. 套用規則（給 AI / 模板轉換）

1. 先建立版面容器（如 `s_column_layout` / `s_vertical_layout`），再放動態 section。
2. 動態 section 只改參數，不改內部 `dynamic_snippet_template` 結構。
3. 需要客製外觀時，優先套現有 `s_custom_*`；若無對應才補 SCSS。
4. `data-custom-name` 必須是 class token 去掉 `s_custom_` 的同步字串（空白分隔）。

---

## E. 後續擴充欄位（預留）

- `data-filter-by-blog-id`
- `data-blog-sort-id`
- `data-force-minimum-max-limit-to16`
- CTA 行為（More News / Read more）
