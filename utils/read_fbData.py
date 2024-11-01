# D:\ApiTest\utils\read_fbData.py
import os
import yaml

yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'fb_data.yaml')

class ReadFBData:
    def __init__(self):
        self.yaml_path = yaml_path

    def read_yaml(self):
        with open(self.yaml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        return data

base_data = ReadFBData()