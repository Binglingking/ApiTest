import json
import os
import subprocess
import requests

from core.FBclient_copy import access_token, refresh_token, project_id
from utils.FB_utils.read_FBdata import base_data
from utils.log_util import logger

GREEN = "\033[92m"
YELLOW = "\033[93m"
END = "\033[0m"


class TokenExpiredError(Exception):
    pass


class RestClient:
    def __init__(self):
        config = base_data.read_ini()
        self.base_url = config.get('host', 'test_url')
        auth = config['auth']
        access_token = config['auth']['access_token']
        refresh_token = config['auth']['refresh_token']
        project_id = config['auth']['project_id']
        uid = config['auth']['uid']
        self.headers = {
            "Authorization": (
                    '{"Head":{"Token":"{\\"access_token\\":\\"' + access_token + '\\",'
                                                                                 '\\"refresh_token\\":\\"' + refresh_token + '\\",'
                                                                                                                             '\\"uid\\":576}","Version":"v2.0","ProjectId":"' + project_id + '"}}'
            ),
            "Content-Type": "application/json"
        }
        # print(f"初始化headers: {self.headers}")  # 打印初始化的headers

    def _handle_response(self, response):
        try:
            result = response.json()
            response.raise_for_status()
            self._log_response(result)
            if result.get('code') == 401 and result.get('msg') == "登录过期":
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
        ADUI_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'FB_getTokenUI.py')
        try:
            subprocess.run(["python", ADUI_path], check=True)
            logger.info("UI自动获取token脚本：FB_getTokenUI.py 执行成功。")
        except subprocess.CalledProcessError as e:
            logger.error(f"执行 FB_getTokenUI.py 时出错: {e}")
            return
        config = base_data.read_ini()
        access_token = config['auth']['access_token']
        refresh_token = config['auth']['refresh_token']
        project_id = config['auth']['project_id']
        self.headers = {
            "Authorization": (
                    '{"Head":{"Token":"{\\"access_token\\":\\"' + access_token + '\\",'
                                                                                 '\\"refresh_token\\":\\"' + refresh_token + '\\",'
                                                                                                                             '\\"uid\\":576}","Version":"v2.0","ProjectId":"' + project_id + '"}}'
            ),
            "Content-Type": "application/json"
        }
        print(f"刷新后的headers: {self.headers}")  # 打印刷新后的headers
        logger.info(GREEN + "Token 已成功更新。" + END)
        logger.info(GREEN + f"Token 已更新为: {self.headers}" + END)

    def get(self, url, **kwargs):
        full_url = self.base_url + url
        self._log_request('GET', full_url, kwargs)
        response = requests.get(full_url, headers=self.headers, **kwargs)
        print(response.url)
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
        print(f"返回结果: {response}")  # 打印返回结果

#
if __name__ == "__main__":
    client = RestClient()
#     try:
#         data = {
#             "id": "1"
#         }
#
#
#         response = client.post("/admax-packerapi/packer/original/list", json=data)
#     except Exception as e:
#         logger.error(f"请求失败: {e}")
