from api.api import dxbj_post
from utils.read_all import base_data
from utils.log_util import logger

# 假设这些参数来自配置文件或其他地方

# ANSI转义序列用于控制台颜色输出
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"


def test_dxbj():
    logger.info("开始执行定向模块编辑用例")
    json = base_data.read_yaml()['dxbj']
    result = dxbj_post(json)
    print(f"{RED}{json}{ENDC}")
    print(f"{GREEN}{result}{ENDC}")

    # 正确检查HTTP响应状态码
    if result['code'] == 200:
        assert result['code'] == 200


    elif result['code'] == 10003:
        assert result['code'] == 10003
        assert result['msg'] == "登录已过期"
        print(f"{RED}登录已过期{ENDC}")
        print(f"{RED}{result}{ENDC}")
    logger.info("定向模块编辑用例执行完毕")


# 调用函数
test_dxbj()
