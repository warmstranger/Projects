from django.http import HttpResponse

from models import User, Store, Collection, Tag
from models import PeopleFollow, CollectionFollow, StoreFollow, TagFollow

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
