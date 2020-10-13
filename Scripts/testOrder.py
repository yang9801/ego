import logging

from Api.apiFactory import ApiFactory
import app, utils


class TestOrder:

    def test_order_list(self):
        """订单列表"""
        res = ApiFactory.get_order_api().order_list_api(1)
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言响应状态码
        utils.common_assert_code(res)
        # 断言关键词
        assert False not in [i in res.text for i in ["current_page", "data", "snap_name"]]

    def test_create_order(self):
        """创建订单"""
        product_id = 12
        count = 7
        res = ApiFactory.get_order_api().create_order_api(product_id, count)
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言用户no 和id 字段大于等于0
        assert len(res.json().get("order_no")) and len(res.json().get("order_id"))

    def test_query_order(self):
        """查看订单"""
        # 订单id
        order_id = 115
        # 预期结果
        exp_name = "李李"
        exp_mobile = "13700000001"
        res = ApiFactory.get_order_api().query_order_api(order_id)
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言订单id
        assert res.json().get("id") == 115

        # 断言地址 用户名 手机号
        assert res.json().get("snap_address").get("name") == exp_name
        assert res.json().get("snap_address").get("mobile") == exp_mobile
