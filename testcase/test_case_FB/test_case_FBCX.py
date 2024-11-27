import allure
import pytest
import random
from api.FB_Api import FBApi
from testcase.test_case_FB.FB_conftest import dl_task_id
from utils.FB_utils.FB_response_handler import FB_handle_response
from utils.FB_utils.read_FBdata import base_data

# ANSI转义序列用于控制台颜色输出
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"
YELLOW = "\033[93m"


def generate_random_task_name_with_channel(channel):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    random_chars = ''.join(random.choice(letters) for _ in range(5))
    return f"Py_add_{channel}_{random_chars}"


def generate_random_version():
    major = random.randint(1, 9)
    minor = random.randint(0, 9)
    patch = random.randint(0, 99)
    return f"{major}.{minor}.{patch}"


def generate_random_suffix(channel):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    suffix = ''.join(random.choice(letters) for _ in range(5))
    return f"{channel}{suffix}"


@allure.epic("分包工具-分包管理")
@allure.feature("分包管理主流程测试")
@allure.description("分包管理主流程测试流程：新增-查询-编辑-删除，并在每个操作后进行查询")
class TestFBCX:
    # 定义一个列表来保存生成的任务名称
    generated_task_names = []

    @allure.story("新增分包计划")
    @allure.title("新增分包计划：py_add")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.parametrize("ad_channel", [
        "Weibo", "OceanEngine", "Tencent", "Taptap", "BaiduSearch", "BaiduFeed",
        "BaiduBrand", "Zhihu", "UC", "360", "Iqiyi", "Hundred", "Official",
        "haiyoukuaibao", "mumu"
    ])  # 新增所有渠道计划  # 新增所有渠道计划
    @pytest.mark.parametrize("original_package_type", ["official", "official-lite"])
    @pytest.mark.run(order=1)
    def test_add_task_valid(self, ad_channel, original_package_type):
        data = base_data.read_yaml()['add_task']['valid_list'][0].copy()
        task_name = generate_random_task_name_with_channel(ad_channel)
        data['task_name'] = task_name
        data['ad_channel'] = ad_channel
        data['original_package_version'] = generate_random_version()
        data['original_package_type'] = original_package_type
        data['package_id_suffix'] = generate_random_suffix(ad_channel)
        result = FBApi.add_task(data)
        FB_handle_response(result)
        assert result['code'] == 200, f"添加失败: {result}"
        # 保存生成的 task_name
        self.generated_task_names.append(task_name)

    @allure.story("查询分包计划")
    @allure.title("查询上一步中新增的分包计划：pytest_add")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/list", "查询分包计划地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=2)
    def test_list_tasks_valid(self):
        for task_name in self.generated_task_names:
            data = base_data.read_yaml()['list_tasks']['valid'].copy()
            data['task_name'] = task_name
            result = FBApi().list_tasks(data)
            assert result['code'] == 200, f"查询失败: {result}"
            FB_handle_response(result)

    # @allure.story("更新分包计划")
    # @allure.title("更新分包计划：pytest_edit")
    # @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/update", "更新分包计划地址")
    # @allure.severity("blocker")  # 用例等级
    # @pytest.mark.run(order=5)
    # def test_update_task_valid(self):
    #     data = base_data.read_yaml()['update_task']['valid']
    #     result = FBApi().update_task(data)
    #     FB_handle_response(result)

    @allure.story("删除分包计划-批量删除")
    @allure.title("删除分包计划-批量删除")
    @allure.testcase("https://test-advertising.yostar.net/admax-packerapi/packer/task/delete", "删除分包计划地址")
    @allure.severity("critical")  # 用例等级
    @pytest.mark.parametrize("task_id_dict", dl_task_id())
    @pytest.mark.run(order=3)
    def test_delete_task_invalid(self,task_id_dict):
        data = base_data.read_yaml()['delete_task']['valid']
        data['task_id'] = task_id_dict["task_id"]
        result = FBApi().delete_task(data)
        FB_handle_response(result)