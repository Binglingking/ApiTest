from core.FB_rest_client import RestClient


class FBApiUtil(RestClient):
    """
    ApiUtil 类封装了与广告投放和任务管理相关的API请求。
    继承自 RestClient，提供了常用的HTTP请求方法。
    """

    def __init__(self):
        """
        初始化 ApiUtil 实例，调用父类的初始化方法。
        """
        super().__init__()

    def add_original_package(self, **kwargs):
        """
        新增原始包。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/admax-packerapi/packer/original/add', **kwargs)

    def list_original_packages(self, **kwargs):
        """
        获取原始包列表。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/admax-packerapi/packer/original/list', **kwargs)

    def add_task(self, **kwargs):
        """
        新增任务。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/admax-packerapi/packer/task/add', **kwargs)

    def update_task(self, **kwargs):
        """
        更新任务。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/admax-packerapi/packer/task/update', **kwargs)

    def list_tasks(self, **kwargs):
        """
        获取任务列表。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/admax-packerapi/packer/task/list', **kwargs)

    def delete_task(self, **kwargs):
        """
        删除任务。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/admax-packerapi/packer/task/delete', **kwargs)


# 创建 FBApiUtil 的实例，供其他模块使用
FBApiUtil = FBApiUtil()
