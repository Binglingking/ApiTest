import configparser
import os
path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'settings.ini')

def read_ini():
    config = configparser.ConfigParser()
    config.read(path,encoding='utf-8')
    return config

# get_ini = read_ini()
# print(read_ini()['host']['test_url'])



