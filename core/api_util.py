from core.rest_client import RestClient


class ApiUtil(RestClient):
    def __init__(self):
        super().__init__()

    def get_dxcx_data(self, **kwargs):
        return self.get('/api/orientationModule/list', **kwargs)
    def get_tfcx_data(self, **kwargs):
        return self.get('/api/channelAdv/list', **kwargs)

    def post_dxbj_data(self, **kwargs):
        return self.post('/api/orientationModule/addOrEdit', **kwargs)
    def post_adv_status_data(self, **kwargs):
        return self.post('/api/channelAdv/batch/operate', **kwargs)
    def add_orientationModule(self, **kwargs):
        return self.post('/api/orientationModule/addOrEdit', **kwargs)
    def del_orientationModule(self, **kwargs):
        return self.post('/api/orientationModule/delete', **kwargs)

apiutil = ApiUtil()


