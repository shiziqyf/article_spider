import hashlib
import time
import random


def generate_task_id(site_name, url, params, version):
    unique_str = str(site_name) + str(url) + str(params) + str(version)
    return hashlib.md5(unique_str.encode('utf-8', errors='ignore')).hexdigest()


def generate_serial_id(target_site_name):
    current_time = int(round(time.time() * 1000))
    return str(target_site_name) + "_" + str(current_time) + "_" + str(random.randint(0, 1000))


def get_current_time():
    return int(round(time.time() * 1000))

