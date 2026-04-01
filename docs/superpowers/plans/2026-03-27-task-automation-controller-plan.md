# Task Automation Controller Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a long-running controller that watches task JSON files, advances workflow stages with approval gates, and provides a CLI `ok` approval command.

**Architecture:** Use small, focused Node.js modules: `task_store` for IO and locking, `flow_engine` for stage logic, `controller` for watching and orchestration, and `cli` for approvals. Keep task state in JSON files and store all actions in `logs`.

**Tech Stack:** Node.js (built-in `fs`, `path`, `os`, `events`), `node:test` for tests.

---

## File Structure

- Create: `pipeline/task_store.js` (task IO, sorting, locking)
- Create: `pipeline/flow_engine.js` (advance logic and validation)
- Create: `pipeline/controller.js` (watcher + orchestration)
- Create: `pipeline/cli.js` (approval command)
- Create: `pipeline/tests/task_store.test.js`
- Create: `pipeline/tests/flow_engine.test.js`
- Create: `pipeline/tests/cli.test.js`
- Create: `pipeline/tests/controller.test.js`
- Create: `tasks/automation/.gitkeep`

---

### Task 1: Task Store (IO, sorting, locking)

**Files:**
- Create: `pipeline/task_store.js`
- Create: `pipeline/tests/task_store.test.js`

- [ ] **Step 1: Write failing tests for task_store**

```js
import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { readTask, writeTask, listTasksByUpdated, withTaskLock } from "../task_store.js";

const createTempDir = () => fs.mkdtempSync(path.join(os.tmpdir(), "icb-task-store-"));

test("writeTask then readTask round-trips JSON", () => {
  const dir = createTempDir();
  const filePath = path.join(dir, "20260327-120000-sample.json");
  const task = { stage: "collector", flow: ["collector"], status: "pending", require_approval: true, approved: false, logs: [] };

  writeTask(filePath, task);
  const read = readTask(filePath);

  assert.equal(read.stage, "collector");
  assert.equal(read.status, "pending");
});

test("listTasksByUpdated sorts by mtime desc", () => {
  const dir = createTempDir();
  const a = path.join(dir, "20260327-120000-a.json");
  const b = path.join(dir, "20260327-120001-b.json");

  writeTask(a, { stage: "collector", flow: ["collector"], status: "pending", require_approval: true, approved: false, logs: [] });
  writeTask(b, { stage: "collector", flow: ["collector"], status: "pending", require_approval: true, approved: false, logs: [] });

  const list = listTasksByUpdated(dir);
  assert.equal(list[0], b);
  assert.equal(list[1], a);
});

test("withTaskLock prevents concurrent processing", async () => {
  const dir = createTempDir();
  const filePath = path.join(dir, "20260327-120002-lock.json");
  writeTask(filePath, { stage: "collector", flow: ["collector"], status: "pending", require_approval: true, approved: false, logs: [] });

  const first = await withTaskLock(filePath, async () => "first");
  assert.equal(first, "first");

  const second = await withTaskLock(filePath, async () => "second");
  assert.equal(second, null);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test pipeline/tests/task_store.test.js`
Expected: FAIL with module not found or missing exports for `task_store.js`.

- [ ] **Step 3: Implement task_store**

```js
import fs from "node:fs";
import path from "node:path";

const locks = new Set();

export const readTask = (filePath) => {
  const content = fs.readFileSync(filePath, "utf8");
  return JSON.parse(content);
};

export const writeTask = (filePath, task) => {
  const json = JSON.stringify(task, null, 2);
  fs.writeFileSync(filePath, json, "utf8");
};

export const listTasksByUpdated = (dirPath) => {
  if (!fs.existsSync(dirPath)) return [];
  const entries = fs.readdirSync(dirPath).map((name) => path.join(dirPath, name));
  return entries
    .filter((filePath) => filePath.endsWith(".json"))
    .sort((a, b) => fs.statSync(b).mtimeMs - fs.statSync(a).mtimeMs);
};

export const withTaskLock = async (filePath, fn) => {
  if (locks.has(filePath)) return null;
  locks.add(filePath);
  try {
    return await fn();
  } finally {
    locks.delete(filePath);
  }
};
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test pipeline/tests/task_store.test.js`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add pipeline/task_store.js pipeline/tests/task_store.test.js
git commit -m "feat: add task store io and locking"
```

---

### Task 2: Flow Engine (stage validation and advance)

**Files:**
- Create: `pipeline/flow_engine.js`
- Create: `pipeline/tests/flow_engine.test.js`

- [ ] **Step 1: Write failing tests for flow_engine**

```js
import test from "node:test";
import assert from "node:assert/strict";
import { advanceStage, validateFlow } from "../flow_engine.js";

test("validateFlow returns false when stage missing", () => {
  const ok = validateFlow({ stage: "executor", flow: ["collector", "discuss" ] });
  assert.equal(ok, false);
});

test("advanceStage moves to next stage and resets approved", () => {
  const task = { stage: "collector", flow: ["collector", "discuss"], approved: true };
  const next = advanceStage(task);
  assert.equal(next.stage, "discuss");
  assert.equal(next.approved, false);
});

test("advanceStage marks status done at last stage", () => {
  const task = { stage: "master", flow: ["collector", "master"], approved: true, status: "pending" };
  const next = advanceStage(task);
  assert.equal(next.status, "done");
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test pipeline/tests/flow_engine.test.js`
Expected: FAIL with module not found or missing exports for `flow_engine.js`.

- [ ] **Step 3: Implement flow_engine**

```js
export const validateFlow = (task) => {
  if (!task || !Array.isArray(task.flow)) return false;
  return task.flow.includes(task.stage);
};

export const advanceStage = (task) => {
  const index = task.flow.indexOf(task.stage);
  const isLast = index === task.flow.length - 1;
  if (isLast) {
    return { ...task, status: "done", approved: false };
  }
  return { ...task, stage: task.flow[index + 1], approved: false };
};
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test pipeline/tests/flow_engine.test.js`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add pipeline/flow_engine.js pipeline/tests/flow_engine.test.js
git commit -m "feat: add flow engine for stage advancement"
```

---

### Task 3: Controller (watch tasks and apply flow)

**Files:**
- Create: `pipeline/controller.js`
- Create: `pipeline/tests/controller.test.js`

- [ ] **Step 1: Write failing tests for controller**

```js
import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { processTaskFile } from "../controller.js";

const createTempDir = () => fs.mkdtempSync(path.join(os.tmpdir(), "icb-controller-"));

test("processTaskFile stops when approval required", () => {
  const dir = createTempDir();
  const filePath = path.join(dir, "20260327-130000-task.json");
  const task = {
    stage: "collector",
    flow: ["collector", "discuss"],
    status: "pending",
    require_approval: true,
    approved: false,
    logs: []
  };
  fs.writeFileSync(filePath, JSON.stringify(task));

  const result = processTaskFile(filePath);
  assert.equal(result, "awaiting_approval");
});

test("processTaskFile advances when approved", () => {
  const dir = createTempDir();
  const filePath = path.join(dir, "20260327-130001-task.json");
  const task = {
    stage: "collector",
    flow: ["collector", "discuss"],
    status: "pending",
    require_approval: true,
    approved: true,
    logs: []
  };
  fs.writeFileSync(filePath, JSON.stringify(task));

  const result = processTaskFile(filePath);
  const updated = JSON.parse(fs.readFileSync(filePath, "utf8"));
  assert.equal(result, "advanced");
  assert.equal(updated.stage, "discuss");
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test pipeline/tests/controller.test.js`
Expected: FAIL with module not found or missing exports for `controller.js`.

- [ ] **Step 3: Implement controller core logic**

```js
import fs from "node:fs";
import path from "node:path";
import { readTask, writeTask, withTaskLock } from "./task_store.js";
import { validateFlow, advanceStage } from "./flow_engine.js";

const appendLog = (task, entry) => ({ ...task, logs: [...task.logs, entry] });

export const processTaskFile = (filePath) => {
  return withTaskLock(filePath, () => {
    let task;
    try {
      task = readTask(filePath);
    } catch (error) {
      return "parse_error";
    }

    if (!validateFlow(task)) {
      const logged = appendLog(task, {
        time: new Date().toISOString(),
        actor: "controller",
        action: "invalid_flow",
        note: "Current stage not in flow"
      });
      writeTask(filePath, logged);
      return "invalid_flow";
    }

    if (task.require_approval && !task.approved) {
      return "awaiting_approval";
    }

    const next = advanceStage(task);
    const logged = appendLog(next, {
      time: new Date().toISOString(),
      actor: "controller",
      action: "stage_advanced",
      note: "Advanced task stage"
    });
    writeTask(filePath, logged);
    return "advanced";
  });
};

export const startController = (tasksSources) => {
  tasksSources.forEach((dirPath) => {
    if (!fs.existsSync(dirPath)) return;
    fs.watch(dirPath, (eventType, filename) => {
      if (!filename || !filename.endsWith(".json")) return;
      const filePath = path.join(dirPath, filename);
      if (fs.existsSync(filePath)) processTaskFile(filePath);
    });
  });
};

if (import.meta.url === `file://${process.argv[1]}`) {
  const root = process.cwd();
  const tasksSources = [path.join(root, "tasks", "automation")];
  startController(tasksSources);
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test pipeline/tests/controller.test.js`
Expected: PASS (2 tests).

- [ ] **Step 5: Commit**

```bash
git add pipeline/controller.js pipeline/tests/controller.test.js
git commit -m "feat: add controller to process task files"
```

---

### Task 4: CLI approval command

**Files:**
- Create: `pipeline/cli.js`
- Create: `pipeline/tests/cli.test.js`
- Modify: `pipeline/task_store.js` (export helper to find latest pending task)

- [ ] **Step 1: Write failing tests for CLI approval**

```js
import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { approveLatestTask } from "../cli.js";

const createTempDir = () => fs.mkdtempSync(path.join(os.tmpdir(), "icb-cli-"));

test("approveLatestTask marks latest pending task approved", () => {
  const dir = createTempDir();
  const a = path.join(dir, "20260327-140000-a.json");
  const b = path.join(dir, "20260327-140001-b.json");
  fs.writeFileSync(a, JSON.stringify({ stage: "collector", flow: ["collector"], status: "pending", require_approval: true, approved: false, logs: [] }));
  fs.writeFileSync(b, JSON.stringify({ stage: "collector", flow: ["collector"], status: "pending", require_approval: true, approved: false, logs: [] }));

  approveLatestTask(dir);
  const updated = JSON.parse(fs.readFileSync(b, "utf8"));
  assert.equal(updated.approved, true);
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test pipeline/tests/cli.test.js`
Expected: FAIL with module not found or missing exports for `cli.js`.

- [ ] **Step 3: Implement helper in task_store**

```js
export const findLatestPendingTask = (dirPath) => {
  const list = listTasksByUpdated(dirPath);
  return list.find((filePath) => {
    const task = readTask(filePath);
    return task.status === "pending" && task.require_approval === true && task.approved === false;
  }) || null;
};
```

- [ ] **Step 4: Implement CLI**

```js
import path from "node:path";
import { readTask, writeTask, findLatestPendingTask } from "./task_store.js";

export const approveLatestTask = (dirPath) => {
  const latest = findLatestPendingTask(dirPath);
  if (!latest) return "no_pending";
  const task = readTask(latest);
  task.approved = true;
  writeTask(latest, task);
  return "approved";
};

if (import.meta.url === `file://${process.argv[1]}`) {
  const root = process.cwd();
  const dirPath = path.join(root, "tasks", "automation");
  const cmd = process.argv[2];
  if (cmd === "ok") approveLatestTask(dirPath);
}
```

- [ ] **Step 5: Run test to verify it passes**

Run: `node --test pipeline/tests/cli.test.js`
Expected: PASS (1 test).

- [ ] **Step 6: Commit**

```bash
git add pipeline/task_store.js pipeline/cli.js pipeline/tests/cli.test.js
git commit -m "feat: add cli approval command"
```

---

### Task 5: Tasks directory and smoke test

**Files:**
- Create: `tasks/automation/.gitkeep`

- [ ] **Step 1: Create tasks directory marker**

Create file `tasks/automation/.gitkeep` with empty content.

- [ ] **Step 2: Run full test suite**

Run: `node --test pipeline/tests/task_store.test.js pipeline/tests/flow_engine.test.js pipeline/tests/controller.test.js pipeline/tests/cli.test.js`
Expected: PASS (all tests).

- [ ] **Step 3: Commit**

```bash
git add tasks/automation/.gitkeep
git commit -m "chore: add tasks automation directory"
```

---

## Self-Review Checklist

- Spec coverage: tasks cover controller, flow engine, store, CLI, approval gate, logs, and error handling.
- Placeholder scan: no TODO/TBD or vague steps.
- Type consistency: field names match spec (`stage`, `flow`, `status`, `require_approval`, `approved`, `logs`).
