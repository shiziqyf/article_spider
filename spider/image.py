import re

from dao.model.task import Task
from spider import task_service, common

model_name = 'spider.image'


def generate_img_task_from_html(parent_task_id, serial_id, article_resource_id, html_str):
    img_urls = re.findall('img src="(.*?)"', html_str, re.S)

    if len(img_urls) > 0:
        for img_url in img_urls:
            now_time = common.get_current_time()
            identifies = common.generate_task_id('', img_url, '', 1)
            task_execute_func_params = {
                "img_url": img_url,
                "serial_id": serial_id,
                "article_resource_id": article_resource_id
            }
            task = Task(identifies=identifies, name="img", status=0, module_name=model_name, execute_func_name="img_task_execute",
                        task_type="IMG", serial_id=serial_id, repeat_expire_time=-1, priority=1, valid_status=1, parent_task_id=parent_task_id, params=task_execute_func_params, created_time=now_time)
            task_service.save_task(task)


def img_task_execute(task_id, execute_params):
    print("img_task_execute params=", str(execute_params))
