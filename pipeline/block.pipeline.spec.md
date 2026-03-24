# ICB /block Pipeline Spec

## Goal
Return a single reusable block as a section-only output.

## Steps
1. **Identify intent**
   - Confirm command is `/block`.
   - Identify the requested block or custom history reference.

2. **Load System policies (Layer 1)**
   - Apply core rules (no inline <style>, SCSS separate).

3. **Minimal retrieval (Layer 2)**
   - Load only the referenced block/resource files.

4. **Build task contract (Layer 3)**
   - Create a task object conforming to `schema/page_task.schema.json`.

5. **Generate outputs**
   - Output section-only XML (no QWeb wrapper).
   - Output SCSS only if needed.

6. **Validate**
   - Run: `python scripts/validate_dynamic_lock.py outputs/ --no-qweb-check`

7. **Deliver**
   - Provide output paths.

## Notes
- `/block` outputs a single `<section>` by default.
