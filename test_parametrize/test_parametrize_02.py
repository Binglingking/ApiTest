import pytest

# 测试数据可以从外部文件读取，这里简化处理
test_data = [
    ('张顺', '一个亿'),
    ('万晶晶', '一千万')
]

@pytest.mark.parametrize('name,money', test_data)
def test_parametrize_02(name, money):
    # 使用 f-string 改进日志输出
    print(f'我是{name}，我的余额是{money}')

    # 修正断言
    if name == '张顺':
        assert money == '一个亿'
    elif name == '万晶晶':
        assert money == '一千万'
