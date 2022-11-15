import traceback

import requests
from lxml import etree
from lxml.html import tostring

from dao.articleDAO import ArticleDAO
from dao.model.article import Article
import json


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def req_post(url, data):
    response = requests.post(url, data)
    return response.json()


def req_get_text(url):
    response = requests.get(url)
    return response.text


def list_first(lis):
    return lis[0] if lis else ""


def start():
    request_url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_all_feed?spider=0'
    data = {
        "sort_type": 200,
        "cursor": str(1),
        "limit": 20
    }
    resp_data_json = req_post(request_url, data)
    data_list = resp_data_json['data']
    if data_list:
        for item_data in data_list:
            item_type = item_data['item_type']
            if item_type != 2:
                continue
            article_id = item_data['item_info']['article_id']
            detail_url = "https://juejin.cn/post/" + article_id
            detail_page(detail_url)


def detail_page(url):
    resp_data_text = req_get_text(url)
    root = etree.HTML(resp_data_text)
    title_s = root.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/h1/text()')
    content_s = root.xpath('//*[@id="juejin"]/div[1]/main/div/div[1]/article/div[4]/div')
    title = list_first(title_s)
    content = list_first(content_s)
    content_html = ''
    if content != '':
        content_html = tostring(content, encoding="utf-8").decode("utf-8")
    print("保存: url=", url)
    # 保存到数据库中
    ArticleDAO.insert(Article(json.dumps({
        'url': url,
        'title': title,
        'content': content_html
    }, ensure_ascii=False), 'JUEJIN'))


if __name__ == '__main__':

    try:
        start()
    except Exception as e:
        msg = traceback.format_exc()  # 方式1
        print(msg)
        print("异常", e)
