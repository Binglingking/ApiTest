
import configparser
import os
import yaml

yaml_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'fb_data.yaml')
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config', 'settings.ini')

class ReadFBData:
    def __init__(self):
        self.ini_path = ini_path
        self.yaml_path = yaml_path

    def read_yaml(self):
        with open(self.yaml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf-8')
        return config

base_data = ReadFBData()
print(ini_path)