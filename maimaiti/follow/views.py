# Create your views here.
#coding: utf-8
from django.shortcuts import render_to_response,redirect
import datetime
from models import UserFollow,TagFollow
from django.contrib.auth.models import User
from django.http import HttpResponse
import json

def follow_user(request,following_id):
    if request.user.is_active:
        user = request.user
        time = datetime.time
        try:
            UserFollow.objects.get(user_id = user.id,following_id = following_id)
            dic ={
                'flag':0,
                'msg':'您已关注!',
            }
        except UserFollow.DoesNotExist:
            userFollow = UserFollow(user_id = user.id,following_id = following_id,time = time)
            userFollow.save()
            followers = UserFollow.objects.filter(following_id = following_id)
            dic ={
                'flag':1,
                'msg':'关注成功!',
                'follower':len(followers),
            }
    else:
        dic ={
            'flag':-1,
            'msg':'请先登录!',
        }
    dic_json = json.dumps(dic)
    response=HttpResponse()
    response['Content-Type']="text/javascript;charset='UTF-8'"
    response.write(dic_json)
    return HttpResponse(response)

def unfollow_user(request,following_id):
    if request.user.is_active:
        user = request.user
        try:
            userFollow = UserFollow.objects.get(user_id = user.id,following_id = following_id)
            userFollow.delete()
            followers = UserFollow.objects.filter(following_id = following_id)
            dic ={
                'flag':1,
                'msg':'取消关注成功!',
                'follower':len(followers),
            }
        except UserFollow.DoesNotExist:
            dic ={
                'flag':0,
                'msg':'未关注此人!',
            }
    else:
        dic ={
            'flag':-1,
            'msg':'请先登录!',
        }
    dic_json = json.dumps(dic)
    response=HttpResponse()
    response['Content-Type']="text/javascript;charset='UTF-8'"
    response.write(dic_json)
    return HttpResponse(response)

def follow_tag(request,user_id,following_id):
    time = datetime.time
    tagFollow = TagFollow(user_id = user_id,following_id = following_id,time = time)
    tagFollow.save()
    return redirect('/home/')

def unfollow_tag(request,user_id,following_id):
    try:
        tagFollow = TagFollow.objects.get(user_id = user_id,following_id = following_id)
        tagFollow.delete()
    except TagFollow.DoesNotExist:
        pass
    return redirect('/home/')

def list_following(user_id):
    list = UserFollow.objects.filter(user_id = user_id).order_by('-time')
    following_list = []
    if len(list):
        for item in list:
            try:
                following = User.objects.get(id = item.following_id)
                following_list.append(following)
            except User.DoesNotExist:
                pass
    following_list.reverse()
    return render_to_response('list.html',{'following_list':following_list})

