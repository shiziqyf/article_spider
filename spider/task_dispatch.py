import time

from dao.model.task import Task
from dao.taskDAO import TaskDAO


def start():
    # 获取最早的优先级最高的任务
    task = TaskDAO.queryEarliestTask()
    print("task = ", task)
    if task is None:
        return
    execute_task(task)


def execute_task(task: Task):
    model_name = task.module_name
    func_name = task.execute_func_name
    params = task.params
    dirt_param = eval(params)
    print(type(params))
    model = __import__(model_name, fromlist=True)
    f = getattr(model, func_name, None)
    if f is not None:
        if dirt_param is None or len(dirt_param) == 0:
            f()
        else:
            f(**dirt_param)
    update_task = Task(status=1)
    TaskDAO.updatedById(task_id=task.id, task=update_task)


if __name__ == '__main__':
    while True:
        time.sleep(1)
        start()
    # test = eval("")
    # print(test)
