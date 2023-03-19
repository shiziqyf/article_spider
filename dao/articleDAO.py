from dao.model.article import Article
from dao.mysqlConn import MysqlConnUtil


class ArticleDAO:
    @staticmethod
    def insert(article: Article):
        conn = None
        cursor = None
        try:
            sql = 'insert into article_resource(source, source_url, content_pack, content_format, transform_status, from_task_id, img_deal_status) ' \
                  'values (%s, %s, %s, %s, %s, %s, %s)'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, (article.source, article.source_url, article.content_pack, "HTML", "INIT", article.from_task_id, article.img_deal_status))
            last_id = cursor.lastrowid
            conn.commit()
            return last_id
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryOneByArticleUrl(url: str) -> Article:
        conn = None
        cursor = None
        try:
            sql = 'select id, source, source_url, content_pack, from_task_id, img_deal_status, gmt_created_time ' \
                  'from  article_resource where source_url = %s'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, url)
            result = cursor.fetchone()
            MysqlConnUtil.closeResource(cursor, conn)
            return ArticleDAO.resultToArticle(cursor, result)
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryEarliestByImgDealStatus(img_deal_status, earliest_time) -> Article:
        conn = None
        cursor = None
        try:
            sql = 'select id, source, source_url, content_pack, from_task_id, img_deal_status, gmt_created_time ' \
                  'from  article_resource where img_deal_status = %s and gmt_created_time > %s order by gmt_created_time asc limit 1'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, (img_deal_status, earliest_time))
            result = cursor.fetchone()
            MysqlConnUtil.closeResource(cursor, conn)
            return ArticleDAO.resultToArticle(cursor, result)
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def updatedById(id, article):
        conn = None
        cursor = None
        try:
            sql = 'update article_resource set'
            sql_part, params = ArticleDAO.generate_updated_sql(article)
            if params is None or len(params) == 0:
                return
            sql = sql + sql_part + ' where id=%s limit 1'
            params.append(id)
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def generate_updated_sql(article: Article):
        sql = ''
        params = []
        property_map = article.__dict__
        first = True
        for key in property_map:
            value = property_map[key]
            if value is None:
                continue
            if first:
                sql = sql + ' ' + key + '=%s'
                first = False
            else:
                sql = sql + ' ,' + key + '=%s'
            params.append(str(value))
        return sql, params

    @staticmethod
    def resultToArticle(cursor, result):
        if result is None:
            return None
        i = 0
        article_dirt = {}
        for item in result:
            title = cursor.description[i][0]
            article_dirt[title] = item
            i = i + 1
        return Article(**article_dirt)
