# Create your views here.

from models import Post
from advertisement.models import Advertisement
from comment.models import Comment
from django.shortcuts import render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    posts = Post.objects.order_by('-time')[:12]
    advertisements = Advertisement.objects.order_by('-time')[:4]
    for post in posts:
        post.time = post.time.strftime('%Y-%m-%d %H:%M:%S')
    return render_to_response('home.html', {'posts':posts,'advertisements':advertisements})

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
    page_size = 25
    post_list = Post.objects.all().order_by('-time')
    paginator = Paginator(post_list, page_size)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('list.html', {"posts": posts})