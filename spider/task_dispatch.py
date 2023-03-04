import time
import traceback
from dao.model.task import Task
from dao.taskDAO import TaskDAO
import threading


def start_one():
    # 获取最早的优先级最高的任务
    task = TaskDAO.queryEarliestTask()
    print("task = ", task)
    if task is None:
        return
    execute_task(task)


def execute_task(task: Task):
    # 任务最多执行3次，超过3次还是失败，则任务优先级降低
    count = 0
    while count < 3:
        count = count + 1
        try:
            model_name = task.module_name
            func_name = task.execute_func_name
            params = task.params
            dirt_param = eval(params)
            model = __import__(model_name, fromlist=True)
            f = getattr(model, func_name, None)
            if f is not None:
                if dirt_param is None or len(dirt_param) == 0:
                    f()
                else:
                    f(**dirt_param)
            update_task = Task(status=1)
            TaskDAO.updatedById(task_id=task.id, task=update_task)
            return
        except Exception as e:
            print(traceback.format_exc())
            time.sleep(1)
    print("id: ", task.id, " 任务执行失败，优先级降低")
    reduce_priority = task.priority - 1
    update_task = Task(priority=reduce_priority)
    TaskDAO.updatedById(task_id=task.id, task=update_task)


def start():
    while True:
        time.sleep(1)
        start_one()


def start_with_new_thread():
    thread = threading.Thread(target=start)
    thread.start()
