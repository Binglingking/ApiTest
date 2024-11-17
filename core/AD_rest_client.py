import json
import os
import subprocess
import requests
from utils.AD_utils.read_oriModMain import base_data
from utils.log_util import logger

GREEN = "\033[92m"
YELLOW = "\033[93m"
END = "\033[0m"

class TokenExpiredError(Exception):
    pass

class RestClient:
    def __init__(self):
        config = base_data.read_ini()
        self.base_url = config.get('api', 'base_url')
        auth = config['auth']
        self.token = auth['token']
        self.region = auth['region']
        self.version = auth['version']
        self.time = auth['time']
        self.headers = {
            "Authorization": json.dumps({
                "Head": {
                    "token": self.token,
                    "region": self.region,
                    "version": self.version,
                    "time": int(self.time)
                }
            })
        }

    def _handle_response(self, response):
        try:
            result = response.json()
            response.raise_for_status()
            self._log_response(result)
            if result.get('code') == 10003 and result.get('msg') == "登录已过期":
                logger.warning(YELLOW + "检测到Token过期，即将尝试刷新Token..." + END)
                self.refresh_token()
                raise TokenExpiredError("token已过期。请重试该请求。")
            return result
        except requests.exceptions.HTTPError as e:
            logger.error(f"请求出错: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"解析响应内容失败: {e}")
            raise

    def refresh_token(self):
        logger.info("token已过期。正在刷新token...")
        ADUI_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'AD_getTokenUI.py')
        try:
            subprocess.run(["python", ADUI_path], check=True)
            logger.info("UI自动获取token脚本：AD_getTokenUI.py 执行成功。")
        except subprocess.CalledProcessError as e:
            logger.error(f"执行 AD_getTokenUI.py 时出错: {e}")
            return
        config = base_data.read_ini()
        self.token = config['auth']['token']
        self.headers = {
            "Authorization": json.dumps({
                "Head": {
                    "token": self.token,
                    "region": self.region,
                    "version": self.version,
                    "time": int(self.time)
                }
            })
        }
        logger.info(GREEN + "Token 已成功更新。" + END)
        logger.info(GREEN + f"Token 已更新为: {self.token}" + END)

    def get(self, url, **kwargs):
        full_url = self.base_url + url
        self._log_request('GET', full_url, kwargs)
        response = requests.get(full_url, headers=self.headers, **kwargs)
        try:
            return self._handle_response(response)
        except TokenExpiredError:
            logger.info("使用新Token重试请求...")
            response = requests.get(full_url, headers=self.headers, **kwargs)
            return self._handle_response(response)

    def post(self, url, **kwargs):
        full_url = self.base_url + url
        self._log_request('POST', full_url, kwargs)
        response = requests.post(full_url, headers=self.headers, **kwargs)
        try:
            return self._handle_response(response)
        except TokenExpiredError:
            logger.info("使用新Token重试请求...")
            response = requests.post(full_url, headers=self.headers, **kwargs)
            return self._handle_response(response)

    def _log_request(self, method, url, params):
        logger.debug(f"请求方式: {method}, 请求地址: {url}")
        logger.debug(f"请求头: {self.headers}")
        logger.debug(f"请求参数: {json.dumps(params, indent=2)}")

    def _log_response(self, response):
        logger.debug(f"返回结果: {response}")

# if __name__ == "__main__":
#     client = RestClient()
#     try:
#         params = {
#             'channel_id': 'OceanEngine',
#             'model_name': 'pytest_add'
#         }
#
#         # 发送带有参数的 GET 请求
#         response = client.get("/api/orientationModule/list", params=params)
#         print(response)
#     except Exception as e:
#         logger.error(f"请求失败: {e}")

