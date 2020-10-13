def common_assert_code(res, code=200):
    """
    通用断言状态码
    :param res: 响应对象
    :param code: 状态码 默认200
    :return:
    """
    assert res.status_code == code
