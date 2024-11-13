import configparser
import os
import logging
import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 定义目标URL
URL = "https://test-admax.yostar.net"
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_config_path():
    # 获取当前脚本文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 组合路径，指向配置文件 AD_settings.ini
    ini_path = os.path.join(current_dir, '..', 'config', 'AD_settings.ini')
    return ini_path

GREEN = "\033[92m"
END = "\033[0m"

def get_token_from_ui():
    # 创建 Chrome 选项对象
    options = Options()

    # 设置 Chrome 选项，让浏览器窗口在测试结束后保持打开状态
    options.add_experimental_option("detach", True)

    # 排除自动化控制的开关，防止被检测
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 禁用自动化扩展
    options.add_experimental_option('useAutomationExtension', False)

    # 设置 User-Agent，模拟真实用户的浏览器环境
    options.add_argument('user-agent=Mozilla/AT5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')

    # 禁用 Blink 功能，防止被检测
    options.add_argument("--disable-blink-features=AutomationControlled")

    # 使用 webdriver_manager 自动下载并管理 ChromeDriver
    service = webdriver.chrome.service.Service(ChromeDriverManager().install())

    # 指定 Chrome 可执行文件的实际路径，确保 Selenium 能找到 Chrome 浏览器
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # 请替换为你的 Chrome 浏览器实际路径

    # 创建 WebDriver 对象，启动 Chrome 浏览器
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # 访问目标 URL
        driver.get(URL)

        # 等待页面加载完成
        time.sleep(2)

        # 找到登录按钮并点击
        login_button1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/button')
        login_button1.click()

        # 等待页面加载完成
        time.sleep(4)

        # 点击某个元素，进入下一步
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/a').click()

        # 等待页面加载完成
        time.sleep(3)

        # 选择某个选项
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/ul/li[1]').click()

        # 等待页面加载完成
        time.sleep(2)

        # 输入用户名
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[1]/div/div/div[1]/input').send_keys('zhangshun')

        # 输入密码
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[2]/div/div/div[1]/input').send_keys('ASDfghjkl.0804')

        # 点击登录按钮
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[4]/div/div/button/span').click()

        # 等待页面加载完成
        time.sleep(2)

        # 重新访问目标 URL
        driver.get(URL)

        # 点击某个按钮
        driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/button').click()

        # 等待页面加载完成
        time.sleep(2)

        # 刷新页面
        driver.refresh()

        # 执行 JavaScript 代码，获取 localStorage 中的数据
        js_code = """return JSON.stringify(window.localStorage);"""
        a = driver.execute_script(js_code)

        # 将获取到的 JSON 字符串转换为 Python 字典
        data_a = json.loads(a)

        # 从字典中提取 token
        token = data_a['token']

        # 构建 token 信息字典
        token_info = {
            'Head': {'token': token, 'region': 'CN', 'version': '1.0', 'time': int(time.time()) + 36000000}
        }

        # 返回 token 信息
        return token_info

    finally:
        # 无论成功还是失败，都关闭浏览器
        driver.quit()

def write_token_to_ini(token_info):
    # 获取配置文件的路径
    ini_path = get_config_path()

    try:
        # 创建 ConfigParser 对象
        config = configparser.ConfigParser()

        # 读取配置文件
        config.read(ini_path)

        # 设置 auth 部分的 token 值
        config.set('auth', 'token', token_info['Head']['token'])

        # 写入配置文件
        with open(ini_path, 'w') as configfile:
            config.write(configfile)

        # 记录日志，表示 Token 已成功写入配置文件
        logger.info(f"Token 已成功写入到 {ini_path}")

    except FileNotFoundError:
        # 如果配置文件未找到，记录错误日志
        logger.error(f"配置文件 {ini_path} 未找到。")

    except configparser.Error as e:
        # 如果配置文件解析出错，记录错误日志
        logger.error(f"配置文件解析错误: {e}")

    except Exception as e:
        # 如果发生其他未知错误，记录错误日志
        logger.error(f"发生未知错误: {e}")

if __name__ == "__main__":
    # 获取 token 信息
    token_info = get_token_from_ui()

    # 如果成功获取到 token 信息，将其写入配置文件
    if token_info:
        write_token_to_ini(token_info)
"""
代码说明
导入模块：
导入了必要的模块，包括 configparser、os、logging、json、time 以及 selenium 和 webdriver_manager 相关的模块。
定义目标 URL：
URL 是我们要访问的目标网站地址。
日志配置：
配置了日志记录器，用于记录程序运行过程中的信息和错误。
获取配置文件路径：
get_config_path 函数用于获取配置文件 AD_settings.ini 的路径。
获取 Token 信息：
get_token_from_ui 函数负责通过 UI 获取 Token 信息。
创建 Chrome 选项对象，设置各种选项以模拟真实用户的行为。
使用 webdriver_manager 自动下载并管理 ChromeDriver。
启动 Chrome 浏览器，访问目标 URL，并进行一系列的页面交互操作。
最后，通过执行 JavaScript 代码获取 localStorage 中的 Token 信息，并返回。
写入 Token 到配置文件：
write_token_to_ini 函数负责将获取到的 Token 信息写入配置文件。
读取配置文件，设置 auth 部分的 token 值，并保存配置文件。
记录日志，表示 Token 已成功写入配置文件。
主程序入口：
在 if __name__ == "__main__": 块中，调用 get_token_from_ui 函数获取 Token 信息，如果成功获取到，则调用 write_token_to_ini 函数将其写入配置文件。
"""