from dao.model.task import Task
from dao.taskDAO import TaskDAO
from spider import common


def save_task(task: Task):
    result = {}
    not_repeat = True
    # oldTask = TaskDAO.queryOneByIdentifies(task.identifies)
    oldTask = TaskDAO.queryOneByIdentifiesAndValid(task.identifies, 1)
    if oldTask is None:
        TaskDAO.insert(task)
        not_repeat = True
    else:
        repeat_expire_time = oldTask.repeat_expire_time
        if repeat_expire_time is None or repeat_expire_time < 0:
            # 没有过期时间
            not_repeat = False
        else:
            if repeat_expire_time > common.get_current_time():
                # 任务重复时间还没过期
                not_repeat = False
            else:
                updated_task = Task(valid_status=0)
                TaskDAO.updatedById(oldTask.id, updated_task)
                TaskDAO.insert(task)
                not_repeat = True

    result["not_repeat"] = not_repeat
    return result
