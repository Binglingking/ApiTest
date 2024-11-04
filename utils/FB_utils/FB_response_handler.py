import logging
import requests

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def FB_handle_response(response: requests.Response, expected_code=200):
    """
    处理 HTTP 响应的状态码，并进行相应的断言和日志记录。

    :param response: API 响应对象
    :param expected_code: 预期的 HTTP 状态码，默认为 200
    :return: None
    """
    try:
        response_json = response.json()
        if response_json['code'] == expected_code:
            logger.info(f"响应内容: {response_json}")
        elif response_json['code'] == 401:
            logger.warning("登录已过期")
            assert response_json['code'] == 401
            assert response_json['msg'] == "登录过期"
        else:
            logger.error(f"未知错误: {response_json}")
            assert False, f"异常响应: {response_json['code']}"
    except ValueError as e:
        # 处理 JSON 解析失败的情况
        logger.error(f"JSON 解析失败: {e}")
        assert False, f"无法解析响应内容: {response.text}"
