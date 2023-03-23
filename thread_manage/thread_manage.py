import threading

import global_var

need_manage_thread = {}


def add_need_manage_thread(thread_id, alias):
    need_manage_thread[thread_id] = alias


def check_thread():
    biz_log = global_var.get_value('biz_log')
    thread_enum = threading.enumerate()
    for thread in thread_enum:
        thread_id = thread.ident
        if thread_id in need_manage_thread:
            alias = need_manage_thread[thread_id]
            is_alive = thread.is_alive()
            biz_log.info('thread status. alias:%s, isAlive:%s', alias, is_alive)
