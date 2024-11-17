import requests
from core.FB_rest_client import RestClient

class FBApi(RestClient):
    def __init__(self):
        super().__init__()

    def add_original_package(self, url, **kwargs):
        return self.post('/admax-packerapi/packer/original/add', **kwargs)

    def list_original_packages(self, url,  **kwargs):
        return self.post('/admax-packerapi/packer/original/list', **kwargs)

    def add_task(self, url, **kwargs):
        return self.post('/admax-packerapi/packer/task/add', **kwargs)

    def update_task(self, url, **kwargs):
        return self.post('/admax-packerapi/packer/task/update', **kwargs)

    def list_tasks(self, url, **kwargs):
        return self.post('/admax-packerapi/packer/task/list', **kwargs)

    def delete_task(self, url, **kwargs):
        return self.post('/admax-packerapi/packer/task/delete', **kwargs)