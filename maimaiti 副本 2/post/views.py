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
from HTMLParser import HTMLParser
import random
import time
import json

def home(request):
    posts = Post.objects.order_by('-time')[:12]
    advertisements = Advertisement.objects.order_by('-time')[:4]
    i = 2
    follow_dic = {}
    while i<=5:
        try:
            userFollow = UserFollow.objects.get(user_id = 1,following_id = i)
            follow_dic[i]="1"
        except UserFollow.DoesNotExist:
            follow_dic[i]="0"
            pass
        i += 1
    for post in posts:
        post.time = post.time.strftime('%Y-%m-%d %H:%M:%S')
    page_size =12
    list_size = 60
    post_list = Post.objects.all().order_by('-time')[0:list_size]
    for post in post_list:
        post.text = parse_html(post.text)
        post.text = post.text[0:len(post.text)/3]+'...'
    print post_list.count()
    context = {
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
        user_id = 1
        try:
            Collection.objects.get(user_id = user_id,post_id = post.id)
            collect_flag = '1'
        except Collection.DoesNotExist:
            collect_flag = '0'
    except Post.DoesNotExist:
         return redirect('/home/')
    comments = Comment.objects.filter(post_id = id).order_by('-time')
    for comment in comments:
        comment.time = comment.time.strftime('%Y年%m月%d日 %H:%M:%S')
    context = {'post':post,'comments':comments,'collect_flag':collect_flag}
    return render_to_response('post_detail2.html', RequestContext(request, context))

def listing(request,page):
    page_size = 12
    list_size = 36
    post_list = Post.objects.all().order_by('-time')
    paginator = Paginator(post_list, list_size)
    try:
        posts = paginator.page(page)
        page = page
    except PageNotAnInteger:
        posts = paginator.page(1)
        page = 1
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        page = paginator.num_pages
    post_list_0 = posts[0:page_size]
    post_list_1 = posts[page_size:2*page_size]
    post_list_2 = posts[2*page_size:3*page_size]
    has_previous = posts.has_previous()
    has_next = posts.has_next()
    next_page_number = posts.next_page_number()
    if has_previous:
        previous_number = posts.previous_page_number()
    else:
        previous_number = 0
    context = {
        "post_list_0": post_list_0,
        "post_list_1": post_list_1,
        "post_list_2": post_list_2,

        "has_previous":has_previous,
        "has_next":has_next,
        "page":page,
        "next_page_number":next_page_number,
        "previous_page_number":previous_number
    }
    return render_to_response('list2.html',context)

def listing_test(request):
    page_size =12
    list_size = 96
    post_list = Post.objects.all().order_by('-time')[0:list_size]
    for post in post_list:
        post.text = parse_html(post.text)
        post.text = post.text[0:len(post.text)/3]+'...'
    context = {
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
    print post_list[page_size:2*page_size]
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
    post_list = []
    if len(list):
        for item in list:
            posts = Post.objects.filter(author_id = item.following_id).order_by('-time')
            for post in posts:
                post.text = parse_html(post.text)
            if len(posts):
                for post in posts:
                    post_dic = {post.time:post}
                    post_list.append(post_dic)
    post_list.sort(reverse=True)
    return render_to_response('follow.html',{'post_list':post_list})

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