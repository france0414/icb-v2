import test from "node:test";
import assert from "node:assert/strict";
import { advanceStage, validateFlow } from "../flow_engine.js";

test("validateFlow returns false when stage missing", () => {
  const ok = validateFlow({ stage: "executor", flow: ["collector", "discuss" ] });
  assert.equal(ok, false);
});

test("validateFlow returns false for empty flow", () => {
  const ok = validateFlow({ stage: "collector", flow: [] });
  assert.equal(ok, false);
});

test("validateFlow returns false for non-array flow", () => {
  const ok = validateFlow({ stage: "collector", flow: "collector" });
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

test("advanceStage does not advance when stage missing", () => {
  const task = { stage: "executor", flow: ["collector", "discuss"], approved: true, status: "pending" };
  const next = advanceStage(task);
  assert.equal(next.stage, task.stage);
  assert.equal(next.status, task.status);
  assert.equal(next.approved, task.approved);
});

test("advanceStage does not advance when flow empty", () => {
  const task = { stage: "collector", flow: [], approved: true, status: "pending" };
  const next = advanceStage(task);
  assert.equal(next.stage, task.stage);
  assert.equal(next.status, task.status);
  assert.equal(next.approved, task.approved);
});

test("advanceStage does not advance when flow is not an array", () => {
  const task = { stage: "collector", flow: "collector", approved: true, status: "pending" };
  const next = advanceStage(task);
  assert.equal(next.stage, task.stage);
  assert.equal(next.status, task.status);
  assert.equal(next.approved, task.approved);
});
