from dao.model.task import Task
from dao.mysqlConn import MysqlConnUtil


class TaskDAO:
    @staticmethod
    def insert(task: Task):
        conn = None
        cursor = None
        try:
            sql = 'insert into spider_task(identifies, name, status, module_name, execute_func_name, params, task_type, serial_id, valid_status, parent_task_id, repeat_expire_time, priority, created_time) ' \
                  'values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, (task.identifies, task.name, task.status, task.module_name, task.execute_func_name, str(task.params),
                                 task.task_type, task.serial_id, task.valid_status, task.parent_task_id, task.repeat_expire_time, task.priority, task.created_time))
            conn.commit()
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryOneByIdentifies(identifies) -> Task:
        conn = None
        cursor = None
        try:
            sql = 'select * from spider_task where identifies = %s'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, identifies)
            result = cursor.fetchone()
            return TaskDAO.resultToTask(cursor, result)
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryOneByIdentifiesAndValid(identifies, valid_status) -> Task:
        conn = None
        cursor = None
        try:
            sql = 'select * from spider_task where identifies = %s and valid_status = %s order by gmt_created_time desc limit 1'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, (identifies, valid_status))
            result = cursor.fetchone()
            return TaskDAO.resultToTask(cursor, result)
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def updatedById(task_id, task: Task):
        conn = None
        cursor = None
        try:
            sql = 'update spider_task set'
            sql_part, params = TaskDAO.generate_updated_sql(task)
            if params is None or len(params) == 0:
                return
            sql = sql + sql_part + ' where id=%s limit 1'
            params.append(task_id)
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryEarliestTaskByType(task_type):
        conn = None
        cursor = None
        try:
            sql = 'select * from spider_task where status = 0 and task_type = %s and priority > -5 order by priority desc limit 1'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, task_type)
            result = cursor.fetchone()
            return TaskDAO.resultToTask(cursor, result)
        except Exception as e:
            raise e
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def generate_updated_sql(task: Task):
        sql = ''
        params = []
        property_map = task.__dict__
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
    def resultToTask(cursor, result):
        if result is None:
            return None
        i = 0
        task_dirt = {}
        for item in result:
            title = cursor.description[i][0]
            task_dirt[title] = item
            i = i + 1
        return Task(**task_dirt)
