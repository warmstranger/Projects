#coding=utf-8

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from models import Store
from users.models import User


def top_stores(request):
    limit = request.GET.get('limit', 30)
    stores = Store.objects.all()[:limit]
    context = {
        'page_title': u'火爆店铺',
        'lists': stores,
    }
    return render_to_response('lists.html', context, RequestContext(request))


def list_stores(request, username):
    user = User.objects.get(username=username)
    context = {
        'target_user': user,
        'selected_tab': 3,
        'lists': user.stores[:20]
    }
    return render_to_response('users/profile.html', context, RequestContext(request))


def store_detail(request, store_name):
    store = Store.objects.get(name=store_name)
    context = {
        'page_title': store_name,
        'store': store,
        'products': store.products[:100],
    }
    return render_to_response('single_store.html', context, RequestContext(request))


def store_claim(request, store_name):
    store = Store.objects.get(name=store_name)
    context = {
        'page_title': '',
        'store': store
    }
    return render_to_response('claim_store.html', context, RequestContext(request))


def store_followers(request, store_name):
    return HttpResponse(0)