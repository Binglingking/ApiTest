from api.api import dxcx_get
from utils.read_all import base_data

# 假设这些参数来自配置文件或其他地方

# ANSI转义序列用于控制台颜色输出
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"


def test_dxcx():
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


# 调用函数
test_dxcx()
