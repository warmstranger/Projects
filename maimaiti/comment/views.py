# Create your views here.
#coding utf-8
from comment.models import Comment
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import datetime

def add(request):
    context = {}
    user_id = request.POST['user_id']
    post_id = request.POST['post_id']
    text = request.POST['text']
    time = datetime.time
    comment = Comment(user_id = user_id,post_id = post_id,text = text,time = time)
    comment.save()
    return redirect('/post/detail/'+post_id)
