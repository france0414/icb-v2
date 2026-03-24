# ICB /create Pipeline Spec

## Goal
Create a new layout by first producing a text skeleton, then generating XML/SCSS after user confirmation.

## Steps
1. **Identify intent**
   - Confirm command is `/create`.
   - Capture required page type, theme cues, and dynamic needs.

2. **Load System policies (Layer 1)**
   - Use immutable rules (QWeb wrapper, output path, dynamic locks, header/footer constraints).

3. **Minimal retrieval (Layer 2)**
   - Read `templates_index.json` only for reference patterns.
   - Do not copy full structures; use as style/structure reference only.

4. **Phase A: Text skeleton**
   - Output section-by-section text outline.
   - Wait for user confirmation.

5. **Build task contract (Layer 3)**
   - Create task object conforming to `schema/page_task.schema.json`.
   - Include required locks and outputs.

6. **Generate outputs**
   - Produce XML/SCSS based on confirmed skeleton.

7. **Validate**
   - Ensure dynamic locked structures are not modified.
   - Ensure header is SCSS-only, footer XPath when used.

8. **Deliver**
   - Output XML/SCSS in `outputs/` with timestamps.

## Notes
- `/create` uses Phase A skeleton; no plan file is generated.
