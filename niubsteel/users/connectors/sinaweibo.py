#coding=utf-8

from connector import Connector
import json

APP_KEY = '235260339'
APP_SECRET = 'a3381ab6819973254f4899b903748059'

class WeiboConnector(Connector):

    name = 'weibo'
    verbose_name = u'微博'
    login_image = '/static/img/signin.png'

    def __init__(self):
        super(WeiboConnector, self).__init__(
            key=APP_KEY,
            secret=APP_SECRET,
            login_url='https://api.weibo.com/oauth2/authorize',
            get_token_url='https://api.weibo.com/oauth2/access_token',
            api_url='https://api.weibo.com/2/'
        )

    def _parse_token(self, response):
        token_dict = json.loads(response)
        uid = token_dict['uid']
        access_token = token_dict['access_token']
        expire = token_dict['expires_in']
        name = self.api(access_token=access_token, api_url='users/show.json', uid=uid)['name']
        return uid, name, access_token, expire

    def settings(self, uid, access_token):
        friends = self.api(access_token, 'friendships/friends.json', uid=uid)
        show = self.api(access_token, 'users/show.json', uid=uid)

        return {
            'friends': friends['users'],
            'location': show['location'],
            'description': show['description'],
            'website': show['url'],
            'profile_image_url': show['profile_image_url'],
            'name': show['name'],
        }
