import logging

from log.loggerHandler import LoggerHandler
# import reflact_test.show1

if __name__ == '__main__':
    # log = LoggerHandler("test.log").log
    # log2 = LoggerHandler("test2.log", True).log
    # # log.debug("dddds22231233")Î
    # log2.warning("123")
    imp = input("模块名:")
    CC = __import__(imp, fromlist=True)
    print("cc = ", CC)
    inp_func = input("请输入要执行的函数：")
    print("func = ", inp_func)
    f = getattr(CC, inp_func, None)
    f(11)
    # show1.show(123)
