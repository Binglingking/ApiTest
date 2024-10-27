import allure
import pytest

from api.oriMod_api import OriModApi
from testcase.test_case_optimize.conftest import edit_oriMod_id, add_oriMod_id
from utils.read_oriModMain import base_data

# ANSI转义序列用于控制台颜色输出

RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"
YELLOW = "\033[93m"


@allure.epic("ADMax-定向模块")
@allure.feature("定向模块主流程测试")
@allure.description("定向模块主流程测试流程：新增-编辑-复制-删除，并在每个操作后进行查询")
class TestAdmax_oriModMain:
    """
    定向模块主流程测试流程：
    新增-编辑-复制-删除，并在每个操作后进行查询
    """

    # @pytest.fixture(scope="module", autouse=FALSE)
    # def get_data(self):
    #     print(f"{GREEN}开始执行用例{ENDC}")
    #     yield
    #     print(f"{GREEN}用例执行完毕{ENDC}")

    @allure.story("定向模块新增")
    @allure.title("新增定向模块：pytest_add")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块新增地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=1)
    def test_add_oriMod(self,):
        data = base_data.read_yaml()['add_oriMod']
        result = OriModApi.add_orientationModule(data)

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{RED}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{YELLOW}{result}{ENDC}")

    @allure.story("定向模块查询")
    @allure.title("查询上一步中新增的模块：pytest_add")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/list", "定向模块查询地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=2)
    def test_add_oriMod_Search(self):
        data = base_data.read_yaml()['add_oriMod_Search']
        result = OriModApi.oriMod_Search(data)
        model_name = base_data.read_yaml()['add_oriMod']['model_name']

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            assert result['data']['list'][0]['model_name'] == model_name
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{RED}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{RED}{result}{ENDC}")

    @allure.story("定向模块编辑")
    @allure.title("编辑新增后的模板")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=3)
    def test_add_oriMod_Edit(self):
        add_id = add_oriMod_id()
        data = base_data.read_yaml()['add_oriMod_Edit']
        data['id'] = add_id
        # data['content']['id'] = add_id
        result = OriModApi.add_oriMod_Edit(data)

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            print(f"{GREEN}{result}{ENDC}")



        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{YELLOW}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
        else:
            print(f"{RED}未知错误:{ENDC}")
            print(f"{RED}{result}{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/list", "定向查询地址")
    @allure.story("定向模块查询")
    @allure.title("查询编辑后的模板：py_Edit")
    @pytest.mark.run(order=4)
    def test_oriMod_Edit_Search(self):
        data = base_data.read_yaml()['oriMod_Edit_Search']
        result = OriModApi.oriMod_Search(data)
        model_name2 = base_data.read_yaml()['add_oriMod_Edit']['model_name']

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            assert result['data']['list'][0]['model_name'] == model_name2
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{YELLOW}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{YELLOW}{result}{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/copy", "定向模块复制地址")
    @allure.story("定向模块-复制")
    @allure.title("复制编辑后的模板：py_Edit——>copy_pyEdit")
    @pytest.mark.run(order=5)
    def test_copy_oriMod(self):
        copy_id = edit_oriMod_id()
        data = base_data.read_yaml()['copy_oriMod']
        data['copy_id'] = copy_id
        result = OriModApi.copy_oriMod(data)


        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{YELLOW}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{YELLOW}{result}{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/list", "定向模块查询地址")
    @allure.story("定向模块-查询")
    @allure.title("查询复制后的模板：copy_pyEdit")
    @pytest.mark.run(order=6)
    def test_copy_oriMod_Search(self):
        data = base_data.read_yaml()['copy_oriMod_Search']
        result = OriModApi.oriMod_Search(data)
        model_name1 = base_data.read_yaml()['copy_oriMod']['model_name']

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            assert result['data']['list'][0]['model_name'] == model_name1
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{YELLOW}登录已过期{ENDC}")
            # 如果需要进一步检查响应体的内容，可以在这里添加
            print(f"{YELLOW}{result}{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/delete", "定向模块删除地址")
    @allure.story("定向模块删除")
    @allure.title("删除编辑后的模板：py_Edit")
    @pytest.mark.run(order=7)
    def test_del_oriMod(self):
        del_id = edit_oriMod_id()
        data = base_data.read_yaml()['del_oriMod']
        data['id'] = del_id
        result = OriModApi.del_orientationModule(data)

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{YELLOW}登录已过期{ENDC}")
            print(f"{YELLOW}{result}{ENDC}")

    @allure.testcase("https://test-admax.yostar.net/api/channelAdv/list", "定向模块查询地址")
    @allure.story("定向查询")
    @allure.title("定向查询1:查询删除的py_Edit模板是否还存在")
    @pytest.mark.run(order=8)
    def test_del_oriMod_Search(self):
        data = base_data.read_yaml()['oriMod_Edit_Search']
        result = OriModApi.oriMod_Search(data)

        # 正确检查HTTP响应状态码
        if result['code'] == 200:
            assert result['code'] == 200
            assert result['data']['list'] == []
            print(f"{GREEN}{result}{ENDC}")

        elif result['code'] == 10003:
            assert result['code'] == 10003
            assert result['msg'] == "登录已过期"
            print(f"{YELLOW}登录已过期{ENDC}")
            print(f"{YELLOW}{result}{ENDC}")


if __name__ == '__main__':
    pytest.main(['-s', '--alluredir=./allure-results', 'test_case_oriModMain.py'])
