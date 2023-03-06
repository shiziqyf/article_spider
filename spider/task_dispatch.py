import time
import traceback

import global_var
from dao.model.task import Task
from dao.taskDAO import TaskDAO
import threading


def start_one():
    # 获取最早的优先级最高的任务
    task = TaskDAO.queryEarliestTask()
    if task is None:
        return
    execute_task(task)


def execute_task(task: Task):
    biz_log = global_var.get_value('biz_log')
    # 任务最多执行3次，超过3次还是失败，则任务优先级降低
    count = 0
    while count < 3:
        count = count + 1
        try:
            model_name = task.module_name
            func_name = task.execute_func_name
            params = task.params
            dict_param = eval(params)
            model = __import__(model_name, fromlist=True)
            f = getattr(model, func_name, None)
            if f is not None:
                if dict_param is None or len(dict_param) == 0:
                    f()
                else:
                    f(execute_params=dict_param)
            update_task = Task(status=1)
            TaskDAO.updatedById(task_id=task.id, task=update_task)
            return
        except Exception:
            biz_log.error('task execute fail, id=%s, %s', task.id, traceback.format_exc())

    biz_log.error('task execute fail too many, priority will reduce, id=%s', task.id)
    reduce_priority = task.priority - 1
    update_task = Task(priority=reduce_priority)
    TaskDAO.updatedById(task_id=task.id, task=update_task)


def start():
    while True:
        time.sleep(1)
        start_one()


def start_with_new_thread():
    thread = threading.Thread(target=start)
    thread.daemon = True
    thread.start()
