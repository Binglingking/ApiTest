import json
import requests
from utils.log_util import logger

# 测试环境的URL
test_url = "https://test-advertising.yostar.net"
UAT_url = 'https://staging-advertising.yostar.net'

access_token = "eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI1Nzg1NTM2LCJpYXQiOjE3MjU1MjYzMzZ9.pyZ6fkqL7VcBbwNb8mEQJ0ET40DMU4z5Oc52mnLI76I"
refresh_token = "111111111nYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI2MTMxMTM2LCJpYXQiOjE3MjU1MjYzMzZ9.uSVmVl8UZ4e4hJOuehQu0AEhaEXAaYWb9tzoqCqmOSE"
project_id = "1cqbltdqdf2vdu69hqkbg"

# 更新后的 Test_headers
Test_headers = {
    "Authorization": (
            '{"Head":{"Token":"{\\"access_token\\":\\"' + access_token + '\\",'
                                                                         '\\"refresh_token\\":\\"' + refresh_token + '\\",'
                                                                                                                     '\\"uid\\":576}","Version":"v2.0","ProjectId":"' + project_id + '"}}'
    ),
    "Content-Type": "application/json"
}

# print(Test_headers)
# 将授权信息转换为请求头格式
token_test = Test_headers


# print(token_test)
class RestClient:
    """
    RestClient 类用于封装HTTP请求，提供GET和POST方法。
    """

    def __init__(self):
        """
        初始化 RestClient 实例，设置日志记录器、授权信息和测试URL。
        """
        self.logger = logger
        self.token_test = token_test
        self.test_url = test_url

    def get(self, url, **kwargs):
        """
        发送GET请求。

        :param url: 请求的URL路径
        :param kwargs: 其他请求参数
        :return: 响应对象
        """
        self.logger.debug("请求头：{}".format(self.token_test))
        self.logger.debug("请求参数：{}".format(json.dumps(kwargs)))
        self.logger.debug("请求地址：{}".format(self.test_url + url))

        response = requests.get(self.test_url + url, headers=self.token_test, **kwargs)
        self.logger.debug("返回结果：{}".format(response.json()))

        return response

    def post(self, url, **kwargs):
        """
        发送POST请求。

        :param url: 请求的URL路径
        :param kwargs: 其他请求参数
        :return: 响应对象
        """
        self.logger.debug("请求头：{}".format(self.token_test))
        self.logger.debug("请求参数：{}".format(json.dumps(kwargs)))
        self.logger.debug("请求地址：{}".format(self.test_url + url))

        response = requests.post(self.test_url + url, headers=self.token_test, **kwargs)
        self.logger.debug("返回结果：{}".format(response.json()))

        return response

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
