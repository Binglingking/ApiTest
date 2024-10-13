import pytest
import requests
import json

from 废弃文件.header import TestHeaders

headers = TestHeaders().generate_headers()
session = requests.Session()
session.headers.update(headers)
# setup_function/teardown_function:用于每条测试数据的前置准备和清理

def setup_function():
    print("准备测试数据")

def teardown_function():
    print("清理测试数据")

def test_Mbcx():

    url = "https://test-advertising.yostar.net/admax-packerapi/packer/original/list"
    data = {
      "id": "1"
    }
    # a = requests.post(url, data=json.dumps(data), headers=headers)
    aa = session.post(url, data=json.dumps(data))
    print(aa.json())
    assert aa.status_code == 200
    assert aa.json()["code"] == 200
    assert aa.json()["msg"] == "OK"
    assert aa.json()["data"]["list"][0]["id"] == 12
    assert aa.json()["data"]["list"][0]["original_package_type"] == "official"
def test_FBcx():
    url = "https://test-advertising.yostar.net/admax-packerapi/packer/task/list"
    data1 = {
        "task_name": "rr",
        "task_status": 1,
        "original_package_type": "",
        "package_version": "",
        "ad_channel": "",
        "page": 1,
        "size": 10
    }
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