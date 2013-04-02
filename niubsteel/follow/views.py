from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from models import User, Store, Collection, Tag
from models import PeopleFollow, CollectionFollow, StoreFollow, TagFollow

from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required

def follow_collection(request, username, collection_name):
    if not request.user.is_active:
        return HttpResponse(2)

    try:
        user = User.objects.get(username=username)
        collection = Collection.objects.get(user=user, name=collection_name)
        try:
            CollectionFollow.objects.get(user=request.user, following=collection).delete()
        except CollectionFollow.DoesNotExist:
            CollectionFollow.objects.create(user=request.user, following=collection)

        return HttpResponse(0)
    except:
        return HttpResponse(1)

def follow_user(request, username):
    if not request.user.is_active:
        return HttpResponse(2)

    try:
        user = User.objects.get(username=username)
        try:
            PeopleFollow.objects.get(user=request.user, following=user).delete()
        except PeopleFollow.DoesNotExist:
            PeopleFollow.objects.create(user=request.user, following=user)

        return HttpResponse(0)
    except:
        return HttpResponse(1)

def follow_tag(request, tag_name):
    if not request.user.is_active:
        return HttpResponse(2)

    try:
        tag = Tag.objects.get(name=tag_name)
        try:
            TagFollow.objects.get(user=request.user, following=tag).delete()
        except TagFollow.DoesNotExist:
            TagFollow.objects.create(user=request.user, following=tag)

        return HttpResponse(0)
    except:
        return HttpResponse(1)

def follow_store(request, store_name):
    if not request.user.is_active:
        return HttpResponse(2)

    try:
        store = Store.objects.get(name=store_name)
        try:
            StoreFollow.objects.get(user=request.user, following=store).delete()
        except StoreFollow.DoesNotExist:
            StoreFollow.objects.create(user=request.user, following=store)

        return HttpResponse(0)
    except:
        return HttpResponse(1)



from datetime import datetime
from datetime import timedelta
from product.models import Save
from comment.models import Comment
from product.models import Product
from follow.models import StoreFollow
from follow.models import CollectionFollow
@login_required
def feed(request):
    # from time A to time B, show new posts to store, user's new posts, user's new comments, user's saves,get user's new follows
    # event, time, type.
    #getP people's events
    events = []
    context = {'people_events': events}
    context['user'] = request.user
    time_start = datetime.now()
    time_end = datetime.now() - timedelta(3)

    for people_following in PeopleFollow.objects.filter(user=request.user):
        person = people_following.following
        args = {'user':person, 'time__gt':time_end, 'time__lt':time_start}

        for person_save in Save.objects.filter(**args)[:20]:
            events.append({'id':len(events),'event_type': 'person_save','time':person_save.time,
                           'person_save': person_save, 'user':person_save.user})

        for person_comment in Comment.objects.filter(**args):
            comment_list = []
            comment_list.append(person_comment)
            events.append({'id':len(events),'event_type': 'person_comment','time': person_comment.time,
                           'person_comment': comment_list,
                           'product':person_comment.product,'user':person_comment.user })

        for person_follow in PeopleFollow.objects.filter(**args):
            print(person_follow.following.username)
            events.append({'id':len(events),'user':person,'event_type': 'person_follow','time': person_follow.time, 'person_follow': person_follow})

        for person_product in Product.objects.filter(**args)[:20]:
            events.append({'id':len(events),'event_type': 'person_product','time':person_product.time, 'person_product': person_product,'user':person })


    for store_follow in StoreFollow.objects.filter(user=request.user):
        args = {'store_name':store_follow.following.name, 'time__gt':time_end, 'time__lt':time_start}
        store_products = Product.objects.filter(**args).order_by('time').reverse()
        if store_products.exists():
            number = len(store_products)
            latest_time = store_products[0].time
            events.append({'id':len(events),'event_type':'store_products','number':number, 'time':latest_time, 'store': store_follow.following, 'store_products':store_products[:10]})

    for collection_follow in CollectionFollow.objects.filter(user=request.user):
        args = {'collection':collection_follow.following, 'time__gt':time_end, 'time__lt':time_start}
        collection_saves = Save.objects.filter(**args).order_by('time').reverse()

        if collection_saves.exists():
            latest_time = collection_saves[0].time
            collection_products = []
            for save in collection_saves[:10]:
                collection_products.append(save.product)
            events.append({'id':len(events),'event_type': 'collection_saves', 'time': latest_time,'number':len(collection_saves),'collection_products': collection_products, 'collection' : collection_follow.following})
    def get_attr(name):
        def inner_func(o):
            return o[name]
        return inner_func
    events.sort(key=get_attr('time'),reverse=True)

    return render_to_response('feed.html',context,RequestContext(request))

