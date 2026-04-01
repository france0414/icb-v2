export const validateFlow = (task) => {
  if (!task || !Array.isArray(task.flow)) return false;
  return task.flow.includes(task.stage);
};

export const advanceStage = (task) => {
  if (!task || !Array.isArray(task.flow) || task.flow.length === 0) return task;
  const index = task.flow.indexOf(task.stage);
  if (index === -1) return task;
  const isLast = index === task.flow.length - 1;
  if (isLast) {
    return { ...task, status: "done", approved: false };
  }
  return { ...task, stage: task.flow[index + 1], approved: false };
};
