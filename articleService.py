from dao.model.article import Article
from dao.articleDAO import ArticleDAO


def saveArticle(article: Article):
    # ArticleDAO.queryByArticleUrl(article.source_url)
    ArticleDAO.insert(article)
