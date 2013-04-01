import taobao, sinaweibo, qq

all_connectors = [
    sinaweibo.WeiboConnector(),
    taobao.TaobaoConnector(),
    qq.QQConnector(),
]

def get_connector(name):
    for connector in all_connectors:
        if connector.name == name:
            return connector