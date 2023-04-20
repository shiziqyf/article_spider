import time
import traceback

from apscheduler.schedulers.background import BackgroundScheduler

import global_var
import thread_manage.thread_manage
from dao.model.task import Task
from dao.taskDAO import TaskDAO
import threading

lock = threading.Lock()


def start_task(task_type):
    # 获取最早的优先级最高的任务
    # task = TaskDAO.queryEarliestTaskByType(task_type)
    task = get_lock_task(task_type)
    if task is None:
        return
    execute_task(task)


def get_lock_task(task_type):
    task = None
    with lock:
        task = TaskDAO.queryEarliestTaskByType(task_type)
        if task is None:
            return
        update_task = Task(status=2)
        TaskDAO.updatedById(task_id=task.id, task=update_task)
    return task


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
                    f(task_id=task.id)
                else:
                    f(task_id=task.id, execute_params=dict_param)
            update_task = Task(status=1)
            TaskDAO.updatedById(task_id=task.id, task=update_task)
            return
        except Exception:
            biz_log.error('task execute fail, id=%s, %s', task.id, traceback.format_exc())

    biz_log.error('task execute fail too many, priority will reduce, id=%s', task.id)
    reduce_priority = task.priority - 1
    update_task = Task(priority=reduce_priority, status=0)
    TaskDAO.updatedById(task_id=task.id, task=update_task)


def start_article():
    biz_log = global_var.get_value('biz_log')
    while True:
        try:
            time.sleep(1)
            start_task('ARTICLE')
        except Exception:
            biz_log.error('start article task fail, err=%s', traceback.format_exc())


def start_img():
    biz_log = global_var.get_value('biz_log')
    while True:
        try:
            time.sleep(0.5)
            start_task('IMG')
        except Exception:
            biz_log.error('start img task fail, err=%s', traceback.format_exc())
    # biz_log = global_var.get_value('biz_log')
    # try:
    #     start_task('IMG')
    # except Exception:
    #     biz_log.error('start img task fail, err=%s', traceback.format_exc())


def start_article_with_new_thread():
    biz_log = global_var.get_value('biz_log')
    biz_log.info('start_article_with_new_thread......')
    thread = threading.Thread(target=start_article)
    thread.daemon = True
    thread.start()
    thread_ident = thread.ident
    thread_manage.thread_manage.add_need_manage_thread(thread_ident, "article_spider")


def start_img_with_new_thread(thread_num):
    biz_log = global_var.get_value('biz_log')
    for i in range(thread_num):
        biz_log.info('start_img_with_new_thread......')
        thread = threading.Thread(target=start_img)
        thread.daemon = True
        thread.start()
        thread_ident = thread.ident
        thread_manage.thread_manage.add_need_manage_thread(thread_ident, "img_spider")

    # threading.
    # schedule = BackgroundScheduler()
    # schedule.add_job(start_img, trigger='interval', seconds=1, max_instances=1)
    # schedule.start()

    # thread = threading.Thread(target=start_img)
    # thread.daemon = True
    # thread.start()
