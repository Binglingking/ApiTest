import os

import yaml

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'data.yaml')
# print(path)
def read_yaml():
    f = open(path, encoding="utf-8")
    data = yaml.safe_load(f)
    return data

get_yaml = read_yaml()
print(get_yaml)