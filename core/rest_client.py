import json
import requests
from utils.log_util import logger

test_url = "https://test-admax.yostar.net"
Authorization_test = {
        "Head": {"token": "9f6ed40924488358990084e699901b35476de082", "region": "CN", "version": "1.0",
                 "time": 1691486926}}
token_test = {"Authorization": json.dumps(Authorization_test)}

class RestClient:
    def __init__(self):
        self.logger = logger
        self.token_test = token_test
        self.test_url = test_url
    def get(self,url,  **kwargs):
        # logger.info("请求方式：{}".format(method))
        self.logger.debug("请求头：{}".format(self.token_test))
        self.logger.debug("请求参数：{}".format(json.dumps(kwargs)))
        self.logger.debug("请求地址：{}".format(self.test_url + url))
        self.logger.debug("返回结果：{}".format(requests.get(self.test_url + url,headers = self.token_test, **kwargs).json()))
        return requests.get(self.test_url + url,headers = self.token_test, **kwargs)

    def post(self,url, **kwargs):
        # logger.info("请求方式：{}".format(method))
        self.logger.debug("请求头：{}".format(self.token_test))
        self.logger.debug("请求参数：{}".format(json.dumps(kwargs)))
        self.logger.debug("请求地址：{}".format(self.test_url + url))
        self.logger.debug("返回结果：{}".format(requests.post(self.test_url + url, headers=self.token_test, **kwargs).json()))
        return requests.post(self.test_url + url,headers = self.token_test, **kwargs)



# import json
# from encodings.utf_7 import encode
#
# import requests
# from Tools.scripts.generate_opcode_h import header
#
# from utils.log_util import logger
#
# test_url = "https://test-admax.yostar.net"
# Authorization_test = {
#         "Head": {"token": "9f6ed40924488358990084e699901b35476de082", "region": "CN", "version": "1.0",
#                  "time": 1691486926}}
# token_test = {"Authorization": json.dumps(Authorization_test)}
#
# class RestClient:
#     def __init__(self):
#         self.token_test = token_test
#         self.test_url = test_url
#     def get(self,url,  **kwargs):
#         # return requests.get(self.test_url + url,headers = self.token_test, **kwargs)
#         return self.request(url,"GET", **kwargs)
#
#     def post(self,url,  **kwargs):
#         return self.request(url,"POST", **kwargs)
#
#     def request(self,url,method, **kwargs):
#
#         if method == "GET":
#             return requests.get(self.test_url + url,headers = self.token_test, **kwargs)
#
#         if method == "POST":
#             return requests.get(self.test_url + url,headers = self.token_test, **kwargs)
#         logger.info("请求方式：{}".format(method))
#         logger.info("请求头：{}".format(self.token_test))
#         logger.info("请求参数：\n{}".format(json.dumps(kwargs, indent=2)))
#         logger.info("请求地址：{}".format(self.test_url + url))
#         logger.info("返回结果：{}".format(
#             requests.request(method, self.test_url + url, headers=self.token_test, **kwargs).json()))

