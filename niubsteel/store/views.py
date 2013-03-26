#coding=utf-8

from django.template import RequestContext
from django.shortcuts import render_to_response

from models import Store
from users.models import User

def top_stores(request):
    limit = request.GET.get('limit', 30)
    stores = Store.objects.all()[:limit]
    context = {
        'page_title': u'热门的商店',
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
    title = store_name
    if store.owner:
        title += '老板:' +  store.owner.profile.full_name
    context = {
        'page_title': title,
        'products': store.products[:100],
    }
    return render_to_response('products.html', context, RequestContext(request))