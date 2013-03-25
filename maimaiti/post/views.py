# Create your views here.

from models import Post
from django.shortcuts import render_to_response
def home(request):
    posts = Post.objects.order_by('-time')[:12]
    for post in posts:
        post.time = post.time.strftime('%Y-%m-%d %H:%M:%S')
    return render_to_response('home.html', {'posts':posts})