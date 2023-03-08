class Task:
    def __init__(self, id=None, identifies=None, name=None, status=None, module_name=None, execute_func_name=None,
                 task_type=None, serial_id=None, repeat_expire_time=None, priority=None, params=None, created_time=None, valid_status=None, parent_task_id=None, gmt_created_time=None, gmt_updated_time=None):
        self.id = id
        self.identifies = identifies
        self.name = name
        self.status = status
        self.module_name = module_name
        self.execute_func_name = execute_func_name
        self.params = params
        self.task_type = task_type
        self.serial_id = serial_id
        self.repeat_expire_time = repeat_expire_time
        self.created_time = created_time
        self.priority = priority
        self.gmt_created_time = gmt_created_time
        self.gmt_updated_time = gmt_updated_time
        self.valid_status = valid_status
        self.parent_task_id = parent_task_id

#
#
#


# id = None
# identifies: str
# name: str
# status: int
# module_name: str
# execute_func_name: str
# params: dict
# task_type: str
# serial_id: str
# repeat_expire_time: int
# created_time: int
# priority: int
# gmt_created_time = None
# gmt_updated_time = None
