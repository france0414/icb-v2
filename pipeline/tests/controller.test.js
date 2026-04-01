import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { processTaskFile } from "../controller.js";

const createTempDir = () => fs.mkdtempSync(path.join(os.tmpdir(), "icb-controller-"));

test("processTaskFile logs parse errors without modifying file", async () => {
  const dir = createTempDir();
  const originalCwd = process.cwd();
  process.chdir(dir);
  try {
    const filePath = path.join(dir, "20260327-125959-task.json");
    const content = "{ invalid json";
    fs.writeFileSync(filePath, content);

    const result = await processTaskFile(filePath);
    assert.equal(result, "parse_error");
    assert.equal(fs.readFileSync(filePath, "utf8"), content);

    const logPath = path.join(dir, "logs", "controller.log");
    const logContents = fs.readFileSync(logPath, "utf8");
    const lines = logContents.trim().split("\n");
    const lastLine = lines[lines.length - 1];
    assert.ok(lastLine.includes(filePath));
    const parts = lastLine.split(" | ");
    assert.ok(parts.length >= 3);
    assert.ok(parts[2].trim().length > 0);
  } finally {
    process.chdir(originalCwd);
  }
});

test("processTaskFile logs Taipei offset timestamps", async () => {
  const dir = createTempDir();
  const originalCwd = process.cwd();
  process.chdir(dir);
  try {
    const badFilePath = path.join(dir, "20260327-131500-task.json");
    fs.writeFileSync(badFilePath, "{ invalid json");

    await processTaskFile(badFilePath);

    const logPath = path.join(dir, "logs", "controller.log");
    const logContents = fs.readFileSync(logPath, "utf8");
    const lines = logContents.trim().split("\n");
    const lastLine = lines[lines.length - 1];
    const timestamp = lastLine.split(" | ")[0];
    assert.ok(timestamp.endsWith("+08:00"));
  } finally {
    process.chdir(originalCwd);
  }

  const dir2 = createTempDir();
  const filePath = path.join(dir2, "20260327-131501-task.json");
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
  assert.equal(updated.logs.length, 1);
  assert.ok(updated.logs[0].time.endsWith("+08:00"));
});

test("processTaskFile stops when approval required", async () => {
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

  const resultPromise = processTaskFile(filePath);
  assert.ok(resultPromise instanceof Promise);
  const result = await resultPromise;
  assert.equal(result, "awaiting_approval");
});

test("processTaskFile advances when approved", async () => {
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

  const resultPromise = processTaskFile(filePath);
  assert.ok(resultPromise instanceof Promise);
  const result = await resultPromise;
  const updated = JSON.parse(fs.readFileSync(filePath, "utf8"));
  assert.equal(result, "advanced");
  assert.equal(updated.stage, "discuss");
});

test("processTaskFile advances when logs missing", async () => {
  const dir = createTempDir();
  const filePath = path.join(dir, "20260327-130002-task.json");
  const task = {
    stage: "collector",
    flow: ["collector", "discuss"],
    status: "pending",
    require_approval: false,
    approved: false
  };
  fs.writeFileSync(filePath, JSON.stringify(task));

  const result = await processTaskFile(filePath);
  const updated = JSON.parse(fs.readFileSync(filePath, "utf8"));
  assert.equal(result, "advanced");
  assert.equal(updated.stage, "discuss");
  assert.ok(Array.isArray(updated.logs));
  assert.equal(updated.logs.length, 1);
  assert.equal(updated.logs[0].action, "stage_advanced");
});
