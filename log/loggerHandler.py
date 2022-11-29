import logging
import os.path


class LoggerHandler:

    def __init__(self, file_name, console=True):
        self.log = logging.getLogger(file_name)
        formatter = logging.Formatter("%(asctime)s %(levelname)s - %(message)s",'%Y-%m-%d %H:%M:%S')

        # 文件
        if file_name:
            fh = logging.FileHandler(filename=file_name)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.log.addHandler(fh)
        if console:
            # 控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            self.log.addHandler(ch)
        self.log.setLevel(logging.DEBUG)

