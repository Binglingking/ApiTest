from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json

# 使用 webdriver-manager 自动管理 ChromeDriver
service = webdriver.chrome.service.Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # 请替换为你的 Chrome 浏览器实际路径

driver = webdriver.Chrome(service=service, options=options)

try:
    # 第一步：进入页面并点击导航页按钮进入登录页面
    driver.get("https://test-publish-center.yo-star.com/#/login")

    # 显式等待导航按钮出现
    nav_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div/div[3]/div[1]/span/i'))
    )
    nav_button.click()

    # 显式等待登录页面加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div/div[2]/div[5]/form/div[1]/div/div[1]/div/input'))
    )

    # 第二步：输入账号和密码后点击登录按钮
    username_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div/div[2]/div[5]/form/div[1]/div/div[1]/div/input')
    password_input = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div/div[2]/div[5]/form/div[2]/div/div[1]/div/input')

    username_input.send_keys('zhangshun')  # 替换为你的用户名
    password_input.send_keys('ASDfghjkl.0804')  # 替换为你的密码

    login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div/div[2]/div[5]/form/div[3]/div/button')
    login_button.click()

    # 显式等待登录完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/span/input'))
    )

    # 第三步：搜索投放管理平台
    search_input = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[1]/span/input')
    search_input.send_keys('投放管理平台')

    # 第四步：点击打开投放管理平台
    element_1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/span[1]'))
    )
    element_1.click()
    # 获取 Authorization 中的 access_token 和 refresh_token
    js_code = """return JSON.stringify(window.localStorage);"""
    local_storage_data = driver.execute_script(js_code)
    data = json.loads(local_storage_data)
    # print(data)

    # 假设 Authorization 信息存储在 localStorage 的 'USERAUTH' 键中
    authorization_data = data.get('USERAUTH')

    # print(f"Access Token (投放管理平台): {authorization_data}")

    # 显式等待新标签页打开
    WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])

    # 第五步：在新标签页中打开项目：ADMax-分包工具2
    element_2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[2]/div[4]/div/span[1]'))
    )
    element_2.click()

    # 显式等待页面加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[1]/div/div/div[2]/div[1]/div[2]/div[4]/div/span[1]'))
    )

    # 获取 ProjectId
    js_code = """return JSON.stringify(window.localStorage);"""
    local_storage_data = driver.execute_script(js_code)
    data = json.loads(local_storage_data)
    ProjectID = data.get('ProjectID')

    # print(f"Project ID (ADMax-分包工具2): {ProjectID}")

    # 合并结果为所需格式
    Test_headers = {
        'Authorization': json.dumps({
            'Head': {
                'Token': authorization_data,
                'Version': 'v2.0',
                'ProjectId': ProjectID
            }
        }),
        'Content-Type': 'application/json'
    }

    print(f"Result: {Test_headers}")

finally:
    # 关闭浏览器
    driver.quit()