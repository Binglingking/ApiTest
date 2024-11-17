import os

current_dir = os.path.dirname(os.path.abspath(__file__))
    # 组合路径，指向配置文件 AD_settings.ini
ini_path = os.path.join(current_dir, '..', 'config', 'AD_settings.ini')
print(ini_path)
