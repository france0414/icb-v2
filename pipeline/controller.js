import fs from "node:fs";
import path from "node:path";
import { readTask, writeTask, withTaskLock } from "./task_store.js";
import { validateFlow, advanceStage } from "./flow_engine.js";

const taipeiFormatter = new Intl.DateTimeFormat("en-CA", {
  timeZone: "Asia/Taipei",
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
  hour12: false,
  hourCycle: "h23"
});

const formatTaipeiTimestamp = (date = new Date()) => {
  const parts = taipeiFormatter.formatToParts(date);
  const lookup = Object.fromEntries(parts.map((part) => [part.type, part.value]));
  return `${lookup.year}-${lookup.month}-${lookup.day}T${lookup.hour}:${lookup.minute}:${lookup.second}+08:00`;
};

const appendLog = (task, entry) => {
  const logs = Array.isArray(task.logs) ? task.logs : [];
  return { ...task, logs: [...logs, entry] };
};

export const processTaskFile = async (filePath) => {
  return await withTaskLock(filePath, async () => {
    let task;
    try {
      task = readTask(filePath);
    } catch (error) {
      const logDir = path.resolve("logs");
      fs.mkdirSync(logDir, { recursive: true });
      const logPath = path.join(logDir, "controller.log");
      const message = error instanceof Error ? error.message : String(error);
      const entry = `${formatTaipeiTimestamp()} | ${filePath} | ${message}\n`;
      fs.appendFileSync(logPath, entry, "utf8");
      return "parse_error";
    }

    if (!validateFlow(task)) {
      const logged = appendLog(task, {
        time: formatTaipeiTimestamp(),
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
      time: formatTaipeiTimestamp(),
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
