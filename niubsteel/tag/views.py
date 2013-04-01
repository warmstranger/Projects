#coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext

from tag.models import Tag, ProductMention
from users.models import User

def top_tags(request):
    tags = Tag.objects.filter()[:20]
    context = {
        'page_title': u'热门品种',
        'lists': tags
    }
    return render_to_response('lists.html', context, RequestContext(request))

def list_mentions(request, username):
    user = User.objects.get(username=username)
    mentions = ProductMention.objects.filter(mention=user)
    context = {
        'target_user': user,
        'selected_tab': 2,
        'products': [mention.from_comment.product for mention in mentions]
    }
    return render_to_response('users/profile.html', context, RequestContext(request))

def tag_detail(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    context = {
        'page_title': '#%s' % tag_name,
        'products': tag.products[:100]
    }
    return render_to_response('products.html', context, RequestContext(request))