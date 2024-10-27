from pickle import FALSE

import allure
import pytest

from api import api
from api.api import Api
from testcase.test_case_optimize.conftest import get_orientation_module_id
from utils.read_all import base_data

# ANSI转义序列用于控制台颜色输出

RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"


@allure.epic("pytest学习：ADmax实战演练")
@allure.feature("定向模块和投放账号部分接口")
class TestAdmax:

    @pytest.fixture(scope="module", autouse=FALSE)
    def get_data(self):
        print(f"{GREEN}开始执行用例{ENDC}")
        yield
        print(f"{GREEN}用例执行完毕{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.story("投放账号查询")
    @allure.title("投放账号查询-悠星-BA-巨量-自-赛铂-OB-iOS-26")
    def test_tfcx(self):
        params = base_data.read_yaml()['tfcx']
        result = Api.tfcx_get(params)

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
    # test_dxcx(get_data)
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.story("新建定向模板")
    @allure.title("新建定向模版-pytest新建")
    def test_add_orientationModule(self):
        params = base_data.read_yaml()['add_orientationModule']
        result = Api.add_orientationModule(params)

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200

            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{RED}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{RED}{result}{ENDC}")

    @allure.story("定向模块编辑")
    @allure.title("定向模块编辑-pytest_mysql")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.issue("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑缺陷问题")
    @allure.description("定向模块编辑-自动化pytest详细用力信息")
    @allure.step("操作步骤")
    @allure.severity("blocker")
    def test_dxbj(self):
        allure.dynamic.story()
        json = base_data.read_yaml()['dxbj']
        result = Api.dxbj_post(json)
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
    # test_dxbj(get_data)
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.story("定向模块查询")
    @allure.title("定向模块查询-pytest_sql")
    def test_dxcx(self):
        params = base_data.read_yaml()['dxcx']
        result = Api.dxcx_get(params)

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            assert result['data']['list'][0]['model_name'] == "pytest_sql"
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{RED}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{RED}{result}{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.story("定向模块")
    @allure.title("定向模块删除-pytest_sql")
    def test_del_orientationModule(self):
        # params = base_data.read_yaml()['del_orientationModule']
        del_id  = get_orientation_module_id()
        params = {
            "channel_id": "OceanEngine",
            "id": del_id
        }
        # print(params)
        result = Api.del_orientationModule(params)

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            # assert result['data']['list'][0]['model_name'] == "pytest_sql"
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{RED}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{RED}{result}{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.story("定向查询1")
    @allure.title("定向查询1-自动化pytest")
    def test_dxcx1(self):
        params = base_data.read_yaml()['dxcx1']
        result = Api.dxcx_get(params)

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

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.story("投放账号状态开启")
    @allure.title("投放账号状态开启-title")
    def test_adv_status(self):
        json = base_data.read_yaml()['adv_status']
        result = Api.adv_status_post(json)
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


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir=./allure-results', 'test_post_get_optimize_class.py'])
