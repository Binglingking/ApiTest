import pytest
import requests
import json

from utils.read_data import get_data
from config.header import TestHeaders
from utils import read_data

headers = TestHeaders().generate_headers()
session = requests.Session()
session.headers.update(headers)
# setup_function/teardown_function:用于每条测试数据的前置准备和清理

# def setup_function():
#     print("准备测试数据")
#
# def teardown_function():
#     print("清理测试数据")

# @pytest.allure.feature('查询母包')
@pytest.mark.parametrize('id', get_data(file_path="C:\\Users\Administrator\PycharmProjects\ApiTest\config\data.yaml")['id'])
@pytest.mark.p0
def test_Mbcx(id):
    url = "https://test-advertising.yostar.net/admax-packerapi/packer/original/list"
    data = {
      "id": id
    }
    # a = requests.post(url, data=json.dumps(data), headers=headers)
    aa = session.post(url, data=json.dumps(data))
    print(aa.json())
    assert aa.status_code == 200
    assert aa.json()["code"] == 200
    assert aa.json()["msg"] == "OK"
    assert aa.json()["data"]["list"][0]["id"] == 12
    assert aa.json()["data"]["list"][0]["original_package_type"] == "official"


# @pytest.allure.feature('查询分包计划')
@pytest.mark.parametrize('data1', get_data(file_path="C:\\Users\Administrator\PycharmProjects\ApiTest\config\data.yaml")['data1'])
@pytest.mark.p1
def test_FBcx(data1):
    url = "https://test-advertising.yostar.net/admax-packerapi/packer/task/list"
    data1 = data1
    # b = requests.post(url, data=json.dumps(data1), headers=headers)
    bb = session.request("POST", url, data=json.dumps(data1))
    assert bb.status_code == 200
    assert bb.json()["code"] == 200
    assert bb.json()["msg"] == "OK"
    # 断言rr包含在返回值中
    assert "rr" in bb.json()["data"]["list"][0]["task_name"]
    assert bb.json()["data"]["list"][0]["task_name"] == "Test_rr"
    print(bb.json())

if __name__ == '__main__':
    pytest.main()