from dao.model.image_resource import ImageResource
from dao.mysqlConn import MysqlConnUtil


class ImageDAO:
    @staticmethod
    def insert(image: ImageResource):
        conn = None
        cursor = None
        try:
            sql = 'insert into image_resource(url, oss_key, from_task_id, from_article_resource_id) values (%s, %s, %s, %s)'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, (image.url, image.oss_key, image.from_task_id, image.from_article_resource_id))
            last_id = cursor.lastrowid
            conn.commit()
            return last_id
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryOneByUrl(url: str) -> ImageResource:
        conn = None
        cursor = None
        try:
            sql = 'select id, url, oss_key, from_task_id, from_article_resource_id from  image_resource where url = %s'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, url)
            result = cursor.fetchone()
            MysqlConnUtil.closeResource(cursor, conn)
            return ImageDAO.resultToImage(cursor, result)
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryByUrls(urls):
        if urls is None or len(urls) == 0:
            return None
        urls_str = ','.join(['%s'] * len(urls))
        conn = None
        cursor = None
        try:
            sql = 'select id, url, oss_key, from_task_id, from_article_resource_id from  image_resource where url in (%s)' % urls_str
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, urls)
            results = cursor.fetchall()
            MysqlConnUtil.closeResource(cursor, conn)
            return ImageDAO.resultToImageList(cursor, results)
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def updatedById(id, image):
        conn = None
        cursor = None
        try:
            sql = 'update image_resource set'
            sql_part, params = ImageDAO.generate_updated_sql(image)
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
    def generate_updated_sql(image: ImageResource):
        sql = ''
        params = []
        property_map = image.__dict__
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
    def resultToImage(cursor, result):
        if result is None:
            return None
        i = 0
        image_dirt = {}
        for item in result:
            title = cursor.description[i][0]
            image_dirt[title] = item
            i = i + 1
        return ImageResource(**image_dirt)

    @staticmethod
    def resultToImageList(cursor, results):
        if results is None:
            return None
        image_resource_list = []
        for result in results:
            i = 0
            image_dirt = {}
            for item in result:
                title = cursor.description[i][0]
                image_dirt[title] = item
                i = i + 1
            image_resource_list.append(ImageResource(**image_dirt))
        return image_resource_list

