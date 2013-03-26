#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

from product.views import index
from models import User
from models import SNWProfile
from weibo import APIClient
from oauth import TB_APIClient
from oauth import APIError
from store.models import Store
import hashlib
import string
#WEIBO
APP_KEY ='3357514965'
APP_SECRET='6c5f3440dc7390e1185231c36fa26fa7'
CALLBACK_URL = 'http://test.hupur.com/wb_callback'

#TAOBAO
TB_APP_KEY ='1021431343'
TB_APP_SECRET='sandboxd4769bb8980f15e831a5a9366'
TB_CALLBACK_URL = 'http://test.hupur.com/tb_callback'
tb_client = TB_APIClient(app_key=TB_APP_KEY, app_secret=TB_APP_SECRET,
                   redirect_uri=TB_CALLBACK_URL,domain='oauth.tbsandbox.com')

def weibo_invite(request):
    try:
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                                      redirect_uri=CALLBACK_URL)
        client.set_access_token(request.session['tb_access_token'], request.session['tb_expires_in'])
        friends = client.friendships.followers.active.get(uid=request.user.weibo_account.snw_id,count=200)
        return render_to_response('users/weibo_invite.html', friends, RequestContext(request))
    except KeyError:
        print('no client, needs auth, redirecting')
        return redirect(weibo_login)

def weibo_login(request):
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                       redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url(scope='email,direct_message_write,friendships_groups_read')    # redirect the user to `url'


    print("redirecting to" + url)
    return redirect(url)

def wb_callback(request):
    #TODO: handle denied
    CODE = request.GET.get('code')
    client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET,
                       redirect_uri=CALLBACK_URL)
    r = client.request_access_token(CODE)
    access_token = r.access_token  # access token，e.g., abc123xyz456
    expires_in = r.expires_in      # token expires in
    client.set_access_token(access_token, expires_in)
    request.session['tb_access_token'] = access_token;
    request.session['tb_expires_in'] = expires_in;
    uid =  client.account.get_uid.get()['uid']
    userinfo = client.users.show.get(uid=uid)
    nickname = userinfo['screen_name']
# if user is already logged on, connect user with Weibo
    if request.user.is_anonymous() == False:
        try:
            user = SNWProfile.objects.get(snw_id=uid).user  # weibo account already exist.
            if request.user != user:
                return redirect(index, {'error': 'This account is assigned to someone else, sign out first if you want to login'})
        except SNWProfile.DoesNotExist: # pofile not exist, create a new one
            user = request.user
            SNWProfile(user=user,type=1, snw_id=uid).save()

    else:  # if user is not logged in
        username = hashlib.sha1('weibo%d' % uid).hexdigest()
        try:
            user = SNWProfile.objects.get(snw_id=uid).user  # user profile exist, log in the user.

        except SNWProfile.DoesNotExist:  # not exist
            user = User.objects.create_user(username=username, email=username, password='secretpassword',login_type=1)
            SNWProfile(user=user,type=1,snw_id=uid,snw_nick=nickname).save()
            profile = user.profile
            profile.location = userinfo['location']
            profile.full_name = userinfo['screen_name']
            profile.description = userinfo['description']
            profile.website = userinfo['url']
            profile.image = userinfo['profile_image_url']
            profile.save()

        print('authenticating' + user.username + '   ' )
        user = authenticate(credential=user.username, password='secretpassword')
        auth_login(request, user)
    if user.activated:
        return redirect(index)
    else:
        return render_to_response('users/settings.html',{'user':user},RequestContext(request))

def taobao_login(request):

    url = tb_client.get_authorize_url(scope='usergrade')    # redirect the user to `url'
    print(url)
    return redirect(url)

def tb_callback(request):
    #TODO: Need add Weibo Attribute in model
    CODE = request.GET.get('code')
    r = tb_client.request_access_token(CODE)
    print('######authorizatin response #######' + r.__str__())
    access_token = r.access_token  # access token，e.g., abc123xyz456
    expires_in = r.expires_in      # token expires in
    request.session['tb_access_token'] = access_token
    request.session['tb_expires_in'] = expires_in
    uid = r['uid']
    nickname = r['nickname']
    tb_client.set_access_token(access_token, expires_in)
    username = hashlib.sha1('taobao%s' % uid).hexdigest()

    # if user logged in
    if request.user.is_anonymous() == False:
        try:
            user = SNWProfile.objects.get(snw_id=uid).user # snw account already exist.
            if request.user != user:
                return redirect(index, {'error': 'This account is assigned to someone else, sign out first if you want to login'})
        except SNWProfile.DoesNotExist:  # pofile not exist, create a new one
            user = request.user
            SNWProfile(user=user, type=2, snw_id=uid).save()

    else:  # if user is not logged in

        #create profile
        try:
            user = SNWProfile.objects.get(snw_id=uid).user   # login request
        except SNWProfile.DoesNotExist:    # registration
            user = User.objects.create_user(username=username, email=username, password='secretpassword', login_type=1)
            print("###new user created" + user.__str__())
            SNWProfile(user=user, type=2, snw_id=uid, snw_nick=nickname).save()
            profile = user.profile
            profile.full_name = nickname
            profile.save()

    #create shop
        try:
            response = tb_client.taobao.shop.get.Get(v=2.0, nick=r['nickname'], fields='sid,title,desc,bulletin')
            shop = response['shop_get_response']['shop']
            if nickname.startswith(u'sandbox'):
                url = 'http://mini.tbsandbox.com/seller/shop_detail.htm?nick=' + nickname
            else:
                url = 'http://shop' + shop['sid'] + '.taobao.com'
            try:
                store = Store.objects.get(owner=user)
                print("store already exist. store: " + store.__str__())
            except Store.DoesNotExist:  # create a mew store
                print("creating store....")
                store = Store(owner=user, name=shop['title'], url=url)
                store.save()
                print ("#### store saved" + store.__str__())
        except APIError as e:   # this user doesn't have any shop
            print(e)
#authenticate
    print('authenticate ' + user.username)
    user = authenticate(credential=user.username, password='secretpassword')
    auth_login(request, user)
    return render_to_response('users/settings.html', {'is_complete':False,'title': 'Complete your profile', 'user': user}, RequestContext(request))

def import_products(request):
    try:
        client = TB_APIClient(app_key=TB_APP_KEY, app_secret=TB_APP_SECRET,
                                          redirect_uri=TB_CALLBACK_URL,domain='oauth.tbsandbox.com')
        client.set_access_token(request.session['tb_access_token'],request.session['tb_expires_in'])
        result = client.taobao.items.onsale.get.Get(v=2.0, fields='num_iid,title,price,pic_url')
        return render_to_response('users/import_products.html', result.get('items_onsale_get_response',''), RequestContext(request))
    except Exception as e:
        print(e)
        return redirect(taobao_login)

def register(request):
    context = {}
    if request.method == 'GET':
        context['next'] = request.GET.get('next', '')
        return render_to_response('users/register.html', context, RequestContext(request))

    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    next = request.POST.get('next', '')

    try:
        User.objects.create_user(username, email, password)
        user = authenticate(credential=username, password=password)
        auth_login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect(index)
    except Exception as ex:
        context['error'] = ex
        context['username'] = username
        context['email'] = email
        context['password'] = password
        context['next'] = next
        return render_to_response('users/register.html', context, RequestContext(request))


def login(request):
    context = {}
    if request.method == 'GET':
        context['next'] = request.GET.get('next', '')
        return render_to_response('users/login.html', context, RequestContext(request))

    credential = request.POST.get('credential', '')
    password = request.POST.get('password', '')
    next = request.POST.get('next', '')

    user = authenticate(credential=credential, password=password)
    if user:
        auth_login(request, user)
        if next:
            return redirect(next)
        else:
            return redirect(index)
    else:
        context['error'] = u'密码错误'
        context['credential'] = credential
        context['next'] = next
        return render_to_response('users/login.html', context, RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect(index)

@login_required
def settings(request):
    context = {}
    if request.method == 'GET':
        return render_to_response('users/settings.html', context, RequestContext(request))

    change_type = request.POST.get('change_type', 'profile')
    try:
        if change_type == 'account':
            user = request.user
            user.email = request.POST.get('email', '')
            user.username = request.POST.get('username', '')
            user.activated = True
            user.save()
            context['user'] = user
        elif change_type == 'profile':
            p = request.user.profile
            p.full_name = request.POST.get('full_name', '')
            p.location = request.POST.get('location', '')
            p.description = request.POST.get('description', '')
            p.website = request.POST.get('website', '')
            p.save()
        elif change_type == 'profile_image':
            p = request.user.profile
            image_uploaded = request.FILES.get('profile_image', None)
            p.image.save(request.user.username, image_uploaded)
        return redirect(profile, username=request.user.username)

    except Exception as ex:
        context['error'] = ex

    return render_to_response('users/settings.html', context, RequestContext(request))

@login_required
def reset_password(request):
    context = {}
    if request.method == 'GET':
        return render_to_response('users/change_password.html', context, RequestContext(request))

    new_password = request.POST.get('new_password', '')
    user = request.user
    user.set_password(new_password)
    user.save()
    return redirect(index)

def top_users(request):
    users = User.objects.all()[:20]
    context = {
        'page_title': u'热门用户',
        'lists': users
    }
    return render_to_response('lists.html', context, RequestContext(request))

def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'target_user': user,
        'selected_tab': 0,
        'products': user.products[:40],
    }
    return render_to_response('users/profile.html', context, RequestContext(request))

def list_followers(request, username):
    user = User.objects.get(username=username)
    context = {
        'target_user': user,
        'selected_tab': 4,
        'lists': user.followers,
    }
    return render_to_response('users/profile.html', context, RequestContext(request))

def list_followings(request, username):
    user = User.objects.get(username=username)
    context = {
        'target_user': user,
        'selected_tab': 5,
        'lists': user.following_people,
    }
    return render_to_response('users/profile.html', context, RequestContext(request))

def list_following_stores(request, username):
    user = User.objects.get(username=username)
    context = {
        'target_user': user,
        'selected_tab': 6,
        'lists': user.following_stores,
        }
    return render_to_response('users/profile.html', context, RequestContext(request))

def forget_password(request):
    context = {}
    if request.method == 'GET':
        return render_to_response('users/forget_password.html', context, RequestContext(request))

    email = User.objects.normalize_email(request.POST.get('email', ''))
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        context['error'] = '无此用户'
        return render_to_response('users/forget_password.html', context, RequestContext(request))

    #TODO: send user email

    return redirect(index)

def check(request):
    email = User.objects.normalize_email(request.GET.get('email', ''))
    username = request.GET.get('username', '')

    users = User.objects.all()
    if username:
        users = users.filter(username=username)
    if email:
        users = users.filter(email=email)

    if users.exists():
        return HttpResponse(0)
    else:
        return HttpResponse(1)
