# ICB /clone Pipeline Spec

## Goal
Translate external layouts into Odoo-compatible drafts in the sandbox (outputs/), without promoting to templates.

## Steps
1. **Identify intent**
   - Confirm command is `/clone`.
   - Capture target URL and scope.

2. **Load System policies (Layer 1)**
   - Use scraping sandbox rules (outputs only, no templates write).
   - Preserve QWeb wrapper and dynamic snippet rules.

3. **Minimal retrieval (Layer 2)**
   - Use Playwright MCP first.
   - Avoid paid services unless user explicitly requests.

4. **Structure-first translation**
   - Prioritize layout using Bootstrap rows/cols.
   - Only add SCSS when structure cannot match.

5. **Build task contract (Layer 3)**
   - Create task object conforming to `schema/page_task.schema.json`.
   - Include dynamic locks if needed.

6. **Generate outputs**
   - Output XML/SCSS into `outputs/`.

7. **Validate**
   - Ensure no dynamic fake cards.
   - Ensure output respects QWeb wrapper.

8. **Deliver**
   - Provide output paths.

## Notes
- Default is draft only; do not promote to templates unless requested.
