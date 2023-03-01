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
        MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryByArticleUrl(url: str):
        sql = 'select * from  article_resource where source_url = %s'
        conn = MysqlConnUtil.getConn()
        cursor = conn.cursor()
        cursor.execute(sql, url)
        result = cursor.fetchall()
        MysqlConnUtil.closeResource(cursor, conn)
        print(result)
        print(type(result))
