import json
import os
import time
import logging
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# 日志配置
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('user-agent=Mozilla/AT5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("webdriver.chrome.driver=D:\\exe\\chromedriver\\chromedriver.exe")
    chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def wait_for_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def login_and_get_tokens(driver):
    driver.get("https://test-publish-center.yo-star.com/#/login")
    wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[3]/div[1]/span/i').click()
    wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/ul/li[1]').click()
    wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[1]/div/div/div[1]/input').send_keys('zhangshun')
    wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[2]/div/div/div[1]/input').send_keys('ASDfghjkl.0804')
    wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/form/div[1]/div[4]/div/div/button/span').click()
    time.sleep(10)  # 等待登录完成

    js_code = """return JSON.stringify(window.localStorage);"""
    local_storage_data = driver.execute_script(js_code)
    token = json.loads(local_storage_data)['USERAUTH']
    access_token = json.loads(token)['access_token']
    refresh_token = json.loads(token)['refresh_token']
    uid = json.loads(token)['uid']
    # Version = json.loads(token)['Version']
    print(token)
    print(access_token)
    print(refresh_token)
    print(uid)
    return access_token, refresh_token, uid

def perform_actions(driver, access_token, refresh_token, uid):
    wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div[2]/span[1]').click()
    time.sleep(2)  # 等待新标签页打开

    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)

    input_element = wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div/div/div[1]/span[2]/input')
    input_element.send_keys("2.x方舟")
    input_element.clear()
    time.sleep(1)
    input_element.send_keys("2.x雀魂")
    input_element.clear()
    time.sleep(1)
    input_element.send_keys("ADMax-分包工具2")
    time.sleep(1)

    button_element = wait_for_element(driver, By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[2]/div/div/span[1]')
    button_element.click()
    time.sleep(10)  # 等待

    js_code1 = """return JSON.stringify(window.localStorage);"""
    local_storage_data1 = driver.execute_script(js_code1)
    print(local_storage_data1)
    ProjectID = json.loads(local_storage_data1)['ProjectID']
    print(ProjectID)

    # 构建 Authorization 字符串
    # test_headers = {
    #     "Authorization": (
    #         '{"Head":{"Token":"{\\"access_token\\":\\"' + access_token + '\\",'
    #         '\\"refresh_token\\":\\"' + refresh_token + '\\",'
    #         '\\"uid\\":576}","Version":"v2.0","ProjectId":"' + ProjectID + '"}}'
    #     ),
    #     "Content-Type": "application/json"
    # }
    #
    # # 打印最终的 headers
    # print(json.dumps(test_headers))
    return ProjectID

def write_token_to_ini(access_token, refresh_token, project_id, uid):
    # 获取配置文件的路径
    ini_path = get_config_path()

    try:
        # 创建 ConfigParser 对象
        config = configparser.ConfigParser()

        # 读取配置文件
        config.read(ini_path)

        # 设置 auth 部分的 token 值
        config.set('auth', 'access_token', access_token)
        config.set('auth', 'refresh_token', refresh_token)
        config.set('auth', 'project_id', project_id)
        # config.set('auth', 'Version', version)
        config.set('auth', 'uid', str(uid))

        # 写入配置文件
        with open(ini_path, 'w') as configfile:
            config.write(configfile)

        # 记录日志，表示 Token 已成功写入配置文件
        logger.info(f"Token 已成功写入到 {ini_path}")

    except FileNotFoundError:
        # 如果配置文件未找到，记录错误日志
        logger.error(f"配置文件 {ini_path} 未找到。")
        return False

    except configparser.Error as e:
        # 如果配置文件解析出错，记录错误日志
        logger.error(f"配置文件解析错误: {e}")
        return False

    except Exception as e:
        # 如果发生其他未知错误，记录错误日志
        logger.error(f"发生未知错误: {e}")
        return False

    return True

def get_config_path():
    # 获取当前脚本文件的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 组合路径，指向配置文件 FBSettings.ini
    ini_path = os.path.join(current_dir, '..', 'config', 'FBSettings.ini')
    return ini_path

def main():
    max_retries = 5
    for attempt in range(max_retries):
        try:
            driver = setup_driver()
            access_token, refresh_token, uid = login_and_get_tokens(driver)
            project_id = perform_actions(driver, access_token, refresh_token, uid)
            if write_token_to_ini(access_token, refresh_token, project_id, uid):
                logger.info("Token 写入成功")
                break
            else:
                logger.error(f"Token 写入失败，尝试第 {attempt + 1} 次")
                if attempt < max_retries - 1:
                    time.sleep(5)  # 等待5秒后重试
                else:
                    logger.error("达到最大重试次数，脚本运行失败")
        except (WebDriverException, TimeoutException) as e:
            logger.error(f"Error occurred: {e}")
            if attempt < max_retries - 1:
                time.sleep(5)  # 等待5秒后重试
            else:
                logger.error("达到最大重试次数，脚本运行失败")
        finally:
            driver.quit()

if __name__ == "__main__":
    main()
