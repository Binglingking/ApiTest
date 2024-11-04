# D:\ApiTest\testcase\test_case_FB\test_case_FBMain.py
import allure
import pytest
import random
from api.FB_Api import FBApi
from utils.FB_utils.FB_response_handler import FB_handle_response
from utils.FB_utils.read_FBdata import base_data

# ANSI转义序列用于控制台颜色输出
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"
YELLOW = "\033[93m"

def generate_random_task_name(prefix="Py_", action=None):
    random_number = random.randint(10, 99)  # 生成两位随机数
    name = f"{prefix}{random_number}"
    if action:
        TestFBMain.generated_names[action] = name
    return name

@allure.epic("分包工具-分包管理")
@allure.feature("分包管理主流程测试")
@allure.description("分包管理主流程测试流程：新增-查询-编辑-删除，并在每个操作后进行查询")
class TestFBMain:
    # 定义一个字典来保存生成的任务名称
    generated_names = {}

    @allure.story("新增⺟包版本")
    @allure.title("新增⺟包版本：pytest_add")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/original/add", "新增⺟包版本地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=1)
    def test_add_original_package_valid(self):
        data = base_data.read_yaml()['add_original_package']['valid']
        result = FBApi().add_original_package(data)
        FB_handle_response(result)

    @allure.story("新增⺟包版本-异常场景")
    @allure.title("新增⺟包版本-异常场景")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/original/add", "新增⺟包版本地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("data", base_data.read_yaml()['add_original_package']['invalid'])
    def test_add_original_package_invalid(self, data):
        result = FBApi().add_original_package(data)
        FB_handle_response(result, expected_code=400)

    @allure.story("查询⺟包列表")
    @allure.title("查询上一步中新增的⺟包：pytest_add")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/original/list", "查询⺟包列表地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=2)
    def test_list_original_packages_valid(self):
        data = base_data.read_yaml()['list_original_packages']['valid']
        result = FBApi().list_original_packages(data)
        if data.get('Test_11'):
            assert result['data']['info']['original_package_id'] == 5
        else:
            FB_handle_response(result)

    @allure.story("查询⺟包列表-异常场景")
    @allure.title("查询⺟包列表-异常场景")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/original/list", "查询⺟包列表地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("data", base_data.read_yaml()['list_original_packages']['invalid'])
    def test_list_original_packages_invalid(self, data):
        result = FBApi().list_original_packages(data)
        if data.get('unauthorized'):
            FB_handle_response(result, expected_code=401)
        else:
            FB_handle_response(result, expected_code=400)

    @allure.story("新增分包计划")
    @allure.title("新增分包计划：pytest_add")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/add", "新增分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=3)
    def test_add_task_valid(self):
        data = base_data.read_yaml()['add_task']['valid']
        data['task_name'] = generate_random_task_name("Py_add_", "add")
        result = FBApi().add_task(data)
        FB_handle_response(result)

    @allure.story("新增分包计划-异常场景")
    @allure.title("新增分包计划-异常场景")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/add", "新增分包计划地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("data", base_data.read_yaml()['add_task']['invalid'])
    def test_add_task_invalid(self, data):
        result = FBApi().add_task(data)
        if data.get('unauthorized'):
            FB_handle_response(result, expected_code=401)
        else:
            FB_handle_response(result, expected_code=400)

    @allure.story("查询分包计划")
    @allure.title("查询上一步中新增的分包计划：pytest_add")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/list", "查询分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=4)
    def test_list_tasks_valid(self):
        data = base_data.read_yaml()['list_tasks']['valid']
        # data['task_name'] = self.generated_names["add"]
        result = FBApi().list_tasks(data)
        if data.get('Test_11'):
            assert result['data']['list'][0]['task_name'] == 'Test_11'
        else:
            FB_handle_response(result)

    @allure.story("查询分包计划-异常场景")
    @allure.title("查询分包计划-异常场景")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/list", "查询分包计划地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("data", base_data.read_yaml()['list_tasks']['invalid'])
    def test_list_tasks_invalid(self, data):
        result = FBApi().list_tasks(data)
        if data.get('unauthorized'):
            FB_handle_response(result, expected_code=401)
        else:
            FB_handle_response(result, expected_code=400)

    @allure.story("更新分包计划")
    @allure.title("更新分包计划：pytest_edit")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/update", "更新分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=5)
    def test_update_task_valid(self):
        data = base_data.read_yaml()['update_task']['valid']
        result = FBApi().update_task(data)
        FB_handle_response(result)

    @allure.story("更新分包计划-异常场景")
    @allure.title("更新分包计划-异常场景")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/update", "更新分包计划地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("data", base_data.read_yaml()['update_task']['invalid'])
    def test_update_task_invalid(self, data):
        result = FBApi().update_task(data)
        if data.get('unauthorized'):
            FB_handle_response(result, expected_code=401)
        elif data.get('already_updated'):
            FB_handle_response(result, expected_code=401)
        else:
            FB_handle_response(result, expected_code=401)

    @allure.story("删除分包计划")
    @allure.title("删除分包计划：pytest_delete")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/delete", "删除分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=6)
    def test_delete_task_valid(self):
        data = base_data.read_yaml()['delete_task']['valid']
        result = FBApi().delete_task(data)
        FB_handle_response(result)

    @allure.story("删除分包计划-异常场景")
    @allure.title("删除分包计划-异常场景")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/delete", "删除分包计划地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("data", base_data.read_yaml()['delete_task']['invalid'])
    def test_delete_task_invalid(self, data):
        result = FBApi().delete_task(data)
        if data.get('unauthorized'):
            FB_handle_response(result, expected_code=401)
        else:
            FB_handle_response(result, expected_code=400)