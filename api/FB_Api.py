"""
这是一个API接口封装文件，提供了多个与广告投放和任务管理相关的功能。
"""

from core.FB_apiUtil import FBApiUtil


class FBApi(object):

    def add_original_package(params):
        """
        新增原始包
        :param params: 新增参数
        :return: 新增结果的JSON响应
        """
        response = FBApiUtil.add_original_package(json=params)
        return response

    def list_original_packages(params):
        """
        获取原始包列表
        :param params: 查询参数
        :return: 查询结果的JSON响应
        """
        response = FBApiUtil.list_original_packages(params=params)
        return response

    def add_task(params):
        """
        新增任务
        :param params: 新增参数
        :return: 新增结果的JSON响应
        """
        response = FBApiUtil.add_task(json=params)
        return response

    def update_task(params):
        """
        更新任务
        :param params: 更新参数
        :return: 更新结果的JSON响应
        """
        response = FBApiUtil.update_task(json=params)
        return response

    def list_tasks(self,params):
        """
        获取任务列表
        :param params: 查询参数
        :return: 查询结果的JSON响应
        """
        response = FBApiUtil.list_tasks(json=params)
        return response

    def delete_task(self,params):
        """
        删除任务
        :param params: 删除参数
        :return: 删除结果的JSON响应
        """
        response = FBApiUtil.delete_task(json=params)
        return response


api = FBApi()
