import configparser
import os

import yaml

yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'oriModMain.yaml')
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config', 'AD_settings.ini')


class ReadOriModMain:
    def __init__(self):
        self.yaml_path = yaml_path
        self.ini_path = ini_path

    def read_yaml(self):
        f = open(self.yaml_path, encoding="utf-8")
        data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf-8')
        return config


base_data = ReadOriModMain()
# print(base_data.read_yaml())