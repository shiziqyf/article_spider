class Task:
    def __init__(self, identifies=None, name=None, status=None, module_name=None, execute_func_name=None,
                 task_type=None, serial_id=None, repeat_expire_time=None, priority=None, params=None, created_time=None):
        self.id = None
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
        self.gmt_created_time = None
        self.gmt_updated_time = None
