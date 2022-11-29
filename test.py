import logging

from log.loggerHandler import LoggerHandler

if __name__ == '__main__':
    log = LoggerHandler("test.log").log
    log2 = LoggerHandler("test2.log", True).log
    # log.debug("dddds22231233")Î
    log2.warning("123")
