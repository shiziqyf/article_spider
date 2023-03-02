from dao.model.task import Task
from dao.taskDAO import TaskDAO


def saveTask(task: Task) -> bool:
    oldTask = TaskDAO.queryOneByIdentifies(task.identifies)
    if oldTask is None:
        TaskDAO.insert(task)
    else:
        expire_time = oldTask.expire_time
        if expire_time is None or expire_time < 0:
            # 没有过期时间
            return False
        # else:

