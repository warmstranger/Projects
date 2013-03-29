# Create your views here.
#coding utf-8
from comment.models import Comment
from django.shortcuts import render_to_response,redirect
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

def delete(request,id):
    try:
        comment = Comment.objects.get(id = id)
        comment.delete()
    except Comment.DoesNotExist:
        pass
    return render_to_response('home2.html')

def listing(request,user_id):
    comments = Comment.objects.filter(user_id = user_id)
    return render_to_response('home2.html',{'comments':comments})