import json

import pytest
import requests

# from 废弃文件.header import Test_headers

Test_headers = {
    'Authorization': '{"Head": {"Token": "{\\"uid\\":576,\\"uuid\\":\\"4fd0c2d9490a2bcd762325abc75fff114LgnrAF6rn5\\",\\"access_token\\":\\"eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI4NzM4NDI5LCJpYXQiOjE3Mjg0NzkyMjl9.vfzg_A28EBNhRCPrgNdYvIl6NEDl-Ykq80CzLHwv838\\",\\"refresh_token\\":\\"eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI5MDg0MDI5LCJpYXQiOjE3Mjg0NzkyMjl9.3GsiffDqzxTExSqKGMuKrR_AiOZbKDLj6qwE_ro0N6w\\"}", "Version": "v2.0", "ProjectId": "cqcu1oidf2vdu69hqkf0"}}',
    'Content-Type': 'application/json'}

headers = Test_headers
head = requests.session()
head.headers.update(
    headers
)


# setup_module/teardown_module:用于整个测试文件数据的前置准备和清理
# @pytest.fixture(autouse=True)
# def func():
#     print('我是前置步骤')


def test_Mbcx(get_data):
    '''
    查询母包校验
    '''
    url = "https://test-advertising.yostar.net/admax-packerapi/packer/original/list"
    # a = requests.post(url, data=json.dumps(data), headers=headers)
    Mbcx = head.post(url, data=json.dumps(get_data))
    print(Mbcx.json())
    assert Mbcx.json()["code"] == 200
    assert Mbcx.json()["msg"] == "OK"
    assert Mbcx.json()["data"]["list"][0]["id"] == 2
    assert Mbcx.json()["data"]["list"][0]["original_package_type"] == "official-lite"


def test_FBcx(get_data1):
    task_name = get_data1['task_name']
    print(task_name)
    '''
    查询分包校验
    '''
    url = "https://test-advertising.yostar.net/admax-packerapi/packer/task/list"
    data1 = {
        "task_name": task_name,
        "page": 1,
        "size": 10
    }
    # b = requests.post(url, data=json.dumps(data1), headers=headers)
    FBcx = head.request("POST", url, data=json.dumps(data1))
    assert FBcx.json()["code"] == 200
    assert FBcx.json()["msg"] == "OK"
    # 断言rr包含在返回值中
    assert "Test_44" in FBcx.json()["data"]["list"][0]["task_name"]
    assert FBcx.json()["data"]["list"][0]["task_name"] == "Test_44"
    print(FBcx.json())

def test_addMBerr(get_data2):
    '''
    新建母包时母包地址错误时，错误提示校验
    '''
    url = 'https://test-advertising.yostar.net/admax-packerapi/packer/original/max-version'

    addMBerr = head.post(url, data=json.dumps(get_data2))
    assert addMBerr.json()["code"] == 400000
    assert addMBerr.json()["msg"] == "请输入正确的oss地址"
    print(addMBerr.json())


if __name__ == '__main__':
    pytest.main()
