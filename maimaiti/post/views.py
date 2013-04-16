# Create your views here.
#encoding: utf-8
from models import Post
from advertisement.models import Advertisement
from comment.models import Comment
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from follow.models import UserFollow
from collection.models import Collection
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.utils import timezone
from HTMLParser import HTMLParser
import random
import time
import json
import urllib
import urllib2

def home(request):
    user = request.user
    posts = Post.objects.order_by('-time')[:12]
    advertisements = Advertisement.objects.order_by('-time')[:4]
    i = 2
    follow_dic = {}
    if user.is_active:
        while i<=5:
            userFollow_list = UserFollow.objects.filter(following_id = i)
            count = len(userFollow_list)
            try:
                UserFollow.objects.get(following_id = i,user_id = user.id)
                follow_flag = '1'
            except UserFollow.DoesNotExist:
                follow_flag = '0'
            follow_dic[i]={count:follow_flag}
            i += 1
    else:
        while i<=5:
            userFollow_list = UserFollow.objects.filter(following_id = i)
            follow_dic[i]= {len(userFollow_list):'0'}
            i+= 1
    for post in posts:
        post.time = post.time.strftime('%Y-%m-%d %H:%M:%S')
    page_size =12
    list_size = 60
    post_list = Post.objects.all().order_by('-time')[0:list_size]
    for post in post_list:
        temp = parse_html(post.text)
        post.preview = temp[0:len(temp)/3]+'...'
    print post_list.count()
    context = {
        'user':user,
        'posts':posts,
        'advertisements':advertisements,
        'follow_dic':follow_dic,
        "post_list_0": post_list[0:page_size],
        "post_list_1": post_list[page_size:2*page_size],
        "post_list_2": post_list[2*page_size:3*page_size],
        "post_list_3":post_list[3*page_size:4*page_size],
        "post_list_4":post_list[4*page_size:5*page_size],
        #"post_list_5":post_list[5*page_size:6*page_size],
        #"post_list_6":post_list[6*page_size:7*page_size],
        #"post_list_7":post_list[7*page_size:8*page_size],
        }
    return render_to_response('home3.html', context)

@csrf_protect
def detail(request,id):
    try:
        post = Post.objects.get(id = id)
        post.time = post.time.strftime('%Y-%m-%d %H:%M:%S')
        if request.user.is_active:
            try:
                Collection.objects.get(user_id = request.user.id,post_id = post.id)
                collect_flag = '1'
            except Collection.DoesNotExist:
                collect_flag = '0'
        else:
            collect_flag = '0'
    except Post.DoesNotExist:
         return redirect('/home/')
    comments = Comment.objects.filter(post_id = id).order_by('-time')
    for comment in comments:
        comment.time = comment.time.strftime('%Y年%m月%d日 %H:%M:%S')
    context = {'post':post,'comments':comments,'collect_flag':collect_flag,'user':request.user}
    return render_to_response('post_detail2.html', RequestContext(request, context))

def listing(request,page):
    PAGE_SIZE = 12
    page = int(page)
    post_list = Post.objects.all().order_by('-time')[page*PAGE_SIZE:(page+1)*PAGE_SIZE]
    posts_dic = {'posts':[]}
    for post in post_list:
        temp = parse_html(post.text)
        post.preview = temp[0:len(temp)/3]+'...'
        dic = {
            'id':post.id,
            'time':post.time.strftime('%Y-%m-%d %H:%M:%S'),
            'text':post.preview,
            'title':post.title,
            'author_id':post.author_id,
            'cover_image':str(post.cover_image),
        }
        posts_dic['posts'].append(dic)
    posts_dic['length'] = PAGE_SIZE
    dic_json = json.dumps(posts_dic)
    response=HttpResponse()
    response['Content-Type']="text/javascript;charset='UTF-8'"
    response.write(dic_json)
    return HttpResponse(response)

def listing_test(request):
    page_size =12
    list_size = 96
    post_list = Post.objects.all().order_by('-time')[0:list_size]
    for post in post_list:
        temp = parse_html(post.text)
        post.preview = temp[0:len(temp)/3]+'...'
    context = {
        "user":request.user,
        "post_list_0": post_list[0:page_size],
        "post_list_1": post_list[page_size:2*page_size],
        "post_list_2": post_list[2*page_size:3*page_size],
        "post_list_3":post_list[3*page_size:4*page_size],
        "post_list_4":post_list[4*page_size:5*page_size],
        "post_list_5":post_list[5*page_size:6*page_size],
        "post_list_6":post_list[6*page_size:7*page_size],
        "post_list_7":post_list[7*page_size:8*page_size],
        "flag":'0',
    }
    return render_to_response('list4.html',context)

@csrf_exempt
def upload(request):
    UPLOAD_FILE_PATH ="/Users/jacky/Projects/maimaiti/post/static/upload/"
    FILTER_IMAGE_TYPE = {'jpeg','jpg','gif','png','bmp'}
    file = request.FILES["imgFile"]
    file_attribute = file.name.split('.')
    file_type = file_attribute[1]
    if file_type in FILTER_IMAGE_TYPE:
        file_name = time.strftime('%Y%m%d%H%M%S', time.localtime()) + str(random.randint(1, 1000))
        des = open(UPLOAD_FILE_PATH + file_name +"."+file_type, 'wb+')
        for chunk in file.chunks():
            des.write(chunk)
            des.close()
        dic = {
            "error" : 0,
            "url" : "/static/upload/"+file_name+"."+file_type,
        }
    else:
        dic = {
            "error" : 1,
            "message":'请上传正确的图片格式',
        }
    return HttpResponse(json.dumps(dic))

def feed(request,user_id):
    list = UserFollow.objects.filter(user_id = user_id)
    user = User.objects.get(id=user_id)
    post_list = []
    if len(list):
        for item in list:
            posts = Post.objects.filter(author_id = item.following_id).order_by('-time')
            for post in posts:
                temp = parse_html(post.text)
                post.preview = temp[0:len(temp)/3]+'...'
            if len(posts):
                for post in posts:
                    post_dic = {post.time:post}
                    post_list.append(post_dic)
    post_list.sort(reverse=True)
    print post_list
    return render_to_response('feed.html',{'post_list':post_list,'follow_list':list,'user':user})

def list_buyer_post(request,user_id,page):
    PAGE_SIZE = 5
    posts = Post.objects.filter(author_id = user_id).order_by('time')
    author = User.objects.get(id=user_id)
    post_list =[]
    for post in posts:
        temp = parse_html(post.text)
        post.preview = temp[0:len(temp)/3]+'...'
    if len(posts):
        for post in posts:
            post_dic = {post.time:post}
            post_list.append(post_dic)
    paginator = Paginator(post_list,PAGE_SIZE)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('post_list.html',{'post_list':posts,'author':author,'user':request.user})

def parse_html(html):
    html=html.strip()
    html=html.strip("\n")
    result=[]
    parse=HTMLParser()
    parse.handle_data=result.append
    parse.feed(html)
    parse.close()
    str = ''.join(result)
    str2 = ''.join(str.split())
    return str2
