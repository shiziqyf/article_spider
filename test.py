# import logging
#
# from log.logger_handler import LoggerHandler
# # import reflact_test.show1
# import time
# import hashlib
#
# import main
#
# # if __name__ == '__main__':
# #     # log = LoggerHandler("test.log").log
# #     # log2 = LoggerHandler("test2.log", True).log
# #     # # log.debug("dddds22231233")Î
# #     # log2.warning("123")
# #     # imp = input("模块名:")
# #     # CC = __import__(imp, fromlist=True)
# #     # print("cc = ", CC)
# #     # inp_func = input("请输入要执行的函数：")
# #     # print("func = ", inp_func)
# #     # f = getattr(CC, inp_func, None)
# #     # f(11)
# #     # show1.show(123)
# #     md5Str = hashlib.md5("12".encode('utf-8', errors='ignore')).hexdigest()
# #     print(md5Str)
# #     for i in range(0, 1000):
# #         current_time = int(round(time.time() * 1000))
# #         print(current_time)
#
from config import settings


def test2():
    age = settings.age
    print("age = ", age)
