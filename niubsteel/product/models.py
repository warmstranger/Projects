from django.db import models
from users.models import User
from store.models import Store
from collection.models import Collection

class ProductMeta(models.Model):
    model_tags = models.CharField(max_length=100, db_index=True)
    trademark_tags = models.CharField(max_length=100, db_index=True)
    width = models.FloatField(db_index=True)
    thick = models.FloatField(db_index=True)

    best_price = models.FloatField(default=100000)

    @property
    def products(self):
        return Product.objects.filter(meta=self).order_by('price')

    @property
    def best_offer(self):
        return self.products[0]

    def __unicode__(self):
        return '%s %s, %f * %f' % (self.model_tags, self.trademark_tags, self.width, self.thick)

class Product(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    url = models.CharField(max_length=600)

    model = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    trademark = models.CharField(max_length=100)

    producer = models.CharField(max_length=100, default=u'')
    stock_location = models.CharField(max_length=100, default=u'')

    price = models.FloatField()
    weight = models.CharField(max_length=40, default=u'')

    store_name = models.CharField(max_length=200, default=u'')
    meta = models.ForeignKey(ProductMeta, db_index=True, null=True, blank=True)

    @property
    def saves(self):
        return Save.objects.filter(product=self)

    @property
    def store(self):
        return Store.objects.get(name=self.store_name)

    def __unicode__(self):
        return '[%s]%s, %s: %f from %s' % (self.time, self.model, self.trademark, self.price, self.store.name)


class Save(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    collection = models.ForeignKey(Collection)
    product = models.ForeignKey(Product)

    def __unicode__(self):
        return '%s by %s' % (self.product.trademark, self.user.username)


from django.dispatch import receiver
from django.db.models.signals import post_save
from config.tags import MODEL_TAGS, TRADEMARK_TAGS
import utils

@receiver(post_save, sender=Product)
def analyze_product(sender, **kwargs):
    product = kwargs['instance']
    saved = kwargs['created']
    if not saved:
        return

    if not Store.objects.filter(name=product.store_name).exists():
        Store.objects.create(name=product.store_name, url='')

    width, thick =  utils.analyze_spec(product.spec)
    trademark_tags = [_[0].upper() for _ in utils.analyze_tags(product.trademark, TRADEMARK_TAGS)]
    trademark_tags.sort()
    model_tags = [_[0].upper() for _ in utils.analyze_tags(product.model, MODEL_TAGS)]
    model_tags.sort()

    meta, create = ProductMeta.objects.get_or_create(
        width=width, thick=thick,
        trademark_tags=' '.join(trademark_tags),
        model_tags=' '.join(model_tags))

    if create:
        print 'meta created:', meta

    product.meta = meta
    product.save()

    meta.best_price = meta.best_offer.price
    meta.save()
