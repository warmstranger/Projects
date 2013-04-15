# Create your views here.
#coding: utf-8
from django.shortcuts import render_to_response,redirect
import datetime
from models import Collection
from post.models import  Post
from post.views import parse_html
from django.http import HttpResponse
import json

def collect(request,user_id,post_id):
    time = datetime.time
    try:
        Collection.objects.get(user_id = user_id,post_id = post_id)
        dic ={
            'flag':0,
            'msg':'您已收藏!',
        }
    except Collection.DoesNotExist:
        collection = Collection(user_id = user_id,post_id = post_id,time = time)
        collection.save()
        collections = Collection.objects.filter(post_id = post_id)
        dic ={
            'flag':1,
            'msg':'收藏成功!',
            'follower':len(collections),
        }
    dic_json = json.dumps(dic)
    response=HttpResponse()
    response['Content-Type']="text/javascript;charset='UTF-8'"
    response.write(dic_json)
    return HttpResponse(response)

def cancel_collect(request,user_id,post_id):
    try:
        collection = Collection.objects.get(user_id = user_id,post_id=post_id)
        collection.delete()
        collections = Collection.objects.filter(post_id = post_id)
        dic ={
            'flag':1,
            'msg':'取消收藏成功!',
            'collection':len(collections),
        }
    except Collection.DoesNotExist:
        dic ={
            'flag':0,
            'msg':'未收藏此文章!',
        }
    dic_json = json.dumps(dic)
    response=HttpResponse()
    response['Content-Type']="text/javascript;charset='UTF-8'"
    response.write(dic_json)
    return HttpResponse(response)

def listing(request,user_id):
    list = Collection.objects.filter(user_id = user_id).order_by('-time')
    post_list = []
    if len(list):
        for item in list:
            try:
                post = Post.objects.get(id = item.post_id)
                post.text = parse_html(post.text)
                post.text = post.text[0:len(post.text)/3]+'...'
                post_list.append(post)
            except Post.DoesNotExist:
                pass
    return render_to_response('list4.html',{'post_list_0':post_list,'flag':'1'})

