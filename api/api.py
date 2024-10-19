from core.api_util import apiutil


def dxcx_get(params):
    response = apiutil.get_dxcx_data(params=params)
    return response.json()

def tfcx_get(params):
    response = apiutil.get_tfcx_data(params=params)
    return response.json()

def dxbj_post(params):
    """
    这是测试定向模块编辑功能
    :param params:
    :return:
    """
    response = apiutil.post_dxbj_data(json=params)
    return response.json()

def adv_status_post(params):
    """
    这是测试投放状态开启功能
    :param params:
    :return:
    """
    response = apiutil.post_adv_status_data(json=params)
    return response.json()
def add_orientationModule(params):
    """
    这是测试定向模块新增功能
    :param params:
    :return:
    """
    response = apiutil.add_orientationModule(json=params)
    return response.json()

def del_orientationModule(params):
    """
    这是测试定向模块新增功能
    :param params:
    :return:
    """
    response = apiutil.del_orientationModule(json=params)
    return response.json()