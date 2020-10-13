import logging

from Api.apiFactory import ApiFactory
import app, utils,pytest


@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        """获取token"""
        # 响应对象
        res = ApiFactory.get_user_api().get_token_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)
        # 断言token是否存在
        assert len(res.json().get("token")) > 0
        # 保存token
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_token_verify(self):
        """验证token"""
        # 响应对象
        res = ApiFactory.get_user_api().token_verify_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)
        # 断言有效
        assert res.json().get("isValid") is True

    def test_user_address(self):
        """用户地址"""
        # 响应对象
        res = ApiFactory.get_user_api().user_address_api()
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)
        # 断言数据正确性
        assert False not in [i in res.text for i in ["李李", "上海市", "13700000001", "浦东新区"]]
