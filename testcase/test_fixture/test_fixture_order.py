import pytest


@pytest.fixture(scope='session')
def session_fixture():
    print('我是session_fixture')


@pytest.fixture(scope='module')
def module_fixture():
    print('我是module_fixture')


@pytest.fixture(scope='class')
def class_fixture():
    print('我是class_fixture')


@pytest.fixture(scope='function')
def func_fixture():
    print('我是func_fixture')


class TestOrder:
    def test_1(self, class_fixture, func_fixture, session_fixture, module_fixture, ):
        assert 1 == 1
