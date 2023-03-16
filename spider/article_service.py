from dao.model.article import Article
from dao.articleDAO import ArticleDAO


def saveArticle(article: Article):
    oldArticle = ArticleDAO.queryOneByArticleUrl(article.source_url)

    if oldArticle is None:
        return ArticleDAO.insert(article)

    return oldArticle.id
    # else:
    #     ArticleDAO.
