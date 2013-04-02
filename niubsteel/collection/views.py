#coding=utf8

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from models import Collection
from users.models import User
from json import dumps
from product.models import Save
from django.contrib import messages

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


def create_collection(request):
    user = request.user
    name = request.POST.get('new_collection_name', '')
    desc = request.POST.get('new_collection_desc', '')

    if Collection.objects.filter(user=user, name=name).exists():
        message = name + u'已存在'
        messages.add_message(request, messages.ERROR, message)
    else:
        try:
            Collection.objects.create(user=user, name=name, description=desc)
            message = u'恭喜！你现在可以收藏东西到 %s 里了' % name
            messages.add_message(request, messages.SUCCESS, message)
        except Exception as ex:
            message = str(ex)
            messages.add_message(request, messages.ERROR, message)
    return redirect(list_collections, user.username)


def top_collections(request):
    collections = Collection.objects.filter()[:20]
    context = {
        'page_title': u'人气收藏',
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
    try:
        collection = Collection.objects.get(user=user, name=collection_name)
    except Collection.DoesNotExist:
        return redirect('users.views.profile', username)
    context = {
        'collection': collection,
        'page_title': '@%s' % username,
        'products': collection.products[:100]
    }
    return render_to_response('single_collection.html', context, RequestContext(request))


@csrf_exempt
def collection_edit(request, collection_id):
    item = Collection.objects.get(pk=collection_id)
    result = {'success': True}
    try:
        for key, val in request.POST.iteritems():
            if hasattr(item, key):
                setattr(item, key, val)
        item.save()
    except Exception as e:
        result['success'] = False
        result['data'] = str(e)

    return HttpResponse(dumps(result))


@csrf_exempt
def collection_delete(request, username, collection_id):
    collection = Collection.objects.get(pk=collection_id)
    Save.objects.filter(collection=collection).delete()
    collection.delete()
    message = u'收藏列表 %s 已删除！' % collection.name
    messages.add_message(request, messages.SUCCESS, message)
    return redirect(list_collections, username)


def collection_followers(request, username, collection_name):
    return HttpResponse(0)
