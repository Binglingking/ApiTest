import pytest
import requests
import json
from 废弃文件.header import Test_headers




headers = Test_headers
h = requests.session()
h.headers.update(
    headers
)






class Test_class:

    # setup_class/teardown_class:用于类级的测试数据准备与清理，只在类中执行一次
    def setup_class(self):
        print("准备测试数据")

    def teardown_class(self):
        print("清理测试数据")

    def test_Mbcx(self):

        url = "https://test-advertising.yostar.net/admax-packerapi/packer/original/list"
        data = {
          "id": "1"
        }
        # a = requests.post(url, data=json.dumps(data), headers=headers)
        aa = h.post(url, data=json.dumps(data))
        print(aa.json())
        assert aa.status_code == 200
        assert aa.json()["code"] == 200
        assert aa.json()["msg"] == "OK"
        assert aa.json()["data"]["list"][0]["id"] == 12
        assert aa.json()["data"]["list"][0]["original_package_type"] == "official"
    def test_FBcx(self):
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
        bb = h.request("POST", url, data=json.dumps(data1))
        assert bb.status_code == 200
        assert bb.json()["code"] == 200
        assert bb.json()["msg"] == "OK"
        # 断言rr包含在返回值中
        assert "rr" in bb.json()["data"]["list"][0]["task_name"]
        assert bb.json()["data"]["list"][0]["task_name"] == "Test_rr"
        print(bb.json())

    if __name__ == '__main__':
        pytest.main()