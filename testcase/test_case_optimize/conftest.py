from utils.log_util import logger
from utils.mysql_util import db


def get_orientation_module_id():
    """
    查询并返回用例中新建的定向模板的ID
    :return: 定向模板的ID
    """
    # SQL查询语句，查找model_name包含'pytest_sql'且未被删除的记录
    sql = """
    SELECT id
    FROM admax_test.channel_orientation_model
    WHERE model_name LIKE '%pytest_sql%'
      AND deleted_at IS NULL
    LIMIT 1
    """

    # 执行SQL查询
    result = db.select_db(sql)

    # 记录查询结果
    logger.info(f'SQL执行结果: {result}')

    # 检查查询结果是否为空
    if not result:
        logger.warning('未找到符合条件的定向模板')
        return None

    # 返回查询到的第一个记录的ID
    return result[0]['id']
# id = get_orientation_module_id()
# print(id)
