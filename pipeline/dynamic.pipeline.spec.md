# ICB /dynamic Pipeline Spec

## Goal
Insert dynamic snippets using locked base templates without altering inner structure.

## Steps
1. **Identify intent**
   - Confirm command is `/dynamic`.
   - Determine target: products or news/blog.

2. **Load System policies (Layer 1)**
   - Use immutable rules for dynamic locked structures.

3. **Minimal retrieval (Layer 2)**
   - Read `templates_index.json`.
   - Select `base-dynamic-products` or `base-dynamic-news`.
   - Load corresponding HTML reference only for class discovery.

4. **Build task contract (Layer 3)**
   - Create task object conforming to `schema/page_task.schema.json`.
   - Include `structure_locked` policy and allowed/forbidden ops.

5. **Generate outputs**
   - Output XML in `outputs/` with timestamp.
   - Section-only output is allowed (no QWeb wrapper) when returning a single snippet.
   - Only add section-level class or `data-custom-name` if needed.
   - Output SCSS only if new styles are required.

6. **Validate**
   - Ensure no inner DOM changes.
   - Ensure `data-template-key` is unchanged.
   - Run: `python scripts/validate_dynamic_lock.py outputs/`
   - If section-only output is used, add `--no-qweb-check`.

7. **Deliver**
   - Provide XML/SCSS output paths.

## Notes
- HTML reference is for class name discovery only.
- No plan file is generated during `/dynamic` execution.
