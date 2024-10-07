import yaml
import os

def get_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return yaml.safe_load(content)
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
        return None
    except Exception as e:
        print(f"Error loading YAML file: {e}")
        return None

# 示例路径，可以根据实际情况调整
data_file_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'data.yaml')

data = get_data(data_file_path)
print(data)

