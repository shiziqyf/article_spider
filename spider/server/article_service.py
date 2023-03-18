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


def get_img_urls_from_html(html_str):
    return re.findall('img src="(.*?)"', html_str, re.S)


# 检查 article 图片是否处理完成
def verify_img_deal():
    print("ddsfdsfsdf")
    article = ArticleDAO.queryEarliestByImgDealStatus(0)
    if article is None:
        return
    content_dirt = json.loads(article.content_pack)
    urls = get_img_urls_from_html(content_dirt['content'])
    if urls is None or len(urls) == 0:
        # TODO 更新
        return
    ImageDAO.queryByUrls(urls)

