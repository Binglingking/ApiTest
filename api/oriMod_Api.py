"""
这是一个API接口封装文件，提供了多个与广告投放和定向模块相关的功能。
"""

from core.oriMod_apiUtil import OriModApiUtil


class OriModApi(object):

    def add_orientationModule(params):
        """
        新增定向模块
        :param params: 新增参数
        :return: 新增结果的JSON响应
        """
        response = OriModApiUtil.add_orientationModule(json=params)
        return response

    def oriMod_Search(params):
        """
        获取定向查询数据
        :param params: 查询参数
        :return: 查询结果的JSON响应
        """
        response = OriModApiUtil.oriMod_Search(params=params)
        return response

    def add_oriMod_Edit(params):
        """
        编辑定向模块
        :param params: 编辑参数
        :return: 编辑结果的JSON响应
        """
        response = OriModApiUtil.add_oriMod_Edit(json=params)
        return response

    def copy_oriMod(params):
        """
        获取定向查询数据
        :param params: 查询参数
        :return: 查询结果的JSON响应
        """
        response = OriModApiUtil.copy_oriMod(json=params)
        return response

    def del_orientationModule(params):
        """
        删除定向模块
        :param params: 删除参数
        :return: 删除结果的JSON响应
        """
        response = OriModApiUtil.del_orientationModule(json=params)
        return response


api = OriModApi()
