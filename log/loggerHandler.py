import logging


class LoggerHandler:

    def __init__(self, file_name, console=True):
        self.log = logging.getLogger(file_name)
        log_format = '%Y-%m-%d %H:%M:%S'
        formatter = logging.Formatter("%(asctime)s %(levelname)s - %(message)s", log_format)

        # 文件
        if file_name:
            fh = logging.FileHandler(filename=file_name)
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