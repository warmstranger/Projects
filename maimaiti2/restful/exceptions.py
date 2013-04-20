#coding=utf-8

class APIError(Exception):
    def __init__(self, status=500, data=u'服务器异常'):
        self.status = status
        self.data = data