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

export const findLatestPendingTask = (dirPath) => {
  const list = listTasksByUpdated(dirPath);
  for (const filePath of list) {
    let task;
    try {
      task = readTask(filePath);
    } catch (error) {
      continue;
    }
    if (
      task.status === "pending" &&
      task.require_approval === true &&
      task.approved !== true
    ) {
      return filePath;
    }
  }
  return null;
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
