#coding=utf-8

from connector import Connector
import json

APP_KEY ='1021442576'
APP_SECRET='sandboxb13928e419aa08996b685d866'

class TaobaoConnector(Connector):

    name = 'taobao'
    verbose_name = u'淘宝'
    login_image = '/static/img/login_taobao.png'

    def __init__(self):
        super(TaobaoConnector, self).__init__(
            key=APP_KEY,
            secret=APP_SECRET,
            login_url='https://oauth.tbsandbox.com/authorize',
            get_token_url='https://oauth.tbsandbox.com/token',
            api_url='https://gw.api.tbsandbox.com/router/rest'
        )

    def _parse_token(self, response):
        token_dict = json.loads(response)
        uid = token_dict['taobao_user_id']
        access_token = token_dict['access_token']
        expire = token_dict['w1_expires_in']
        name = token_dict['taobao_user_nick']
        return uid, name, access_token, expire

    def _taobao_api(self, uid, access_token, method, field_list, **kwargs):
        result = self.api(access_token, '', format='json', method=method, v='2.0',
            fields=','.join(field_list), **kwargs)
        return result

    def settings(self, uid, access_token):
        response = self._taobao_api(uid, access_token, 'taobao.user.get',
            ['location', 'avatar', 'email', 'nick'])
        user = response['user_get_response']['user']

        response = self._taobao_api(uid, access_token, 'taobao.shop.get',
            ['sid', 'title', 'desc', 'pic_path', 'shop_score'], nick=user['nick'])
        shop = response['shop_get_response']

        return {
            'name': user['nick'],
            'location': user['location']['city'],
            'email': user['email'],
            'profile_image_url': user['avatar'],
            'shop': shop['shop'] if shop.has_key('shop') else None,
        }