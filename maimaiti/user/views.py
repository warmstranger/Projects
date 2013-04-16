# Create your views here.
#encoding: utf-8
from django.shortcuts import render_to_response,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from models import UserMapping
import json
import urllib
import urllib2

def redirect_login(request):
    LOGIN_URL = 'http://mobilesh.cptrue.com/account/SSOSignIn'
    APP_KEY = 'A71AB289C8444224A9C0'
    REDIRECT_URI = 'http://127.0.0.1:8000/login/'
    params ={
        'client_id':APP_KEY,
        'response_type':'code',
        'redirect_uri':REDIRECT_URI
    }
    return redirect(LOGIN_URL+'?'+urllib.urlencode(params))

def login(request):
    USERINFO_URL = 'http://mobilesh.cptrue.com/account/userinfo'
    APP_KEY = 'A71AB289C8444224A9C0'
    APP_SECRET = '3bd61869969ff3add3da960013eef381'
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
            UserMapping.objects.get(original_user_id = user_id)
        except UserMapping.DoesNotExist:
            user = User.objects.create_user(username = username,password='maimaiti')
            userMapping = UserMapping(user_id=user.id , original_user_id = user_id)
            userMapping.save()
        user = authenticate(username=username,password='maimaiti')
        auth_login(request, user)
        return redirect('/home')
    else:
        return redirect('/redirect_login')