# Taipei Timezone Logging Design

Date: 2026-03-27

## Overview
Update controller logging so all timestamps are recorded in Taiwan time (Asia/Taipei). This affects task `logs` entries and the parse error log written to `logs/controller.log`.

## Goals
- All timestamps in `pipeline/controller.js` use Taiwan time.
- Timestamp format is ISO-like with explicit `+08:00` offset.
- Keep changes localized to the controller (no new dependencies).

## Non-Goals
- Changing timestamps in other files or modules.
- Adding external time libraries.

## Approach
Add a small helper in `pipeline/controller.js` that returns a Taiwan time string. Use it wherever timestamps are currently generated:
- `logs` entries for `invalid_flow` and `stage_advanced`
- `logs/controller.log` parse error entries

### Timestamp Format
Use `YYYY-MM-DDTHH:mm:ss+08:00` (ISO-like, local offset explicit). Example:
`2026-03-27T14:24:08+08:00`

## Components and Files
- Modify: `pipeline/controller.js`
- Modify: `pipeline/tests/controller.test.js` (if tests assert time format)

## Testing and Acceptance
- Logs in task JSON show Taiwan time with `+08:00`.
- `logs/controller.log` lines show Taiwan time with `+08:00`.
- Existing controller tests still pass; update tests only if they validate timestamp format.

## Future Considerations
- If other modules need timestamps, extract a shared utility later.
