from core.api_util import apiutil


def dxcx_get(params):
    response = apiutil.get_dxcx_data(params=params)
    return response.json()


def dxbj_post(params):
    """
    这是测试定向模块编辑功能
    :param params:
    :return:
    """
    response = apiutil.post_dxbj_data(json=params)
    return response.json()