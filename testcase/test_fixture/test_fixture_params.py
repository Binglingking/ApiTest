import pytest
import requests
import json

# from 废弃文件.header import Test_headers

Test_headers = {
    'Authorization': '{"Head": {"Token": "{\\"uid\\":576,\\"uuid\\":\\"4fd0c2d9490a2bcd762325abc75fff114LgnrAF6rn5\\",\\"access_token\\":\\"eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI4NzM4NDI5LCJpYXQiOjE3Mjg0NzkyMjl9.vfzg_A28EBNhRCPrgNdYvIl6NEDl-Ykq80CzLHwv838\\",\\"refresh_token\\":\\"eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI5MDg0MDI5LCJpYXQiOjE3Mjg0NzkyMjl9.3GsiffDqzxTExSqKGMuKrR_AiOZbKDLj6qwE_ro0N6w\\"}", "Version": "v2.0", "ProjectId": "cqcu1oidf2vdu69hqkf0"}}',
    'Content-Type': 'application/json'}

headers = Test_headers
head = requests.session()
head.headers.update(
    headers
)


@pytest.fixture(params=[
    {
        "id": "4.0.1"
    },
    {
    "id": "4.0.2"
}],ids=['Mbcx','FBcx'])
def params_fixture(request):
    return request.param
def test_Mbcx(params_fixture):
    '''
    查询母包校验
    '''
    url = "https://test-advertising.yostar.net/admax-packerapi/packer/original/list"
    # a = requests.post(url, data=json.dumps(data), headers=headers)
    Mbcx = head.post(url, data=json.dumps(params_fixture))
    print(Mbcx.json())
    assert Mbcx.json()["code"] == 200
    assert Mbcx.json()["msg"] == "OK"
    assert Mbcx.json()["data"]["list"][0]["id"] == 2
    assert Mbcx.json()["data"]["list"][0]["original_package_type"] == "official-lite"







if __name__ == '__main__':
    pytest.main()
