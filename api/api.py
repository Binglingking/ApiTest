"""
这是一个API接口封装文件，提供了多个与广告投放和定向模块相关的功能。
"""

from core.api_util import apiutil
class Api:
    def dxcx_get(params):
        """
        获取定向查询数据
        :param params: 查询参数
        :return: 查询结果的JSON响应
        """
        response = apiutil.get_dxcx_data(params=params)
        return response.json()


    def tfcx_get(params):
        """
        获取投放查询数据
        :param params: 查询参数
        :return: 查询结果的JSON响应
        """
        response = apiutil.get_tfcx_data(params=params)
        return response.json()


    def dxbj_post(params):
        """
        编辑定向模块
        :param params: 编辑参数
        :return: 编辑结果的JSON响应
        """
        response = apiutil.add_oriMod_Edit(json=params)
        return response.json()


    def adv_status_post(params):
        """
        开启或关闭投放状态
        :param params: 状态参数
        :return: 状态操作结果的JSON响应
        """
        response = apiutil.post_adv_status_data(json=params)
        return response.json()


    def add_orientationModule(params):
        """
        新增定向模块
        :param params: 新增参数
        :return: 新增结果的JSON响应
        """
        response = apiutil.add_orientationModule(json=params)
        return response.json()


    def del_orientationModule(params):
        """
        删除定向模块
        :param params: 删除参数
        :return: 删除结果的JSON响应
        """
        response = apiutil.del_orientationModule(json=params)
        return response.json()
api = Api()