import pytest


@pytest.mark.parametrize('name', ['张顺', '万晶晶'])
def test_parametrize_01(name):
    print('我是' + name)
