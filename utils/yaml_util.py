from faker import Faker

# i = 11
# for a in str(i):

fake = Faker(locale='zh_CN')



def fuc_yaml(get_yaml1):
    if isinstance(get_yaml1, dict):
        for key, value in get_yaml1.items():
            if '${' and '}' in str(value):
                start = str(value).index('${')
                end = str(value).index('}')
                fuv_name = str(value)[start + 2:end]
                get_yaml1[key] = str(value)[0:start] + str(eval(fuv_name))+str((value)[end+1:len(str(value))])
    return get_yaml1


def random_name():
    return fake.name()


def age():
    return fake.random_int(min=18, max=60)


def sex():
    return fake.random_element(elements=('男', '女'))


if __name__ == '__main__':
    get_yaml1 = {'name': '上海-${random_name()}-测试', 'age': '${age()}', 'sex': '${sex()}'}
    # print(fuc_yaml(get_yaml1))
