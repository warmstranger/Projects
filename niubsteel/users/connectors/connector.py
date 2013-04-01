import urllib, urllib2, json, urlparse

class Connector(object):

    name = ''
    auth_client = 'test.hupur.com'

    def __init__(self, key, secret, login_url, get_token_url, api_url):
        self.key = key
        self.secret = secret
        self.api_url = api_url

        self.login_url = login_url
        self.login_callback_url = 'http://%s/login/callback/%s' % (self.auth_client, self.name)

        self.get_token_url = get_token_url

    def _parse_token(self, token_dict):
        raise NotImplementedError('parse token needs to be implemented in concrete Connector')

    @property
    def template(self):
        return 'connector/%s.html' % self.name

    def settings(self, uid, access_token):
        return {}

    def login(self, scope=None):
        params = {
            'client_id': self.key,
            'response_type': 'code',
            'redirect_uri': self.login_callback_url,
            'scope': scope,
        }
        return self.login_url + '?' + urllib.urlencode(params)


    def login_callback(self, request):
        code = request.GET.get('code', '')
        params = {
            'client_id': self.key,
            'client_secret': self.secret,
            'redirect_uri': self.login_callback_url,
            'code': code,
            'grant_type': 'authorization_code'
        }
        response = urllib2.urlopen(self.get_token_url, urllib.urlencode(params)).read()
        return self._parse_token(response)

    def api(self, access_token, api_url, **kwargs):
        url = urlparse.urljoin(self.api_url, api_url)
        params = kwargs.copy()
        params['access_token'] = access_token
        response = urllib2.urlopen(url + '?' + urllib.urlencode(params)).read()
        return json.loads(response)