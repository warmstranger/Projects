from django.db import models
from users.models import User

class Store(models.Model):
    owner = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=40)
    url = models.URLField(default=u'')
    phone = models.CharField(max_length=40, default=u'')

    def __unicode__(self):
        return '%s[%s]' % (self.name, self.url)

    @property
    def products(self):
        from product.models import Product
        return Product.objects.filter(store_name=self.name).order_by('-time')

    @property
    def preview_products(self):
        return self.products[:5]

    @property
    def url(self):
        from django.core.urlresolvers import reverse
        return reverse('store.views.store_detail', kwargs={
            'store_name': self.name,
        })

    @property
    def followers(self):
        from follow.models import StoreFollow
        return [follow.user for follow in StoreFollow.objects.filter(following=self)]

    def is_user_following(self, user):
        from follow.models import StoreFollow
        return StoreFollow.objects.filter(user=user, following=self).exists()
