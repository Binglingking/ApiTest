import pytest


@pytest.fixture(scope='session',autouse=True)
def test_session():
    print('我是session级别的fixture')

@pytest.fixture(scope='function')
def test_func1():
    print('我是func1级别的fixture')

@pytest.fixture(scope='function')
def test_func2():
    print('我是func2级别的fixture')

@pytest.fixture(scope='function')
def get_data():
    data = {
        "id": "4.0.2"
    }
    return data

@pytest.fixture(scope='function')
def get_data1():
    data1 = {
        "task_name": "Test_44",
        "page": 1,
        "size": 10
    }
    return data1

@pytest.fixture(scope='function')
def get_data2():
    data2 = {
        "package_type": "official",
        "package_url": "111"
    }
    return data2

@pytest.fixture(scope='function',autouse=True)
def func():
    print('我是前置步骤')
    yield
    print('我是后置步骤')

@pytest.fixture(scope='function')
def use_usefixture():
    print('我是usefixture')

@pytest.fixture(scope='function')
def use_usefixture1():
    print('我是usefixture1')