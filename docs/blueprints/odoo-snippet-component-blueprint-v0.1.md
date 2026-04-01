# Odoo Snippet to Component Blueprint v0.1

## 1) Goal and Scope
- Define a standard for turning Odoo snippets into reusable components.
- Naming must reflect real structure.
- Scope: initial coverage for the selected types in this version.
- Out of scope: inventing new SCSS or altering locked Odoo structures.

## 2) Types (v0.1)
- dynamic
- dynamic_carousel
- static
- snippet_carousel
- faq_collapse
- s_tabs
- countdown

## 3) Structure Rules
- Core structure must follow:
  - section > container or container-fluid > row > col
- Inner content must use Odoo allowed elements/classes only:
  - h1/h2/h3/p/a/img
  - .o_we_bg_filter (overlay)
  - .s_parallax_bg (background layer)
  - .o_cc (color block)
  - .lead (subtitle)
- Any snippet with multiple template variants must use templates/ as the source of truth.

## 4) Naming Rules
- name: structure-driven and human readable (example: hero_banner, feature_grid).
- type: from the Types list above.
- category: layout/content/interaction (or other agreed buckets).
- odoo_snippet_id: optional in v0.1, to be filled later.

## 5) Custom Name Rule (Section)
- Allow data-custom-name on section (required if custom class used).
- Custom class is allowed only when paired with data-custom-name.
- The section naming format follows existing catalog rules:
  - PascalCase
  - No spaces, dashes, or underscores
  - Multiple names separated by spaces in data-custom-name
  - Corresponding class: s_custom_YourName

## 6) Styles and Resources
- Use existing Odoo classes for effects (parallax, overlay, spacing, animation).
- Do not create new SCSS during collection unless a rule already exists.
- Images: https://picsum.photos/
- Icons: Font Awesome v4

## 7) Output and Acceptance
- Output as Component definition JSON.
- Acceptance:
  - Structure matches required nesting.
  - Only allowed inner classes used.
  - Required/optional fields are complete.
  - data-custom-name + custom class rules respected.

## 8) Common Errors
- Naming does not match actual structure.
- Using disallowed inner classes.
- Adding custom SCSS during collection.
- Custom class without data-custom-name.

## 9) Version and Change Log
- v0.1: initial structure rules, naming rules, and type list.

## Appendix: Component JSON Example
```json
{
  "name": "hero_banner",
  "type": "hero",
  "category": "layout",
  "structure": "section > container > row > col",
  "fields": {
    "required": ["title", "background_image"],
    "optional": ["subtitle", "button_text", "button_link"]
  },
  "features": ["background_image", "overlay", "cta_button"],
  "style_options": ["dark_mode", "light_mode", "center_align"],
  "best_for": ["landing_page", "branding"],
  "not_for": ["product_list"],
  "odoo_snippet_id": "s_banner",
  "version": "v1"
}
```
