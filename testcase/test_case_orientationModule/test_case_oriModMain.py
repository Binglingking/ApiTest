import allure
import pytest
import random
from api.oriMod_api import OriModApi
from testcase.test_case_optimize.AD_conftest import add_oriMod_id, edit_oriMod_id, copy_oriMod_id
from utils.AD_utils.AD_response_handler import handle_response
from utils.AD_utils.read_oriModMain import base_data
from config.AD_getTokenUI import get_token_from_ui

# ANSI转义序列用于控制台颜色输出
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"
YELLOW = "\033[93m"

def generate_random_model_name(prefix="Py_", action=None):
    random_number = random.randint(10, 99)  # 生成两位随机数
    name = f"{prefix}{random_number}"
    if action:
        TestAdmax_oriModMain.generated_names[action] = name
    return name

@allure.epic("ADMax-定向模块")
@allure.feature("定向模块主流程测试")
@allure.description("定向模块主流程测试流程：新增-编辑-复制-删除，并在每个操作后进行查询")
class TestAdmax_oriModMain:
    # 定义一部字典来保存生成的模板名称
    generated_names = {}

    @allure.story("定向模块新增")
    @allure.title("新增定向模块：pytest_add")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块新增地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=1)
    def test_add_oriMod(self):
        # 在用例执行前获取Token
        # print("开始获取Token...")
        # try:
        #     get_token_from_ui()
        #     print(f"Token获取成功")
        # except Exception as e:
        #     print(f"Token获取失败: {e}")
        #     pytest.exit("由于无法获取有效的Token，测试用例将不会执行。")

        data = base_data.read_yaml()['add_oriMod']
        data['model_name'] = generate_random_model_name("Py_add_", "add")
        result = OriModApi.add_orientationModule(data)
        handle_response(result)
    @allure.story("定向模块查询")
    @allure.title("查询上一步中新增的模块：pytest_add")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/list", "定向模块查询地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=2)
    def test_add_oriMod_Search(self):
        data = base_data.read_yaml()['add_oriMod_Search']
        data['model_name'] = self.generated_names["add"]
        result = OriModApi.oriMod_Search(data)
        assert result['data']['list'][0]['model_name'] == self.generated_names["add"]
        handle_response(result)

    @allure.story("定向模块编辑")
    @allure.title("编辑新增后的模板")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/addOrEdit", "定向模块编辑地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=3)
    def test_add_oriMod_Edit(self):
        add_id = add_oriMod_id()
        data = base_data.read_yaml()['add_oriMod_Edit']
        data['id'] = add_id
        data['model_name'] = generate_random_model_name("Py_edit_", "edit")
        result = OriModApi.add_orientationModule(data)
        handle_response(result)

    @allure.story("定向模块查询")
    @allure.title("查询编辑后的模板：py_Edit")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/list", "定向模块查询地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=4)
    def test_oriMod_Edit_Search(self):
        data = base_data.read_yaml()['oriMod_Edit_Search']
        result = OriModApi.oriMod_Search(data)
        assert result['data']['list'][0]['model_name'] == self.generated_names["edit"]
        handle_response(result)

    @allure.story("定向模块-复制")
    @allure.title("复制编辑后的模板：py_Edit——>copy_pyEdit")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/copy", "定向模块复制地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=5)
    def test_copy_oriMod(self):
        copy_id = edit_oriMod_id()
        data = base_data.read_yaml()['copy_oriMod']
        data['copy_id'] = copy_id
        data['model_name'] = generate_random_model_name("Py_copy_", "copy")
        result = OriModApi.copy_oriMod(data)
        handle_response(result)

    @allure.story("定向模块-查询")
    @allure.title("查询复制后的模板：copy_pyEdit")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/list", "定向模块查询地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=6)
    def test_copy_oriMod_Search(self):
        data = base_data.read_yaml()['copy_oriMod_Search']
        data['model_name'] = self.generated_names["copy"]
        result = OriModApi.oriMod_Search(data)
        assert result['data']['list'][0]['model_name'] == self.generated_names["copy"]
        handle_response(result)

    @allure.story("定向模块删除")
    @allure.title("删除新增/编辑/复制的模板模板数据，防止下次测试冲突")
    @allure.testcase("https://test-admax.yostar.net/api/orientationModule/delete", "定向模块删除地址")
    @allure.severity("blocker")  # 用例等级
    @pytest.mark.run(order=7)
    def test_del_oriMod(self):
        # 获取需要删除的模板 ID 列表
        del_ids = [edit_oriMod_id(), copy_oriMod_id()]
        for del_id in del_ids:
            data = base_data.read_yaml()['del_oriMod']
            data['id'] = del_id
            result = OriModApi.del_orientationModule(data)
            handle_response(result)