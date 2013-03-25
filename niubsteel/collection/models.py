#coding=utf-8

from django.db import models
from users.models import User

class Collection(models.Model):
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    name = models.CharField(max_length=40)
    description = models.TextField(default=u'')

    def __unicode__(self):
        return self.name

    @property
    def products(self):
        from product.models import Save
        saves = Save.objects.filter(collection=self)
        return [save.product for save in saves]

    @property
    def preview_products(self):
        return self.products[:5]

    @property
    def url(self):
        from django.core.urlresolvers import reverse
        return reverse('collection.views.collection_detail', kwargs={
            'username': self.user.username,
            'collection_name': self.name,
        })

    @property
    def followers(self):
        from follow.models import CollectionFollow
        return [follow.user for follow in CollectionFollow.objects.filter(following=self)]

    def is_user_following(self, user):
        from follow.models import CollectionFollow
        return CollectionFollow.objects.filter(user=user, following=self).exists()

from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def create_default_collections(sender, **kwargs):
    user = kwargs['instance']
    saved = kwargs['created']
    if not saved:
        return

    Collection.objects.create(user=user, name=u'我的收藏')
    Collection.objects.create(user=user, name=u'便宜货')