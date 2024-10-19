import pymysql

from utils.log_util import logger
from utils.read_ini import read_ini

data = read_ini()['mysql']
# print(data)
Db_CONF = {
    'host': data['MYSQL_HOST'],
    'port': int(data['MYSQL_PORT']),
    'user': data['MYSQL_USER'],
    'password': data['MYSQL_PASSWORD']
}

class MySQL:
    def __init__(self):
        self.conn = pymysql.connect(**Db_CONF)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def __del__(self):
        self.cur.close()
        self.conn.close()

    def select_db(self, sql):
        """
        执行sql语句，返回查询结果
        :param sql:
        :return:
        """
        logger.info(f"开始执行sql:" + sql)
        self.cur.execute(sql)
        return self.cur.fetchall()

    def execute_db(self, sql):
        """
        执行sql语句，返回受影响行数
        :param sql:
        :return:
        """
        try:
            logger.info(f"开始执行sql:"+ sql)
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.error("执行sql时报错：".format(e))

db = MySQL()
if __name__ == '__main__':
    db = MySQL()
    # sql = "SELECT channel_id FROM admax_test.advertiser_report where id = 5"
    # result = db.select_db(sql)
    # # print(type(result))
    # print(result[0]['channel_id'])
