# import pytest
#
#
# @pytest.fixture(scope='session',autouse=True)
# def test_session():
#     print('我是session级别的fixture')
#
# @pytest.fixture(scope='function',autouse=True)
# def test_func1():
#     print('我是func1级别的fixture')
#
# @pytest.fixture(scope='function',autouse=True)
# def test_func2():
#     print('我是func2级别的fixture')