---
description: Standardized workflow for generating Odoo pages (Static & Dynamic)
---

# Odoo Page Generation Workflow

This workflow defines the standard operating procedure (SOP) for generating Odoo 14 webpage code. It enforces strict adherence to documentation to ensure consistency and correctness.

## 1. Analyze Request Type

First, determine the nature of the request:

-   **Static Content**: General layouts, text, images, feature grids.
-   **Dynamic Content**: Automatically fetching records (Products, Blogs, Events).
-   **Static Navigation**: Links to categories (e.g., "Shop by Category"), even if they look like product cards.

## 2. Dynamic vs. Static Decision Tree

### 🔴 IF Dynamic (Products/Blogs Listings)
> **Goal**: Show "Latest Products", "Best Sellers", "News Carousel".

1.  **MANDATORY**: You **MUST** read `docs/ODOO_DYNAMIC_RULES.md`.
2.  **Structure**: Use `s_dynamic_snippet_products` or `s_dynamic_snippet_blog_posts`.
3.  **Forbidden**: Do NOT wrap these in custom `div`s. Only nest within `s_text_block` or `s_column_layout`.
4.  **Classes**: Use `data-custom-name` correlated with `s_custom_` classes as defined in the rules.

### 🟡 IF Static Navigation (Product Categories)
> **Goal**: Show clickable cards for "Men", "Women", "Accessories".

1.  **MANDATORY**: Treat this as **STATIC** content.
2.  **Structure**: Use `s_three_columns`, `s_media_list`, or `s_masonry_block`.
3.  **Forbidden**: Do **NOT** use `s_dynamic_snippet` for categories.

### 🟢 IF Standard Static Page
> **Goal**: Homepage, About Us, Contact, Landing Page.

1.  **Reference**: `docs/ODOO_RULES_AI.md` (Core Design) & `docs/ODOO_LAYOUT_RULES.md`.
2.  **Images**: Use `https://picsum.photos/` for placeholders.
3.  **Hero**: Flexible color choice (`o_cc1` - `o_cc5`) passed on design needs.

## 3. Button Styling Check

Does the design require specific button effects (Skew, Arrows, Flash, Dot Zoom)?

-   **YES**: You **MUST** read `docs/ODOO_BUTTON_STYLES.md`.
    -   Use the exact SCSS provided.
    -   Add the corresponding `s_custom_btnXX` class.
-   **NO**: Use standard Bootstrap classes (`btn-primary`, `btn-outline-secondary`, `rounded-circle`, `flat`).

## 4. Code Generation Steps

1.  **Skeleton**: Start with `<div id="wrap" class="oe_structure oe_empty">`.
2.  **Snippets**: Assemble the page using **only** accepted Odoo snippets (e.g., `s_banner`, `s_text_block`, `s_call_to_action`).
3.  **Attributes**: Ensure all `data-snippet` and `data-name` attributes are correct.
4.  **Polish**: Apply utility classes (`pt32`, `pb32`, `o_colored_level`).

## 5. Final Output

Return two distinct blocks:
1.  **XML**: The QWeb template.
2.  **SCSS**: The accompanying CSS/SCSS (including button styles if applicable).
