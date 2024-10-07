import json

class TestHeaders:
    def __init__(self):
        self.test_url = 'https://test-advertising.yostar.net'
        self.uat_url = 'https://staging-advertising.yostar.net'
        self.access_token = "eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI4NTQ1OTg3LCJpYXQiOjE3MjgyODY3ODd9.xfnsVXYQYB94-vdJNj9M7d-5GT6A9N--vshCpma0ohY"
        self.refresh_token = "eyJhbGciOiJIUzI1NiIsImtpZCI6InYxIiwidHlwIjoiSldUIn0.eyJuYW1lIjoiemhhbmdzaHVuIiwiaXNzIjoieW9zdGFyIiwic3ViIjoiNTc2IiwiZXhwIjoxNzI4ODkxNTg3LCJpYXQiOjE3MjgyODY3ODd9.JKswgI9JEYR6b-cj0XrI4KLKLL5pvMuWQrwbtdzdA2c"
        self.project_id = "cqbltdqdf2vdu69hqkbg"

    def generate_headers(self):
        headers = {
            "Authorization": json.dumps({
                "Head": {
                    "Token": {
                        "access_token": self.access_token,
                        "refresh_token": self.refresh_token,
                        "uid": 576
                    },
                    "Version": "v2.0",
                    "ProjectId": self.project_id
                }
            }),
            "Content-Type": "application/json"
        }
        return headers

# 使用示例
if __name__ == "__main__":
    test_headers = TestHeaders()
    headers = test_headers.generate_headers()
    print(headers)
