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
