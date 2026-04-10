# TODO Roadmap Restructure Design

Date: 2026-04-09

## Context
`TODO.md` currently mixes near-term action items, long-term roadmap detail, and historical discussion snapshots. Project rules require checking `TODO.md` before continuing work, so excessive detail slows startup and increases cognitive load.

The desired state is: `TODO.md` stays a lightweight execution entrypoint, while `docs/roadmap/` becomes the long-term roadmap home. The user confirmed `docs/roadmap/` as the destination and prefers a single consolidated Phase file rather than per-Phase files.

## Goals
- Keep `TODO.md` quick to scan for active work.
- Preserve all roadmap detail and historical discussion content.
- Establish a stable, searchable structure under `docs/roadmap/`.
- Ensure the location and linking rules are explicit and repeatable.

## Non-Goals
- No content rewriting beyond reorganizing and linking.
- No new roadmap items are created or removed; only moved.
- No changes to project rules outside `TODO.md` and new roadmap files.

## Proposed Structure
- `docs/roadmap/README.md`
  - Entry point with links to roadmap files and a brief description of their roles.
- `docs/roadmap/phases.md`
  - All Phase sections (Phase 4–7 and future), including completed items and detailed notes.
- `docs/roadmap/discussion-snapshots.md`
  - Full historical “討論共識快照” blocks with dates and bullet details.

## `TODO.md` Content Rules (After Restructure)
- Keep the title and top-level context lines.
- For each Phase:
  - Keep a one-line summary of scope or status.
  - Keep any unchecked items that are active/near-term.
  - Replace detailed completed items and long descriptions with a link to `docs/roadmap/phases.md`.
- Move the entire “討論共識快照” section to `docs/roadmap/discussion-snapshots.md` and leave a link in `TODO.md`.

## Migration Steps
1. Create `docs/roadmap/README.md` with links and purpose.
2. Create `docs/roadmap/phases.md` and move all Phase sections (4–7) into it.
3. Create `docs/roadmap/discussion-snapshots.md` and move all discussion snapshots into it.
4. Update `TODO.md` to:
   - Keep high-level Phase headings and any active unchecked tasks.
   - Replace detailed completed sections with links to `docs/roadmap/phases.md`.
   - Replace the full snapshot section with a link to `docs/roadmap/discussion-snapshots.md`.

## Success Criteria
- `TODO.md` is under ~60 lines and readable in under 30 seconds.
- All moved content is preserved verbatim in `docs/roadmap/`.
- Links between `TODO.md` and `docs/roadmap/` are correct and stable.

## Risks and Mitigations
- Risk: Missing items during move.
  - Mitigation: Move content verbatim, then verify `TODO.md` contains links to every moved section.
- Risk: Confusion about where to add new roadmap items.
  - Mitigation: State clearly in `docs/roadmap/README.md` that long-term items belong in `docs/roadmap/phases.md`, while `TODO.md` should only contain near-term active tasks.
