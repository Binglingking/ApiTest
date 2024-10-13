from core.rest_client import RestClient


class ApiUtil(RestClient):
    def __init__(self):
        super().__init__()

    def get_dxcx_data(self, **kwargs):
        return self.get('/api/orientationModule/list', **kwargs)

    def post_dxbj_data(self, **kwargs):
        return self.post('/api/orientationModule/addOrEdit', **kwargs)

apiutil = ApiUtil()