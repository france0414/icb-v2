import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { approveLatestTask } from "../cli.js";

const createTempDir = () => fs.mkdtempSync(path.join(os.tmpdir(), "icb-cli-"));
const writeTaskFile = (filePath, task) => {
  fs.writeFileSync(filePath, JSON.stringify(task));
};

test("approveLatestTask marks latest pending task approved", () => {
  const dir = createTempDir();
  const a = path.join(dir, "20260327-140000-a.json");
  const b = path.join(dir, "20260327-140001-b.json");
  const olderTime = new Date("2026-03-27T14:00:00Z");
  const newerTime = new Date("2026-03-27T14:00:01Z");
  writeTaskFile(a, {
    stage: "collector",
    flow: ["collector"],
    status: "pending",
    require_approval: true,
    approved: false,
    logs: []
  });
  fs.utimesSync(a, olderTime, olderTime);
  writeTaskFile(b, {
    stage: "collector",
    flow: ["collector"],
    status: "pending",
    require_approval: true,
    approved: false,
    logs: []
  });
  fs.utimesSync(b, newerTime, newerTime);

  approveLatestTask(dir);
  const updated = JSON.parse(fs.readFileSync(b, "utf8"));
  const older = JSON.parse(fs.readFileSync(a, "utf8"));
  assert.equal(updated.approved, true);
  assert.equal(older.approved, false);
});

test("approveLatestTask treats missing approved as false", () => {
  const dir = createTempDir();
  const a = path.join(dir, "20260327-150000-a.json");
  const b = path.join(dir, "20260327-150001-b.json");
  const olderTime = new Date("2026-03-27T15:00:00Z");
  const newerTime = new Date("2026-03-27T15:00:01Z");
  writeTaskFile(a, {
    stage: "collector",
    flow: ["collector"],
    status: "pending",
    require_approval: true,
    approved: false,
    logs: []
  });
  fs.utimesSync(a, olderTime, olderTime);
  writeTaskFile(b, {
    stage: "collector",
    flow: ["collector"],
    status: "pending",
    require_approval: true,
    logs: []
  });
  fs.utimesSync(b, newerTime, newerTime);

  approveLatestTask(dir);
  const updated = JSON.parse(fs.readFileSync(b, "utf8"));
  const older = JSON.parse(fs.readFileSync(a, "utf8"));
  assert.equal(updated.approved, true);
  assert.equal(older.approved, false);
});

test("approveLatestTask skips invalid JSON files", () => {
  const dir = createTempDir();
  const bad = path.join(dir, "20260327-160000-bad.json");
  const good = path.join(dir, "20260327-155959-good.json");
  const newerTime = new Date("2026-03-27T16:00:00Z");
  const olderTime = new Date("2026-03-27T15:59:59Z");
  fs.writeFileSync(bad, "{not-json}");
  fs.utimesSync(bad, newerTime, newerTime);
  writeTaskFile(good, {
    stage: "collector",
    flow: ["collector"],
    status: "pending",
    require_approval: true,
    approved: false,
    logs: []
  });
  fs.utimesSync(good, olderTime, olderTime);

  approveLatestTask(dir);
  const updated = JSON.parse(fs.readFileSync(good, "utf8"));
  assert.equal(updated.approved, true);
});
