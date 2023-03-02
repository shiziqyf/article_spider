def __init__(self, name, status, module_name, execute_func, task_type, params=None):
    if params is None:
        params = {}
    self.id = None
    self.name = name
    self.status = status
    self.module_name = module_name
    self.execute_func = execute_func
    self.params = params
    self.task_type = task_type

    self.gmt_created_time = None
    self.gmt_updated_time = None

