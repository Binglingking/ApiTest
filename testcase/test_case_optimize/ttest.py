import json

import requests

test_url = "https://test-admax.yostar.net"
Authorization_test = {
        "Head": {"token": "9f6ed40924488358990084e699901b35476de082", "region": "CN", "version": "1.0",
                 "time": 1691486926}}
token_test = {"Authorization": json.dumps(Authorization_test)}

data = {
    "name": "test_name",
    "age": 18,
    "sex": "男"
}