import pytest

from api.api import dxcx_get, dxbj_post, tfcx_get, adv_status_post
from utils.read_all import base_data

# ANSI转义序列用于控制台颜色输出
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"


@pytest.fixture(scope="module")
def get_data():
    print(f"{GREEN}开始执行用例{ENDC}")
    yield
    print(f"{GREEN}用例执行完毕{ENDC}")


def test_dxbj(get_data):
    json = base_data.read_yaml()['dxbj']
    result = dxbj_post(json)
    print(f"{GREEN}{result}{ENDC}")

    # 正确检查HTTP响应状态码
    if result['code'] == 200:
        assert result['code'] == 200


    elif result['code'] == 10003:
        assert result['code'] == 10003
        assert result['msg'] == "登录已过期"
        print(f"{RED}登录已过期{ENDC}")
        # 如果需要进一步检查响应体的内容，可以在这里添加
        print(f"{RED}{result}{ENDC}")


# 调用函数
test_dxbj(get_data)
def test_dxcx(get_data):
    params = base_data.read_yaml()['dxcx']
    result = dxcx_get(params)

    # 正确检查HTTP响应状态码
    if result['code'] == 200:
        assert result['code'] == 200
        assert result['data']['list'][0]['model_name'] == "自动化pytest"
        print(f"{GREEN}{result}{ENDC}")

    elif result['code'] == 10003:
        assert result['code'] == 10003
        assert result['msg'] == "登录已过期"
        print(f"{RED}登录已过期{ENDC}")
        # 如果需要进一步检查响应体的内容，可以在这里添加
        print(f"{RED}{result}{ENDC}")

def test_dxcx1():
    params = base_data.read_yaml()['dxcx1']
    result = dxcx_get(params)

    # 正确检查HTTP响应状态码
    if result['code'] == 200:
        assert result['code'] == 200
        assert result['data']['list'][0]['model_name'] == "12.12"
        print(f"{GREEN}{result}{ENDC}")

    elif result['code'] == 10003:
        assert result['code'] == 10003
        assert result['msg'] == "登录已过期"
        print(f"{RED}登录已过期{ENDC}")
        # 如果需要进一步检查响应体的内容，可以在这里添加
        print(f"{RED}{result}{ENDC}")
def test_adv_status(get_data):
    json = base_data.read_yaml()['adv_status']
    result = adv_status_post(json)
    print(f"{GREEN}{result}{ENDC}")

    # 正确检查HTTP响应状态码
    if result['code'] == 200:
        assert result['code'] == 200


    elif result['code'] == 10003:
        assert result['code'] == 10003
        assert result['msg'] == "登录已过期"
        print(f"{RED}登录已过期{ENDC}")
        # 如果需要进一步检查响应体的内容，可以在这里添加
        print(f"{RED}{result}{ENDC}")

def test_tfcx():
    params = base_data.read_yaml()['tfcx']
    result = tfcx_get(params)

    # 正确检查HTTP响应状态码
    if result['code'] == 200:
        assert result['code'] == 200
        assert result['data']['list'][0]['adv_name'] == "悠星-BA-巨量-自-赛铂-OB-iOS-26"
        assert result['data']['list'][0]['agent'] == '赛铂'
        print(f"{GREEN}{result}{ENDC}")

    elif result['code'] == 10003:
        assert result['code'] == 10003
        assert result['msg'] == "登录已过期"
        print(f"{RED}登录已过期{ENDC}")
        # 如果需要进一步检查响应体的内容，可以在这里添加
        print(f"{RED}{result}{ENDC}")
# 调用函数
test_dxcx(get_data)
