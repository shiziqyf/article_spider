from dao.model.task import Task
from dao.taskDAO import TaskDAO


def start():
    # 获取最早的优先级最高的任务
    task = TaskDAO.queryEarliestTask()
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


if __name__ == '__main__':
    start()
    # test = eval("")
    # print(test)
