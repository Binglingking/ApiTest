import json

import pytest
import requests
from utils.read_all import base_data


Test_headers = {
    'Authorization': '{"Head": {"Token": "{\\"uid\\":576,\\"uuid\\":\\"4fd0c2d9490a2bcd762325abc75fff114LgnrAF6rn5\\",\\"access_token\\":\\"eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI4OTE3NTk2LCJpYXQiOjE3Mjg2NTgzOTZ9.9HgfJhbkgEVR-Hq8Th3DeedzaaY8DtRyQ1cMiHf9_j4\\",\\"refresh_token\\":\\"eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI5MjYzMTk2LCJpYXQiOjE3Mjg2NTgzOTZ9.vs8X0D-7NIEFvSr85nZ3JaKp38yTTT4WPkp_oU0hJlc\\"}", "Version": "v2.0", "ProjectId": "cqcu1oidf2vdu69hqkf0"}}',
    'Content-Type': 'application/json'}

headers = Test_headers
head = requests.session()
head.headers.update(
    headers
)
url = base_data.read_ini()['host']['test_url']

@pytest.mark.parametrize("Mbcx_data", base_data.read_yaml()['Mbcx_data'])
def test_Mbcx(Mbcx_data):
    """
    查询母包校验
    """

    # a = requests.post(url, data=json.dumps(data), headers=headers)
    # Mbcx_data =get_yaml['Mbcx_data']
    Mbcx = head.post(url + '/admax-packerapi/packer/original/list', data=json.dumps(Mbcx_data))
    print(Mbcx.json())
    assert Mbcx.json()["code"] == 200
    assert Mbcx.json()["msg"] == "OK"
    assert Mbcx.json()["data"]["list"][0]["id"] == 2
    assert Mbcx.json()["data"]["list"][0]["original_package_type"] == "official-lite"
@pytest.mark.parametrize("FBcx_data", base_data.read_yaml()['FBcx_data'])
def test_FBcx(FBcx_data):
    """
    查询分包校验

    """

    FBcx = head.request("POST", url + "/admax-packerapi/packer/task/list", data=json.dumps(FBcx_data))
    if FBcx_data['task_name'] == 'Test_44':
        assert FBcx.json()["code"] == 200
        assert FBcx.json()["msg"] == "OK"
        assert FBcx.json()["data"]["list"][0]["task_name"] == "Test_44"
    elif FBcx_data['task_name'] == 'Test_111':
        assert FBcx.json()["code"] == 200
        assert FBcx.json()["msg"] == "OK"
        assert FBcx.json()["data"]["list"][0]["task_name"] == "Test_111"
    elif FBcx_data['task_name'] == 'Test_55':
        assert FBcx.json()["code"] == 200
        assert FBcx.json()["msg"] == "OK"
        assert FBcx.json()["data"]["paginate"]["total_number"] == 0
    print(FBcx.json())

@pytest.mark.parametrize("addMBerr_data", base_data.read_yaml()['addMBerr_data'])
def test_addMBerr(addMBerr_data):
    """
    新建母包时母包地址错误时，错误提示校验
    """
    url + '/admax-packerapi/packer/original/max-version'
    addMBerr = head.post(url + '/admax-packerapi/packer/original/max-version', data=json.dumps(addMBerr_data))
    print(addMBerr.json())
    assert addMBerr.json()["code"] == 400000
    assert addMBerr.json()["msg"] == "请输入正确的oss地址"
    print(addMBerr.json())


if __name__ == '__main__':
    pytest.main()
