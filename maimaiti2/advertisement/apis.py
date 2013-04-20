
from restful.decorators import api

@api
def get_advertisement():
    from models import Advertisement
    ads = Advertisement.objects.filter(enabled=True).order_by('order')
    return [ad.image.url for ad in ads]
