# Create your views here.
from django.shortcuts import render_to_response,redirect
import datetime
from models import UserFollow,TagFollow
from django.contrib.auth.models import User

def follow_user(request,user_id,following_id):
    time = datetime.time
    try:
        UserFollow.objects.get(user_id = user_id,following_id = following_id)
    except UserFollow.DoesNotExist:
        userFollow = UserFollow(user_id = user_id,following_id = following_id,time = time)
        userFollow.save()
    return redirect('/home/')

def unfollow_user(request,user_id,following_id):
    try:
        userFollow = UserFollow.objects.get(user_id = user_id,following_id = following_id)
        userFollow.delete()
    except UserFollow.DoesNotExist:
        pass
    return redirect('/home/')

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

