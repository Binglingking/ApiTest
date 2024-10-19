# import json
#
# import requests
#
# test_url = "https://test-admax.yostar.net"
# Authorization_test = {
#         "Head": {"token": "9f6ed40924488358990084e699901b35476de082", "region": "CN", "version": "1.0",
#                  "time": 1691486926}}
# token_test = {"Authorization": json.dumps(Authorization_test)}
#
# data = {
#     "name": "test_name",
#     "age": 18,
#     "sex": "男"
# }
import sys
import allure
import pytest

# 打印 sys.path，用于调试
print("sys.path:", sys.path)

# 打印 allure 模块的路径，用于调试
print(f"allure module path: {allure.__file__}")

# 打印 allure 模块的内容，用于调试
print(f"allure module contents: {dir(allure)}")

@allure.epic("pytest学习：ADmax实战演练")
class TestPostGetOptimizeClass:

    @allure.feature("POST请求优化")
    def test_post_request(self):
        # 测试代码
        assert True

    @allure.feature("GET请求优化")
    def test_get_request(self):
        # 测试代码
        assert True

if __name__ == '__main__':
    pytest.main(['-v', '-s', '--alluredir=./allure-results'])
