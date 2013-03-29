# Create your views here.
#encoding: utf-8
from models import Post
from advertisement.models import Advertisement
from comment.models import Comment
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import random
import time
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = Post.objects.order_by('-time')[:12]
    advertisements = Advertisement.objects.order_by('-time')[:4]
    for post in posts:
        post.time = post.time.strftime('%Y-%m-%d %H:%M:%S')
    return render_to_response('home2.html', {'posts':posts,'advertisements':advertisements})

@csrf_protect
def detail(request,id):
    try:
        post = Post.objects.get(id = id)
        post.time = post.time.strftime('%Y-%m-%d %H:%M:%S')
    except Post.DoesNotExist:
         return redirect('/home/')
    comments = Comment.objects.filter(post_id = id).order_by('-time')
    context = {'post':post,'comments':comments}
    return render_to_response('post_detail.html', RequestContext(request, context))

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
    previous_page_number = posts.previous_page_number()
    context = {
        "post_list_0": post_list_0,
        "post_list_1": post_list_1,
        "post_list_2": post_list_2,
        "has_previous":has_previous,
        "has_next":has_next,
        "page":page,
        "next_page_number":next_page_number,
        "previous_page_number":previous_page_number
    }
    return render_to_response('list.html',context)

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