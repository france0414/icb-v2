# Editability Execution Checklist (Odoo)

Purpose: enforce a pre-execution check whenever a page/block includes editable content.

## Mandatory pre-check before implementation

1. Read and confirm rules from:
   - `.agent/skills/icb_page_generator/resources/editability_rules.md`
   - `.agent/skills/icb_page_generator/resources/snippet_rules.md`
   - `.agent/skills/icb_page_generator/resources/spacing_rules.md`

2. Verify structure plan before coding:
   - Text is in real HTML elements (`h1-h6`, `p`, `li`, `a`)
   - Image is replaceable (`img` or Odoo editable background)
   - Wrapper depth stays minimal
   - No style/content coupling that blocks Odoo editor selection

3. If card must be fully clickable:
   - Parent: `position-relative s_custom_clickableCard`
   - Existing link: `s_custom_cardLink`
   - Overlay allowed only in non-editor mode:
     - `#wrapwrap:not(.odoo-editor-editable) .s_custom_cardLink::before { position:absolute; inset:0; }`
   - Never use `stretched-link`

## Execution gate (must pass before applying changes)

- Confirm heading semantics are valid (single `h1`, then logical hierarchy)
- Confirm editable text blocks are not trapped by link overlays
- Confirm absolute/overlay elements have corresponding `position: relative` parent
- Confirm editor-mode safety guard is applied for overlap/overlay behavior

## Agent operating rule

Before any XML/SCSS modification touching editable sections, run this checklist first.
If any item is unclear, resolve structure first, then implement.

## Theme-first rule (ICB/Odoo theme)

This project already has system theme colors and mapped text colors.

1. When using system theme backgrounds, prefer existing theme classes/tokens first:
   - `o_cc1`~`o_cc5` (and project-defined `o_cg*` groups if available)
2. Do not hardcode equivalent theme colors in SCSS when theme tokens/classes already cover the need.
3. Do not manually override text color on themed blocks unless there is a confirmed contrast/accessibility issue.
4. Avoid writing CSS that locks system theme behavior and reduces backend editability.

In short: use system theme for color/text pairing first; custom SCSS only fills layout/interaction gaps.

## Grid-first layout rule (ICB/Odoo)

For list/detail structures (left image + right text, or reversed):

1. Build with Bootstrap 4.5 grid first (`row` + `col-*`), not custom hardcoded width ratios.
2. Default behavior should remain editable in Odoo editor (users can drag/adjust structure in backend).
3. Do not hardcode image/text percentage ratios in SCSS unless user explicitly requests fixed ratio.
4. Use Bootstrap breakpoints (`col-1`~`col-12`, `col-sm-*`, `col-md-*`, `col-lg-*`, `col-xl-*`) for responsive control.
5. Only add SCSS for gaps that grid/utilities cannot solve.

In short: structure with grid first, keep proportions editor-friendly, customize only when required.

## Routing rule for list -> detail

For project-created pages, list items should link directly to the target page route.

- Preferred: direct detail route, e.g. `/data-run-detail`
- Avoid adding an extra routing layer like `/applications/...` unless explicitly required

## Information architecture classification gate

Before building any list/detail page, classify each item into exactly one type:

1. `application_track` (single-line application entry)
2. `solution` (problem/benefit-oriented solution entry)
3. `taxonomy_node` (tree category/subcategory node)

Execution rules:

- All items in the same view must share a consistent outer frame pattern (same shell and hierarchy).
- Do not mix application cards, solution cards, and taxonomy nodes in one ambiguous wrapper.
- If mixed content is required, split into separate sections with explicit type labels and routing intent.
- Routing follows type:
  - `application_track` -> direct detail page route
  - `solution` -> solution detail route
  - `taxonomy_node` -> category/subcategory index route

In short: classify first, then choose one consistent outer frame per type.

## Snippet-first composition rule

Before building any section:

1. Start from Odoo native snippet composition logic and valid hierarchy.
2. Prefer conservative snippet shells first:
   - `s_text_block`
   - `s_banner`
   - `s_image_text`
3. Keep wrapper hierarchy correct first; visual refinement comes after structure validity.
4. Evaluate layout with meaningful structure classes (`row`, `col-*`, and project-defined structural classes) instead of ad-hoc wrappers.

Note:
- `s_text` is not treated as a section shell here; it is a div-level content wrapper for editable inline text blocks.

## Text block handling rule

For editable text-heavy sections:

1. Use `s_text` as the safest content wrapper for editable spacing and backend manipulation.
2. If title and body both use `<p>`, separate them into different editable wrappers (or distinct structural blocks).
3. Do not place title/body in a single merged text container when independent style targeting is required.

In short: snippet shell first, then clean row/col structure, then split editable text units for reliable style control.
