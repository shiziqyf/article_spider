from dao.model.article import Article
from mysqlConn import MysqlConnUtil


class ArticleDAO:
    @staticmethod
    def insert(article: Article):
        sql = 'insert into article_resource(source, source_url, content_pack, content_format, transform_status) values (%s,%s, %s, %s, %s)'
        conn = MysqlConnUtil.getConn()
        cursor = conn.cursor()
        cursor.execute(sql, (article.source, article.source_url, article.content_pack, "HTML", "INIT"))
        conn.commit()
