#coding=utf8

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from models import Collection
from users.models import User
from json import dumps

@login_required
@csrf_exempt
def new_collection(request):
    context = {}
    if request.method == 'GET':
        return render_to_response('collection/new_collection.html', context, RequestContext(request))

    user = request.user
    name = request.POST.get('new_collection_name', '')
    result = {
        'success': True
    }
    if Collection.objects.filter(user=user, name=name).exists():
        result['success'] = False
        result['data'] = name + u'已存在'
    else:
        try:
            collection = Collection.objects.create(user=user, name=name)
            result['data'] = collection.name
        except Exception as ex:
            result['success'] = False
            result['data'] = str(ex)
    return HttpResponse(dumps(result))

def top_collections(request):
    collections = Collection.objects.filter()[:20]
    context = {
        'page_title': u'热门的收藏',
        'lists': collections
    }
    return render_to_response('lists.html', context, RequestContext(request))

def list_collections(request, username):
    user = User.objects.get(username=username)
    context = {
        'target_user': user,
        'selected_tab': 1,
        'lists': user.collections[:20]
    }
    return render_to_response('users/profile.html', context, RequestContext(request))

def collection_detail(request, username, collection_name):
    user = User.objects.get(username=username)
    collection = Collection.objects.get(user=user, name=collection_name)
    context = {
        'page_title': '@%s' % username,
        'products': collection.products[:100]
    }
    return render_to_response('products.html', context, RequestContext(request))


def get_collection(request, username, collection_id):
    user = User.objects.get(username=username)
    collection = Collection.objects.get(pk=collection_id)
    context = {
        'page_title': '@%s' % username,
        'products': collection.products[:100]
    }
    return render_to_response('products.html', context, RequestContext(request))
