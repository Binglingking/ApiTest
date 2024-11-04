from core.AD_rest_client import RestClient


class ApiUtil(RestClient):

    """
    ApiUtil 类封装了与广告投放和定向模块相关的API请求。
    继承自 RestClient，提供了常用的HTTP请求方法。
    """
    def __init__(self):
        """
        初始化 ApiUtil 实例，调用父类的初始化方法。
        """
        super().__init__()

    def add_orientationModule(self, **kwargs):
        """
        新增定向模块。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/api/orientationModule/addOrEdit', **kwargs)

    def get_dxcx_data(self, **kwargs):
        """
        获取定向查询数据。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.get('/api/orientationModule/list', **kwargs)

    def get_tfcx_data(self, **kwargs):
        """
        获取投放查询数据。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.get('/api/channelAdv/list', **kwargs)

    def post_dxbj_data(self, **kwargs):
        """
        编辑定向模块。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/api/orientationModule/addOrEdit', **kwargs)

    def post_adv_status_data(self, **kwargs):
        """
        批量操作投放状态（开启或关闭）。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/api/channelAdv/batch/operate', **kwargs)

    def del_orientationModule(self, **kwargs):
        """
        删除定向模块。

        :param kwargs: 请求参数
        :return: 响应对象
        """
        return self.post('/api/orientationModule/delete', **kwargs)


# 创建 ApiUtil 的实例，供其他模块使用
apiutil = ApiUtil()


