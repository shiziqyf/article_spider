from dao.model.task import Task
from dao.taskDAO import TaskDAO


def save_task(task: Task) -> bool:
    oldTask = TaskDAO.queryOneByIdentifies(task.identifies)
    if oldTask is None:
        TaskDAO.insert(task)
        return True
    else:
        repeat_expire_time = oldTask.repeat_expire_time
        if repeat_expire_time is None or repeat_expire_time < 0:
            # 没有过期时间
            return False
        else:
            TaskDAO.updatedById(oldTask.id, task)
            return True
