import re

import global_var
from dao.imageDAO import ImageDAO
from dao.model.image_resource import ImageResource
from dao.model.task import Task
from spider import common
from spider.server import task_service, image_service

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
    biz_log = global_var.get_value('biz_log')
    biz_log.info('img_task_execute, task_id=%s', task_id)
    img_url = execute_params['img_url']
    # TODO 上传到oss
    article_resource_id = execute_params['article_resource_id']
    image = ImageResource(url=img_url, oss_key='', from_task_id=task_id, from_article_resource_id=article_resource_id)
    image_service.save_image(image)
    biz_log.info('img_task_execute finish, url=%s, task_id=%s', img_url, task_id)
