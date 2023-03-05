from dao.model.article import Article
from dao.mysqlConn import MysqlConnUtil


class ArticleDAO:
    @staticmethod
    def insert(article: Article):
        conn = None
        cursor = None
        try:
            sql = 'insert into article_resource(source, source_url, content_pack, content_format, transform_status) values (%s,%s, %s, %s, %s)'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, (article.source, article.source_url, article.content_pack, "HTML", "INIT"))
            conn.commit()
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryOneByArticleUrl(url: str) -> Article:
        conn = None
        cursor = None
        try:
            sql = 'select * from  article_resource where source_url = %s'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, url)
            result = cursor.fetchone()
            MysqlConnUtil.closeResource(cursor, conn)
            return result
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)
