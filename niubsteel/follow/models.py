from django.db import models

from users.models import User
from store.models import Store
from collection.models import Collection
from tag.models import Tag

class PeopleFollow(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='related_peoplefollow_user')
    following = models.ForeignKey(User, related_name='related_peoplefollow_following')

class StoreFollow(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    following = models.ForeignKey(Store)

class CollectionFollow(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    following = models.ForeignKey(Collection)

class TagFollow(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    following = models.ForeignKey(Tag)


