from dao.model.task import Task
from mysqlConn import MysqlConnUtil


class TaskDAO:
    @staticmethod
    def insert(task: Task):
        conn = None
        cursor = None
        try:
            sql = 'insert into spider_task(identifies, name, status, module_name, execute_func_name, params, task_type, serial_id, expire_time, priority) ' \
                  'values (%s,%s, %s, %s, %s,%s,%s, %s, %s, %s)'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, (task.identifies, task.name, task.status, task.module_name, task.execute_func_name, task.params,
                                 task.task_type, task.serial_id, task.serial_id, task.expire_time, task.priority))
            conn.commit()
        except Exception:
            raise
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def queryOneByIdentifies(identifies) -> Task:
        conn = None
        cursor = None
        try:
            sql = 'select * from  spider_task where identifies = %s'
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, identifies)
            result = cursor.fetchone()
            MysqlConnUtil.closeResource(cursor, conn)
            return result
        except Exception:
            raise
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def updatedById(task_id, task: Task):
        conn = None
        cursor = None
        try:
            # name, status, module_name, execute_func_name, params, task_type, serial_id, expire_time, priority
            sql = 'update spider_task set'
            sql_part, params = TaskDAO.generate_updated_sql(task)
            if params is None or len(params) == 0:
                return 0
            sql = sql + sql_part + ' where id=%s limit 1'
            params.append(task_id)
            print("updated_sql : ", sql)
            conn = MysqlConnUtil.getConn()
            cursor = conn.cursor()
            cursor.execute(sql, params)
            result = cursor.fetchone()
            conn.commit()
            MysqlConnUtil.closeResource(cursor, conn)
            return result
        except Exception:
            raise
        finally:
            MysqlConnUtil.closeResource(cursor, conn)

    @staticmethod
    def generate_updated_sql(task: Task):
        sql = ""
        params = []
        property_map = task.__dict__
        first = True
        for key in property_map:
            value = property_map[key]
            if value is None:
                continue
            if first:
                sql = sql + " " + key + "=%s"
                first = False
            else:
                sql = sql + " ," + key + "=%s"
            params.append(str(value))
        return sql, params


if __name__ == '__main__':
    task = Task(name="test e", identifies="122")
    count = TaskDAO.updatedById("2", task)
    print("count: ", count)
