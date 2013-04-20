# Create your views here.
#encoding: utf-8
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from models import Profile
import json
import urllib
import urllib2

APP_KEY = 'A71AB289C8444224A9C0'
APP_SECRET = '3bd61869969ff3add3da960013eef381'

LOGIN_URL = 'http://mobilesh.cptrue.com/account/SSOSignIn'
USERINFO_URL = 'http://mobilesh.cptrue.com/account/userinfo'

def redirect_login(request):
    REDIRECT_URI = 'http://127.0.0.1:8000/login'
    params ={
        'client_id':APP_KEY,
        'response_type':'code',
        'redirect_uri':REDIRECT_URI
    }
    return redirect(LOGIN_URL+'?'+urllib.urlencode(params))

def logout(request):
    from django.contrib.auth import logout as auth_logout
    auth_logout(request)
    return redirect('/')

def login(request):
    REDIRECT_URI = 'http://127.0.0.1:8000/home/'
    code = request.GET.get('code')
    params = {
        'client_id': APP_KEY,
        'client_secret': APP_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code,
        'grant_type': 'authorization_code'
    }
    response = urllib2.urlopen(USERINFO_URL, urllib.urlencode(params)).read()
    print response
    data = json.loads(response)
    if data['IsSuccess']:
        username = data['UserName']
        user_id = data['UserId']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.create_user(username=username, password=APP_SECRET)

        if not user.profile.connected_user:
            profile = user.profile
            profile.connected_user = user_id
            profile.save()

        user = authenticate(username=username, password=APP_SECRET)
        auth_login(request, user)
        return redirect('/')
    else:
        return redirect('/')