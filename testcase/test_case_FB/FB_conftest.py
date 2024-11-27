from utils.log_util import logger
from utils.mysql_util import db


def dl_task_id():
    """
    查询并返回用例中新建的定向模板的ID
    :return: 定向模板的ID
    """

    sql = """
    SELECT task_id FROM admax_test.package_task WHERE task_name LIKE 'py_add%' AND deleted_at is null; 
    """

    # 执行SQL查询
    result = db.select_db(sql)
    print(result)

    # 记录查询结果
    logger.info(f'SQL执行结果: {result}')

    # 检查查询结果是否为空
    if not result:
        logger.warning('未找到符合条件的task_id')
        return None

    # 返回查询到的第一个记录的ID
    return result
# dl_task_id()