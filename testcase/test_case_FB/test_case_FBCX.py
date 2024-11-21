
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
    random_number = random.randint(0, 9999)  # 生成随机数
    name = f"{prefix}{random_number}"
    if action:
        TestFBCX.generated_names[action] = name
    return name


@allure.epic("分包工具-分包管理")
@allure.feature("分包管理主流程测试")
@allure.description("分包管理主流程测试流程：新增-查询-编辑-删除，并在每个操作后进行查询")
class TestFBCX:
    # 定义一个字典来保存生成的任务名称
    generated_names = {}
    task_id = None

    @allure.story("新增分包计划")
    @allure.title("新增分包计划：pytest_add")
    # @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/add", "新增分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=1)
    def test_add_task_valid(self):
        data = base_data.read_yaml()['add_task']['valid']
        data['task_name'] = generate_random_task_name("Py_add_", "add")
        result = FBApi.add_task(data)
        # assert result['code'] == 200
        FB_handle_response(result)

    @allure.story("查询分包计划")
    @allure.title("查询上一步中新增的分包计划：pytest_add")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/list", "查询分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=2)
    def test_list_tasks_valid(self):
        data = base_data.read_yaml()['list_tasks']['valid']
        data['task_name'] = self.generated_names["add"]
        result = FBApi().list_tasks(data)
        self.task_id = result['data']['list'][0]['task_id']
        print(self.task_id)
        print(result)
        assert result['data']['list'][0]['task_name'] == self.generated_names["add"]
        FB_handle_response(result)

    @allure.story("删除分包计划")
    @allure.title("删除分包计划：pytest_delete")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/delete", "删除分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=3)
    def test_delete_task_valid(self):
        data = base_data.read_yaml()['delete_task']['valid']
        data['task_id']  = self.task_id
        print('task_id参数:',data)
        result = FBApi().delete_task(data)
        FB_handle_response(result)

    @allure.story("删除分包计划-批量删除")
    @allure.title("删除分包计划-批量删除")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/delete", "删除分包计划地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("data", base_data.read_yaml()['delete_task']['valid_list'])
    def test_delete_task_invalid(self, data):
        result = FBApi().delete_task(data)
        FB_handle_response(result)
