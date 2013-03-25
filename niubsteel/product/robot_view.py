from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from comment.models import Comment
from models import Product, Save
import json, utils
from config.tags import MODEL_TAGS, TRADEMARK_TAGS

@csrf_exempt
def robot_push(request):
    try:
        robot_user = User.objects.get(username='niubsteel')
    except User.DoesNotExist:
        robot_user = User.objects.create_user(username='niubsteel', email='niubsteel@hupur.com', password='niubsteel')

    products = json.loads(request.POST['items'])
    for product in products:
        try:
            p = Product.objects.get(
                user=robot_user,
                url=product['url'],
                model=product['model'],
                trademark=product['trademark'],
                spec=product['spec'],
                producer=product['producer'],
                stock_location=product['stock_location'],
                store_name=product['provider'])
            p.price = float(utils.number_only(product['price']))
            p.weight = product['weight']
            p.save()
        except Product.DoesNotExist:
            p = Product.objects.create(
                user=robot_user,
                url=product['url'],
                model=product['model'],
                trademark=product['trademark'],
                spec=product['spec'],
                producer=product['producer'],
                stock_location=product['stock_location'],
                store_name=product['provider'],
                price=float(utils.number_only(product['price'])),
                weight=product['weight'])
            Save.objects.create(
                product=p,
                user=robot_user,
                collection=robot_user.collections[0]
            )
            trademark_tags = ['#'+_[0] for _ in utils.analyze_tags(p.trademark, TRADEMARK_TAGS)]
            model_tags = ['#'+_[0] for _ in utils.analyze_tags(p.model, MODEL_TAGS)]
            Comment.objects.create(
                user=robot_user,
                product=p,
                text=' '.join(trademark_tags + model_tags)
            )

        print p

    return HttpResponse(0)
