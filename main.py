import os
import sys
import time

from apscheduler.schedulers.background import BackgroundScheduler

import global_var
from log.logger_handler import LoggerHandler
from spider import task_dispatch, juejin


def init_config(args):
    config_file_name = 'dev.toml'
    if len(args) >= 2 and args[1] is not None:
        config_file_name = str(args[1]) + ".toml"

    os.environ["INCLUDES_FOR_DYNACONF"] = "['{}']".format(config_file_name)


def test_job():
    print("test_job")


if __name__ == '__main__':
    # init config
    init_config(sys.argv)
    # init log module
    LoggerHandler.init_log()

    biz_log = global_var.get_value('biz_log')

    # 任务调度启动
    task_dispatch.start_with_new_thread()
    schedule = BackgroundScheduler()
    juejin.juejin_spider_start()
    schedule.add_job(juejin.juejin_spider_start, trigger='interval', seconds=300)
    schedule.start()
    while True:
        biz_log.info(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1000)
