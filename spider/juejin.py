import json
import traceback

import requests
from lxml import etree
from lxml.html import tostring

from dao.model.article import Article
from reflact_test import show1
from spider import common, article_service

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

model_name = 'juejin'
target_site_name = 'juejin'
list_url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?spider=0'
list_version = "1"
detail_version = "1"


def req_post_json(url, json_body):
    response = requests.post(url=url, json=json_body)
    return response.json()


def req_get_text(url):
    response = requests.get(url)
    return response.text


def list_first(lis):
    return lis[0] if lis else ""


def start():
    serial_id = common.generate_serial_id(target_site_name)
    start_cursor = '0'
    list_task(serial_id, list_url, start_cursor)


def list_task(serial_id, request_url, cursor):
    data = {
        "sort_type": 300,
        "cursor": cursor,
        "limit": 20,
        "id_type": 2,
        "client_type": 2608
    }

    # TODO 生成 task


def page_task_execute(serial_id, request_url, data):
    resp_data_json = req_post_json(request_url, data)
    next_cursor = resp_data_json['cursor']
    data_list = resp_data_json['data']
    if data_list is None:
        return
    for item_data in data_list:
        item_type = item_data['item_type']
        if item_type != 2:
            continue
        article_id = item_data['item_info']['article_id']
        detail_url = "https://juejin.cn/post/" + article_id
        # TODO 生成 task

    list_task(serial_id, list_url, next_cursor)


def detail_task_execute(serial_id, request_url):
    resp_data_text = req_get_text(request_url)
    root = etree.HTML(resp_data_text)
    title_s = root.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/h1/text()')
    content_s = root.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/div[4]/div')
    title = list_first(title_s)
    content = list_first(content_s)
    content_html = ''
    if content != '':
        content_html = tostring(content, encoding="utf-8").decode("utf-8")
    print("保存: url=", request_url)
    # 保存到数据库中
    articleService.saveArticle(Article(request_url, json.dumps({
        'url': request_url,
        'title': title,
        'content': content_html
    }, ensure_ascii=False), "JUEJIN"))


if __name__ == '__main__':
    try:
        print("start......")
        show1.show()
        # page()
        print("end.....")
    except Exception as e:
        msg = traceback.format_exc()
        print(msg)
        print("异常", e)
