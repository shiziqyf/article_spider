from dao.model.article import Article
from mysqlConn import MysqlConnUtil


class ArticleDAO:
    @staticmethod
    def insert(article: Article):
        sql = 'insert into article(source, content, created, updated) values ("%s", "%s", "%s","%s")'
        conn = MysqlConnUtil.getConn()
        cursor = conn.cursor()
        cursor.execute(sql, (article.source, article.content, article.created, article.updated))
        conn.commit()
