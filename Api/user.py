import logging

import app, requests


class UserApi:

    def __init__(self):
        # 获取token
        self.get_token_url = app.base_url + "/token/user"
        # 验证token
        self.token_verify_url = app.base_url + "/token/verify"
        # 用户信息地址
        self.user_address_url = app.base_url + "/address"

    def get_token_api(self):
        """获取token"""
        logging.info("token - 获取token")
        data = {"code": app.code}
        logging.info("请求数据:{}".format(data))
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def token_verify_api(self):
        """验证token"""
        logging.info("token - 验证token")
        data = {"token": app.headers.get("token")}
        logging.info("请求数据:{}".format(data))
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def user_address_api(self):
        """用户地址"""
        logging.info("token - 用户地址")
        return requests.get(self.user_address_url, headers=app.headers)
