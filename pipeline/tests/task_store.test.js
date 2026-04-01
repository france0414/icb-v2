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

  const baseTime = Date.now();
  fs.utimesSync(a, new Date(baseTime - 2000), new Date(baseTime - 2000));
  fs.utimesSync(b, new Date(baseTime - 1000), new Date(baseTime - 1000));

  const list = listTasksByUpdated(dir);
  assert.equal(list[0], b);
  assert.equal(list[1], a);
});

test("withTaskLock prevents concurrent processing", async () => {
  const dir = createTempDir();
  const filePath = path.join(dir, "20260327-120002-lock.json");
  writeTask(filePath, { stage: "collector", flow: ["collector"], status: "pending", require_approval: true, approved: false, logs: [] });

  let release;
  const holdLock = new Promise((resolve) => {
    release = resolve;
  });

  const firstPromise = withTaskLock(filePath, async () => {
    await holdLock;
    return "first";
  });

  await new Promise((resolve) => setImmediate(resolve));

  const second = await withTaskLock(filePath, async () => "second");
  assert.equal(second, null);

  release();
  const first = await firstPromise;
  assert.equal(first, "first");
});
