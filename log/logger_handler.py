import logging

import logging.handlers

import global_var
from config import settings


class LoggerHandler:

    def __init__(self, file_name, console=True):
        self.log = logging.getLogger(file_name)
        log_format = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter("%(asctime)s %(levelname)s - %(message)s", log_format)

        # 文件
        if file_name:
            # fh = logging.FileHandler(filename=file_name)
            fh = logging.handlers.TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=7)
            fh.suffix = "%Y-%m-%d.log"
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            self.log.addHandler(fh)
        # 控制台
        if console:
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            self.log.addHandler(ch)
        self.log.setLevel(logging.INFO)

    @staticmethod
    def init_log():
        print("start init log......")
        biz_log = LoggerHandler(settings.log.biz_file).log
        debug_log = LoggerHandler(settings.log.debug_file).log
        global_var.set_value('biz_log', biz_log)
        global_var.set_value('debug_log', debug_log)
