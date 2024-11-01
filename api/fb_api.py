# D:\ApiTest\api\fb_api.py
import requests
from core.rest_client import RestClient

class FBApi(RestClient):
    def __init__(self):
        super().__init__()

    def add_original_package(self, **kwargs):
        return self.post('/admax-packerapi/packer/original/add', **kwargs)

    def list_original_packages(self, **kwargs):
        return self.post('/admax-packerapi/packer/original/list', **kwargs)

    def add_task(self, **kwargs):
        return self.post('/admax-packerapi/packer/task/add', **kwargs)

    def update_task(self, **kwargs):
        return self.post('/admax-packerapi/packer/task/update', **kwargs)

    def list_tasks(self, **kwargs):
        return self.post('/admax-packerapi/packer/task/list', **kwargs)

    def delete_task(self, **kwargs):
        return self.post('/admax-packerapi/packer/task/delete', **kwargs)