from utils.read_data import  get_yaml
from utils.yaml_util import fuc_yaml


def test_eval():
    data = get_yaml['person']
    print(fuc_yaml(data))
    print(data)
