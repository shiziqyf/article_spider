import json
import threading
import time

import global_var
from dao.articleDAO import ArticleDAO
from dao.imageDAO import ImageDAO
from dao.model.article import Article
from spider.image import generate_img_task_from_html
from spider.server.article_service import get_img_urls_from_html


def verify_article_img_deal(article):
    biz_log = global_var.get_value('biz_log')
    # biz_log.info('start verify_img_deal, article_id = %s', article.id)
    content_dirt = json.loads(article.content_pack)
    urls = get_img_urls_from_html(content_dirt['content'])
    if urls is not None and len(urls) > 0:
        image_resources = ImageDAO.queryByUrls(urls)
        if len(urls) == len(image_resources):
            ArticleDAO.updatedById(article.id, Article(img_deal_status=1))
            biz_log.info('verify_img_deal pass, article_id = %s', article.id)


def verify_img_deal_timing():
    earliest_time = 0
    while True:
        article = ArticleDAO.queryEarliestByImgDealStatus(0, earliest_time)
        if article is None:
            earliest_time = 0
            time.sleep(10)
            continue
        earliest_time = article.gmt_created_time
        verify_article_img_deal(article)
        time.sleep(0.1)


def generate_img_task():
    while True:
        article = ArticleDAO.queryEarliestByImgDealStatus(-1, 0)
        if article is None:
            time.sleep(10)
            continue
        content_dirt = json.loads(article.content_pack)
        content_html_str = content_dirt['content']
        generate_img_task_from_html(None, '', article.id, content_html_str)
        ArticleDAO.updatedById(article.id, Article(img_deal_status=0))


def start_verify_img_deal_new_thread():
    thread_deal = threading.Thread(target=verify_img_deal_timing)
    thread_generate = threading.Thread(target=generate_img_task)
    thread_deal.daemon = True
    thread_generate.daemon = True
    thread_deal.start()
    thread_generate.start()
