# ICB /page Pipeline Spec

## Goal
Provide a deterministic, low-token pipeline for `/page` generation by separating policy, retrieval, task contract, generation, and validation.

## Steps
1. **Identify intent**
   - Confirm command is `/page`.
   - Extract required page type and any explicit template references.

2. **Load System policies (Layer 1)**
   - Use immutable rules from core policy (QWeb wrapper, output path, dynamic locks, header/footer constraints).

3. **Minimal retrieval (Layer 2)**
   - Read `templates_index.json`.
   - Select only the needed templates by name/category/usage.
   - If dynamic snippets are involved, prefer base dynamic templates and enforce `structure_locked` rules.

4. **Build task contract (Layer 3)**
   - Create a task object conforming to `schema/page_task.schema.json`.
   - Include explicit `locks` and `allowed/forbidden_ops` from index.
   - List exact expected output files (XML/SCSS).

5. **Generate outputs**
   - Use contract to generate XML/SCSS.
   - Do not expand retrieval beyond what was selected in step 3.

6. **Validate**
   - Check `structure_locked` targets are untouched.
   - If footer is involved, ensure XPath output.
   - If header is involved, ensure SCSS-only output.

7. **Deliver**
   - Output XML/SCSS into `outputs/` with timestamped filenames.

## Notes
- No plan file is generated during `/page` execution.
- For dynamic blocks, HTML reference is used only for class discovery in SCSS.
