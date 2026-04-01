# Taipei Timezone Logging Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ensure all controller-generated timestamps use Taiwan time with an explicit +08:00 offset.

**Architecture:** Add a local timestamp formatter in `pipeline/controller.js` and replace all `new Date().toISOString()` usages with it for task logs and parse-error logs. No external dependencies.

**Tech Stack:** Node.js standard library (`Intl.DateTimeFormat`).

---

## File Structure

- Modify: `pipeline/controller.js`
- Modify: `pipeline/tests/controller.test.js`

---

### Task 1: Add Taipei timestamp formatter and update logs

**Files:**
- Modify: `pipeline/controller.js`
- Modify: `pipeline/tests/controller.test.js`

- [ ] **Step 1: Write failing test for Taiwan time format**

Add a test to `pipeline/tests/controller.test.js` that ensures log timestamps include `+08:00`:

```js
test("processTaskFile writes +08:00 timezone in logs", async () => {
  const dir = createTempDir();
  const filePath = path.join(dir, "20260327-130003-task.json");
  const task = {
    stage: "collector",
    flow: ["collector", "discuss"],
    status: "pending",
    require_approval: false,
    approved: false,
    logs: []
  };
  fs.writeFileSync(filePath, JSON.stringify(task));

  await processTaskFile(filePath);
  const updated = JSON.parse(fs.readFileSync(filePath, "utf8"));
  assert.ok(updated.logs[0].time.endsWith("+08:00"));
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `node --test pipeline/tests/controller.test.js`
Expected: FAIL with assertion about `+08:00`.

- [ ] **Step 3: Implement formatter in controller**

Update `pipeline/controller.js` by adding a formatter and replacing timestamps:

```js
const formatTaipeiTimestamp = () => {
  const formatter = new Intl.DateTimeFormat("sv-SE", {
    timeZone: "Asia/Taipei",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
    hour12: false
  });
  const parts = formatter.formatToParts(new Date());
  const pick = (type) => parts.find((part) => part.type === type)?.value || "";
  return `${pick("year")}-${pick("month")}-${pick("day")}T${pick("hour")}:${pick("minute")}:${pick("second")}+08:00`;
};
```

Replace:
- `new Date().toISOString()` in task logs with `formatTaipeiTimestamp()`
- `new Date().toISOString()` in parse-error log entry with `formatTaipeiTimestamp()`

- [ ] **Step 4: Run test to verify it passes**

Run: `node --test pipeline/tests/controller.test.js`
Expected: PASS (all controller tests).

- [ ] **Step 5: Commit**

```bash
git add pipeline/controller.js pipeline/tests/controller.test.js
git commit -m "feat: log taipei timezone timestamps"
```

---

## Self-Review Checklist

- Spec coverage: all controller timestamps now use Taiwan time with `+08:00`.
- Placeholder scan: no TODO/TBD.
- Type consistency: log fields still `time/actor/action/note`.
