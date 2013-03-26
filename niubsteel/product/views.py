#coding: utf-8

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from models import Product, Save
from users.models import Profile
from collection.models import Collection
from comment.models import Comment
from apis import analyze, search as api_search
from json import dumps

def index(request):
    return redirect(trending)

def search(request):
    q = request.GET.get('q', '')
    context = {
        'result': api_search(q)[:100],
        'q': q,
    }
    return render_to_response('search.html', context, RequestContext(request))


def trending(request):
    return redirect(recent_posts)

def recent_posts(request):

    recent_products = Product.objects.order_by('-time')[:99]
    context = {
        'page_title': u'火爆资源',
        'products': recent_products
    }
    return render_to_response('products.html', context, RequestContext(request))


def popular(request):
    return render_to_response('single_product.html')


@login_required
def post_url(request):
    context = {}
    if request.method == 'GET':
        error = request.GET.get('error', '')
        if error:
            context['error'] = error
        return render_to_response('post/url.html', context, RequestContext(request))


@login_required
def post_analyze(request):
    context = {}
    if request.method == 'GET':
        context['url'] = request.GET.get('url', '')
        return render_to_response('post/analyze.html', context, RequestContext(request))

    result = {}
    url = request.POST.get('url', '')
    try:
        product = analyze(url)
        data = product.__dict__.copy()
        data.pop('_state')
        result['success'] = True
        result['data'] = data
    except Exception as ex:
        result['success'] = False
        result['data'] = ex

    return HttpResponse(dumps(result))


@login_required
def post_preview(request):
    context = {
        'title': request.POST.get('preview_title', ''),
        'url': request.POST.get('preview_url', ''),
        'image': request.POST.get('preview_image', ''),
        'price': request.POST.get('preview_price', ''),
    }
    return render_to_response('post/preview.html', context, RequestContext(request))


@login_required
def post_finish(request):
    try:
        product = Product(
            user=request.user,
            title=request.POST.get('title', ''),
            url=request.POST.get('url', ''),
            image=request.POST.get('image', ''),
            price=request.POST.get('price', '')
        )
        product.save()

        context = {
            'product': product,
        }

    except Exception as ex:
        context = {
            'error': ex
        }
    return render_to_response('post/finish.html', context, RequestContext(request))


@login_required
@csrf_exempt
def save_product(request):
    if request.method == 'GET':
        return HttpResponse('NEED POST')

    product_id = int(request.POST.get('product_id'))
    collection_name = request.POST.get('collection_name', '')
    comment = request.POST.get('comment', '')

    result = { 'success': False }

    try:
        product = Product.objects.get(id=product_id)

        if collection_name:
            try:
                collection = Collection.objects.get(user=request.user, name=collection_name)
            except Collection.DoesNotExist:
                collection = Collection.objects.create(user=request.user, name=collection_name)

            if Save.objects.filter(user=request.user, collection=collection, product=product).exists():
                raise Exception('已保存过了')

            Save.objects.create(user=request.user, collection=collection, product=product)

        if comment:
            Comment.objects.create(user=request.user, product=product, text=comment)

        result['success'] = True
    except Exception as ex:
        result['data'] = str(ex)

    return HttpResponse(dumps(result))


def product_save_detail(request, product_id, save_id):
    product = Product.objects.get(id=product_id)
    try:
        # Add product to check whether this save is valid.
        first_save = Save.objects.get(pk=save_id, product=product)
    except Exception:
        # Invalid save, so redirect to product detail.
        return redirect(product_detail, product_id)
    try:
        first_comment = Comment.objects.filter(product=product)[0]
    except Exception:
        first_comment = None
    saved_in_col = []
    if first_save:
        saved_in_col = Save.objects.filter(collection=first_save.collection)
    # TODO how many user directly saved product from this saver?
    try:
        recent_saves = Save.objects.filter(product=product).order_by('-time')[0:8]
    except Exception:
        recent_saves = []
    save_count = Save.objects.filter(product=product).count()
    try:
        comments = Comment.objects.filter(product=product).order_by('-time')[0:10]
        comments_count = Comment.objects.filter(product=product).count()
    except Exception:
        comments, comments_count = [], 0

    context = {
        'product': product,
        'original': False,
        'saver': first_save.user,
        'requester': request.user,
        'first_comment': first_comment,
        'first_save': first_save,
        'recent_saves': recent_saves,
        'save_count': save_count,
        'comments': comments,
        'comments_more': comments_count > 10,
        'saved_in_col': saved_in_col
    }
    return render_to_response('single_product.html', context, RequestContext(request))


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        first_comment = Comment.objects.filter(user=product.user, product=product)[0]
    except Exception:
        first_comment = None
    try:
        first_save = Save.objects.filter(user=product.user, product=product)[0]
    except Exception:
        first_save = None
    saved_in_col = []
    if first_save:
        saved_in_col = Save.objects.filter(collection=first_save.collection)[:20]
    # TODO how many user directly saved product from the poster?
    try:
        recent_saves = Save.objects.filter(product=product).order_by('-time')[:8]
    except Exception:
        recent_saves = []
    save_count = Save.objects.filter(product=product).count()
    try:
        comments = Comment.objects.filter(product=product).order_by('-time')[:10]
        comments_count = Comment.objects.filter(product=product).count()
    except Exception:
        comments, comments_count = [], 0

    context = {
        'product': product,
        'original': True,
        'saver': first_save.user,
        'requester': request.user,
        'first_comment': first_comment,
        'first_save': first_save,
        'recent_saves': recent_saves,
        'save_count': save_count,
        'comments': comments,
        'comments_more': comments_count > 10,
        'saved_in_col': saved_in_col
    }
    return render_to_response('single_product.html', context, RequestContext(request))


def product_savers(request, product_id):
    return HttpResponse(0)
