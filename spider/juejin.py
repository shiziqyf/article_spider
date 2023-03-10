import json

import requests
from lxml import etree
from lxml.html import tostring

import global_var
from dao.model.article import Article
from dao.model.task import Task
from spider import common, article_service, task_service

model_name = 'spider.juejin'
target_site_name = 'juejin'
list_url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?spider=0'
list_version = "2"
detail_version = "1"
list_repeat_keep_time = 14400000  # 4小时
# list_repeat_keep_time = 1000  # 1秒
detail_repeat_keep_time = -1  # 永久


def req_post_json(url, json_body):
    response = requests.post(url=url, json=json_body)
    return response.json()


def req_get_text(url):
    response = requests.get(url)
    return response.content.decode('utf-8', 'ignore').encode('gbk', 'replace').decode('gbk', 'replace')
    # return response.text.encode('utf-8').decode('utf-8')


def list_first(lis):
    return lis[0] if lis else ""


is_first = None


def juejin_spider_start():
    biz_log = global_var.get_value('biz_log')
    biz_log.info('juejin_spider start......')
    model = 'INCREMENTAL'
    global is_first
    if is_first is None:
        is_first = global_var.get_value('is_first')

    if is_first:
        model = 'FULL'
        is_first = False
    try:
        serial_id = common.generate_serial_id(target_site_name)
        start_cursor = '0'
        list_task(serial_id, list_url, start_cursor, model, None)
    except Exception as e:
        biz_log.error(e)


def list_task(serial_id, url, cursor, model, parent_task_id):
    req_params = {
        "sort_type": 300,
        "cursor": cursor,
        "limit": 20,
        "id_type": 2,
        "client_type": 2608
    }

    now_time = common.get_current_time()
    repeat_expire_time = now_time + list_repeat_keep_time
    identifies = common.generate_task_id(target_site_name, url, req_params, list_version)
    task_execute_func_params = {
        "url": url,
        "req_params": req_params,
        "serial_id": serial_id,
        "model": model
    }
    task = Task(identifies=identifies, name="juejin_list", status=0, module_name=model_name, execute_func_name="page_task_execute",
                task_type=None, serial_id=serial_id, repeat_expire_time=repeat_expire_time, priority=1, valid_status=1, parent_task_id=parent_task_id, params=task_execute_func_params, created_time=now_time)
    task_service.save_task(task)


def page_task_execute(task_id, execute_params):
    biz_log = global_var.get_value('biz_log')
    url = execute_params['url']
    biz_log.info('juejin_page_task_execute, url=%s, params=%s', url, execute_params)
    req_params = execute_params['req_params']
    serial_id = execute_params['serial_id']
    model = ''
    if 'model' in execute_params:
        model = execute_params['model']
    # biz_log.info('page_task_execute, url')
    resp_data_json = req_post_json(url, req_params)
    next_cursor = resp_data_json['cursor']
    data_list = resp_data_json['data']
    if data_list is None:
        return
    need_continue_list = False
    for item_data in data_list:
        item_type = item_data['item_type']
        if item_type != 2:
            continue
        article_id = item_data['item_info']['article_id']
        detail_url = "https://juejin.cn/post/" + article_id

        now_time = common.get_current_time()
        detail_task_id = common.generate_task_id(target_site_name, detail_url, article_id, detail_version)
        task_execute_func_params = {
            "url": detail_url,
            'serial_id': serial_id
        }
        task = Task(identifies=detail_task_id, name="juejin_detail", status=0, module_name=model_name, execute_func_name="detail_task_execute",
                    task_type=None, serial_id=serial_id, repeat_expire_time=detail_repeat_keep_time, priority=2, valid_status=1, parent_task_id=task_id, params=task_execute_func_params, created_time=now_time)
        save_result = task_service.save_task(task)
        has_no_repeat_task = save_result["not_repeat"]
        if has_no_repeat_task:
            need_continue_list = True
    biz_log.info('need_continue_list = %s', need_continue_list)
    # if next_cursor
    if model == 'FULL':
        list_task(serial_id, list_url, next_cursor, model, task_id)
    elif need_continue_list:
        list_task(serial_id, list_url, next_cursor, model, task_id)


def detail_task_execute(task_id, execute_params):
    biz_log = global_var.get_value('biz_log')
    url = execute_params['url']
    biz_log.info('juejin_detail_task_execute, url=%s, task_id=%s', url, task_id)
    resp_data_text = req_get_text(url)
    root = etree.HTML(resp_data_text)
    title_s = root.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/h1/text()')
    content_s = root.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/div[4]/div')
    published_time_s = root.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/div[3]/div/div[2]/time/text()')
    title = list_first(title_s)
    content = list_first(content_s)
    if len(content) < 1:
        biz_log.error("juejin detail content is blank, task_id=%s", task_id)
        biz_log.info("resp_data_text = %s", resp_data_text)
        raise Exception('juejin detail content is blank')
    published_time = list_first(published_time_s)
    content_html = ''
    if content != '':
        content_html = tostring(content, encoding="utf-8").decode("utf-8")
    biz_log.info('juejin_detail fetch finish, url=%s, task_id=%s', url, task_id)
    # 保存到数据库中
    save_result = article_service.saveArticle(Article(url, json.dumps({
        'url': url,
        'title': title,
        'content': content_html,
        'published_time': published_time
    }, ensure_ascii=False), "JUEJIN", from_task_id=task_id))
    biz_log.info('save article, url=%s, result=%s', url, save_result)
