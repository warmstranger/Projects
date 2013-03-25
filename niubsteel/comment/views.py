#coding=utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Comment
from product.models import Product
from json import dumps
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def save_comment(request, product_id):
    if request.method == 'GET':
        return HttpResponse('NEED POST')

    comment = request.POST.get('comment', '')
    result = {'success': False}
    if comment:
        try:
            product = Product.objects.get(id=product_id)
            Comment.objects.create(user=request.user, product=product, text=comment)

            result['success'] = True
        except Exception as ex:
            result['data'] = str(ex)
    else:
        result['data'] = 'Comment body is empty'

    return HttpResponse(dumps(result))


def list_comments(request, product_id):
    product = Product.objects.get(pk=product_id)
    # offset is the earliest comment id loaded.
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 10))
    try:
        comments = Comment.objects.filter(pk__lt=offset, product=product).order_by('-time')[:limit]
        comments_count = Comment.objects.filter(pk__lt=offset, product=product).count()
        comments_more = comments_count > limit
        context = {'comments': comments, 'comments_more': comments_more}
        return render_to_response('comment_list.html', context, RequestContext(request))
    except Exception:
        return HttpResponse(0)

