import os
import sys
import time

from apscheduler.schedulers.background import BackgroundScheduler

import global_var
from app_service import article_app_service
from dao.mysqlConn import MysqlConnUtil
from log.logger_handler import LoggerHandler
from spider import task_dispatch, juejin
from spider.server import oss_service
from thread_manage import thread_manage


def init_config(args):
    config_file_name = 'dev.toml'
    is_first = False
    if len(args) >= 2 and args[1] is not None:
        config_file_name = str(args[1]) + ".toml"
    if len(args) >= 3 and args[2] is not None:
        is_first = True if args[2].lower() == 'true' else False
    global_var.set_value('is_first', is_first)
    os.environ["INCLUDES_FOR_DYNACONF"] = "['{}']".format(config_file_name)


# 初始化必要资源
def init_resource():
    # init config
    init_config(sys.argv)
    # init log module
    LoggerHandler.init_log()
    # init mysql conn pool
    MysqlConnUtil.init_pool()

    oss_service.init()


def start_schedule():
    schedule = BackgroundScheduler()
    juejin.juejin_spider_start()
    schedule.add_job(juejin.juejin_spider_start, trigger='interval', seconds=300)
    # schedule.add_job(thread_manage.check_thread, trigger='interval', seconds=300)
    schedule.start()


if __name__ == '__main__':
    init_resource()

    biz_log = global_var.get_value('biz_log')

    # 任务调度启动
    task_dispatch.start_article_with_new_thread()
    task_dispatch.start_img_with_new_thread(4)
    article_app_service.start_verify_img_deal_new_thread()
    start_schedule()
    while True:
        biz_log.info(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1000)
