# Task Automation Controller Design

Date: 2026-03-27

## Overview
Design a long-running task automation controller that watches task JSON files and advances them through a fixed workflow. Approval is granted via a simple CLI command (`ok`) that marks the latest pending task as approved, after which the controller continues the workflow.

## Goals
- Provide a single, reliable controller to monitor task changes and advance stages.
- Support a clear approval gate at every stage.
- Keep task history in a single source of truth (`logs` within the task JSON).
- Allow future expansion to multiple task domains (automation vs pages) with minimal changes.

## Non-Goals
- Building a UI for approvals or dashboards.
- Full multi-agent scheduling and load balancing.
- Automatic task generation from external sources.

## Task Structure
Each task is a JSON file stored in `/tasks/automation/` with a timestamped filename.

Filename:
`YYYYMMDD-HHMMSS-<slug>.json`

Required fields:
- `stage`: current stage, one of `collector`, `discuss`, `assign`, `executor`, `reviewer`, `master`
- `flow`: array of stage names in order
- `status`: `pending` or `done`
- `require_approval`: boolean
- `approved`: boolean
- `logs`: array of events

Log event shape:
```json
{
  "time": "2026-03-27T14:32:10Z",
  "actor": "controller",
  "action": "stage_advanced",
  "note": "Moved from discuss to assign"
}
```

Optional (future):
- `analysis`: object containing website block analysis and ICB conversion intermediates.

## Components
- `pipeline/controller.js`: long-running process that watches task folders, loads task JSON, applies flow rules, and writes updates and logs.
- `pipeline/task_store.js`: read/write utilities, sorting by updated time, and a lightweight in-process lock to prevent duplicate processing.
- `pipeline/flow_engine.js`: computes next stage based on `flow` and `stage`, applies approval gate rules.
- `pipeline/cli.js`: accepts `ok` and marks the latest pending task as `approved: true`.

## Data Flow
1. Controller starts and watches configured `tasksSources` (default: `/tasks/automation/`).
2. On file change/addition:
   - Read JSON.
   - Validate minimal shape.
   - If `require_approval` is true and `approved` is false, stop.
   - If `approved` is true, advance to the next stage and reset `approved` to false.
   - If the task reaches the final stage and is completed, set `status` to `done`.
   - Append a log entry for each action or error.
3. CLI receives `ok` and marks the latest pending task as `approved: true`.
4. Controller observes that change and advances the task.

## Error Handling
- JSON parse error: write an error log entry, skip advancement.
- `flow` missing or does not include current `stage`: log and stop.
- Duplicate processing attempts: skip if the task is currently locked in-process.

## Configuration
- `tasksSources`: array of task directories. Initial value: `[/tasks/automation/]`.
- Future addition: `[/tasks/pages/]` without changing core logic.

## CLI Behavior
- Command: `node pipeline/cli.js ok`
- Default: applies to the latest pending task awaiting approval.

## Testing and Acceptance
- New task file generates a log entry.
- `require_approval=true` prevents automatic advancement.
- `ok` sets `approved=true` for the latest pending task.
- Controller advances to the next stage after approval.
- Final stage sets `status=done` and logs completion.
- JSON errors are logged without advancement.

## Future Extensions
- Add `/tasks/pages/` to `tasksSources` with an independent flow.
- Allow explicit task selection for approval by ID.
- Expand `analysis` to hold website block analysis and ICB conversion results.
