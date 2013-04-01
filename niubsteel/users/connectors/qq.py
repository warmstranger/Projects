#coding=utf-8

from connector import Connector
import urllib2, json, urlparse

APP_KEY = '100406677'
APP_SECRET = '0a1d05bcf76ed7f37d2467902c967120'

class QQConnector(Connector):

    name = 'qq'
    verbose_name = u'QQ'
    login_image = 'http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Connect_logo_7.png'

    def __init__(self):
        self.openid_url = 'https://graph.qq.com/oauth2.0/me'

        super(QQConnector, self).__init__(
            key=APP_KEY,
            secret=APP_SECRET,
            login_url='https://graph.qq.com/oauth2.0/authorize',
            get_token_url='https://graph.qq.com/oauth2.0/token',
            api_url='https://graph.qq.com/',
        )

    def _parse_token(self, response):
        token_dict = urlparse.parse_qs(response)
        access_token = token_dict['access_token'][0]
        expire = token_dict['expires_in'][0]

        url = '%s?access_token=%s' % (self.openid_url, access_token)
        response = urllib2.urlopen(url).read()[9:-3]
        uid = json.loads(response)['openid']

        response = self._qq_api(uid, access_token, 'user/get_user_info')
        return uid, response['nickname'], access_token, expire

    def _qq_api(self, uid, access_token, url, **kwargs):
        return self.api(access_token, url, oauth_consumer_key=APP_KEY, openid=uid, format='json', **kwargs)

    def settings(self, uid, access_token):

        return {
        }
