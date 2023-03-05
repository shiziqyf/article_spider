_global_dict = {}


def _init():  # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    _global_dict[key] = value


def get_value(key):
    try:
        return _global_dict[key]
    except Exception as e:
        print('读取 ' + key + ' 失败\r\n')
        raise e
