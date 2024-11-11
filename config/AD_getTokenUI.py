import configparser
import os
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_config_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ini_path = os.path.join(current_dir, '..', 'config', 'AD_settings.ini')
    return ini_path

GREEN = "\033[92m"
END = "\033[0m"

def get_token_from_ui():
    # 这里编写UI脚本逻辑，获取Token
    # 假设获取到的Token为 new_token
    new_token = "fd302d262cbaee099c024508bbfca54d0546350f"  # 示例值
    # 将Token写入到 settings.ini 文件中
    ini_path = get_config_path()
    try:
        config = configparser.ConfigParser()
        config.read(ini_path)
        config.set('auth', 'token', new_token)
        with open(ini_path, 'w') as configfile:
            config.write(configfile)
    except FileNotFoundError:
        logger.error(f"配置文件 {ini_path} 未找到。")
    except configparser.Error as e:
        logger.error(f"配置文件解析错误: {e}")
    except Exception as e:
        logger.error(f"发生未知错误: {e}")

if __name__ == "__main__":
    get_token_from_ui()