import pytest
import requests
import json

from Tools.scripts.generate_opcode_h import header

from 废弃文件.header import TestHeaders




headers = TestHeaders.generate_headers(header)
h = requests.session()
h.headers.update(
    headers
)

@pytest.mark.p0
def test_Mbcx():

    url = "https://test-advertising.yostar.net/admax-packerapi/packer/original/list"
    data = {
      "id": "1"
    }
    a = requests.post(url, data=json.dumps(data), headers=headers)
    # aa = h.post(url, data=json.dumps(data))
    print(a.json())
    assert a.status_code == 200
    assert a.json()["code"] == 200
    assert a.json()["msg"] == "OK"
    assert a.json()["data"]["list"][0]["id"] == 12
    assert a.json()["data"]["list"][0]["original_package_type"] == "official"

@pytest.mark.p1
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
    b = requests.post(url, data=json.dumps(data1), headers=headers)
    # bb = h.request("POST", url, data=json.dumps(data1))
    assert b.status_code == 200
    assert b.json()["code"] == 200
    assert b.json()["msg"] == "OK"
    # 断言rr包含在返回值中
    assert "rr" in b.json()["data"]["list"][0]["task_name"]
    assert b.json()["data"]["list"][0]["task_name"] == "Test_rr"
    print(b.json())

if __name__ == '__main__':
    pytest.main()