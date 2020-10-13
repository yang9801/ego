from Api.apiFactory import ApiFactory

# # 调用轮播图
# print("轮播图:{}".format(ApiFactory.get_home_api().banner_api().json()))
#
# # 调用专题栏
# print("专题栏:{}".format(ApiFactory.get_home_api().theme_api().json()))
#
# # 调用最新新品
# print("最新新品:{}".format(ApiFactory.get_home_api().recent_product_api().json()))


# # 调用商品分类
# print("商品分类:{}".format(ApiFactory.get_product_api().product_classify_api().json()))
#
# # 调用分类下商品
# print("分类下商品:{}".format(ApiFactory.get_product_api().classify_product_api().json()))
#
# # 调用商品信息
# print("商品信息:{}".format(ApiFactory.get_product_api().product_detail_api().json()))

# print("token:{}".format(ApiFactory.get_user_api().get_token_api().json()))

# 调用订单列表
print("订单列表:{}".format(ApiFactory.get_order_api().order_list_api().json()))

print("创建订单:{}".format(ApiFactory.get_order_api().create_order_api(12, 7).json()))

print("订单详细:{}".format(ApiFactory.get_order_api().query_order_api(117).json()))

