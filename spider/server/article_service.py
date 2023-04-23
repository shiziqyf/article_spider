import re

from dao.imageDAO import ImageDAO
from dao.model.article import Article
from dao.articleDAO import ArticleDAO
import json


def saveArticle(article: Article):
    oldArticle = ArticleDAO.queryOneByArticleUrl(article.source_url)

    if oldArticle is None:
        return ArticleDAO.insert(article)

    return oldArticle.id
    # else:
    #     ArticleDAO.


def fillContentPack(article: Article):
    if article is None:
        return
    content_pack = article.content_pack
    if content_pack is None or len(content_pack) == 0:
        oss_key = article.content_oss_key


def get_img_urls_from_html(html_str):
    return re.findall('img[\s\S]+?src=[\'\"](.*?)[\'\"]', html_str, re.S)

# 检查 article 图片是否处理完成
