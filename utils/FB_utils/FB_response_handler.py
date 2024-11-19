import logging
import requests

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def FB_handle_response(response, expected_code=200):
    """
    处理 HTTP 响应的状态码，并进行相应的断言和日志记录。

    :param response: API 响应对象
    :param expected_code: 预期的 HTTP 状态码，默认为 200
    :return: None
    """
    if response['code'] == expected_code:
        logger.info(f"响应内容: {response}")
    elif response['code'] == 401:
        logger.warning("登录已过期")
        assert response['code'] == 401
        assert response['msg'] == "登录过期"
    else:
        logger.error(f"未知错误: {response}")
        assert False, f"异常响应: {response['code']}"
