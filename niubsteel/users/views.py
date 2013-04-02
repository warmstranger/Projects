#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from product.views import index
from models import User, Connection
import connectors
import os, hashlib

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
    context = {
        'connectors': connectors.all_connectors
    }
    if request.method == 'GET':
        context['next'] = request.GET.get('next', '')
        return render_to_response('users/login.html', context, RequestContext(request))

    credential = request.POST.get('credential', '')
    password = request.POST.get('password', '')
    next = request.POST.get('next', '')

    user = authenticate(credential=credential, password=password)
    if user and not user.connector:
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

def logout_login(request):
    auth_logout(request)
    return redirect(login)

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
def convert(request):
    context = {}
    try:
        user = request.user
        if not user.connector:
            raise Exception('Cannot convert a non-connector user')

        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        user.username = username
        user.email = email
        user.save()
        user.set_password(password)
        user.connector = ''
        user.save()
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
        'page_title': u'人气用户',
        'lists': users
    }
    return render_to_response('lists.html', context, RequestContext(request))


def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'target_user': user,
        'selected_tab': 0,
        'products': user.products,
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

def connector_login(request, connector_name):
    connector = connectors.get_connector(connector_name)
    return redirect(connector.login())

def connector_callback(request, connector_name):
    connector = connectors.get_connector(connector_name)
    uid, name, access_token, expire_time = connector.login_callback(request)
    request.session['%s_access_token' % connector_name] = access_token

    if request.user.is_anonymous():
        try:
            connection = Connection.objects.get(connector_id=uid, connector=connector_name)
            if connection.user.connector:
                credential = connection.user.username
                user = authenticate(credential=credential, password=credential)
            else:
                user = authenticate(connection_id=connection.id)

        except Connection.DoesNotExist:
            seed = os.urandom(40)
            credential = hashlib.sha1(seed).hexdigest()
            user = User.objects.create_user(username=credential, email=credential, password=credential)
            user.connector = connector_name
            user.save()
            user = authenticate(credential=credential, password=credential)
            Connection.objects.create(user=user, connector=connector_name, connector_id=uid, connector_username=name)

        auth_login(request, user)
        return redirect(index)

    try:
        Connection.objects.get(user=request.user, connector=connector_name)
        return redirect(connector_detail, connector_name=connector_name, uid=uid)

    except Connection.DoesNotExist:
        Connection.objects.create(user=request.user, connector=connector_name,
            connector_id=uid, connector_username=name)
        return redirect(settings)

@login_required
def connector_cancel(request, connector_name):
    if request.user.is_anonymous() or request.user.connector:
        raise Exception('Only site users can cancel connector')

    Connection.objects.get(user=request.user, connector=connector_name).delete()
    return redirect(settings)

@login_required
def connector_detail(request, connector_name, uid):
    if request.user.is_anonymous() or request.user.connector:
        raise Exception('Only site users can see connector details')

    connection = Connection.objects.get(user=request.user, connector=connector_name)
    context = {
        'enabled': True,
    }
    if uid != connection.connector_id:
        context['error'] = u'警告：绑定的第三方账号并非当前登陆账号'
        context['enabled'] = False

    context['connection'] = connection
    access_token = request.session['%s_access_token' % connector_name]
    context.update(connection.open_connector.settings(uid, access_token))
    return render_to_response('users/connector.html', context, RequestContext(request))
