import logging

import requests, app


class ProductApi:
    """商品"""

    def __init__(self):
        # 商品分类
        self.product_classify_url = app.base_url + "/category/all"
        # 分类下商品
        self.classify_product_url = app.base_url + "/product/by_category"
        # 商品信息
        self.product_detail_url = app.base_url + "/product/{}"

    def product_classify_api(self):
        """商品分类"""
        logging.info("商品 - 商品分类")
        return requests.get(self.product_classify_url)

    def classify_product_api(self, classify_id=2):
        """
        分类下商品
        :param classify_id: 分类id
        :return:
        """
        logging.info("商品 - 分类下商品")
        data = {"id": classify_id}
        logging.info("请求数据:{}".format(data))
        # 请求
        return requests.get(self.classify_product_url, params=data)

    def product_detail_api(self, product_id=2):
        """
        商品信息
        :param product_id: 商品id
        :return:
        """
        logging.info("商品 - 商品信息")
        return requests.get(self.product_detail_url.format(product_id))
