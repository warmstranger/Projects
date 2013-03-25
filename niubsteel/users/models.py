#coding=utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password, login_type=0):
        if not username:
            raise ValueError(u'用户名为空')

        if not email:
            raise ValueError(u'邮箱为空')

        if not password:
            raise ValueError(u'密码为空')

        user = self.model(username=username, email=UserManager.normalize_email(email))
        user.set_password(password)
        user.login_type = login_type
        user.save()
        return user

    def create_superuser(self, username, email, password, login_type = 0):
        user = self.create_user(username, email, password, login_type)
        user.activated = True
        user.save()
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=40, verbose_name=u'用户名', unique=True, db_index=True)
    email = models.CharField(max_length=40, verbose_name=u'邮箱', db_index=True)
    activated = models.BooleanField(default=False)
    login_type = models.IntegerField(default=0)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __unicode__(self):
        return '%s[%s]' % (self.username, self.email)

    def get_full_name(self):
        return self.__unicode__()

    def get_short_name(self):
        return self.email

    def is_staff(self):
        return True

    def has_module_perms(self, module):
        return True

    def has_perm(self, perm):
        return True

    @property
    def name(self):
        return self.username

    @property
    def products(self):
        from product.models import Save
        saves = Save.objects.filter(user=self)
        return [save.product for save in saves]

    @property
    def preview_products(self):
        return self.products[:5]

    @property
    def has_taobao_account(self):
        return SNWProfile.objects.filter(user=self,type=2).exists()
    @property
    def taobao_account(self):
        return SNWProfile.objects.get(user=self,type=2)

    @property
    def has_store(self):
        from store.models import Store
        return Store.objects.filter(owner=self).exists()
    @property
    def store(self):
        from store.models import Store
        return Store.objects.get(owner=self)

    @property
    def has_weibo_account(self):
        return SNWProfile.objects.filter(user=self,type=1).exists()

    @property
    def weibo_account(self):
        return SNWProfile.objects.get(user=self,type=1)

    @property
    def has_qq_account(self):
        return SNWProfile.objects.filter(user=self,type=3).exists()

    @property
    def qq_account(self):
        return SNWProfile.objects.get(user=self,type=3)

    @property
    def url(self):
        from django.core.urlresolvers import reverse
        return reverse('users.views.profile', kwargs={
            'username': self.username,
        })

    @property
    def collections(self):
        from collection.models import Collection
        return Collection.objects.filter(user=self)

    @property
    def mentions(self):
        from tag.models import ProductMention
        return ProductMention.objects.filter(mention=self)

    @property
    def stores(self):
        from store.models import Store
        return Store.objects.filter(owner=self)

    @property
    def following_people(self):
        from follow.models import PeopleFollow
        return [follow.following for follow in PeopleFollow.objects.filter(user=self)]

    @property
    def following_stores(self):
        from follow.models import StoreFollow
        return [follow.following for follow in StoreFollow.objects.filter(user=self)]

    @property
    def followers(self):
        from follow.models import PeopleFollow
        return [follow.user for follow in PeopleFollow.objects.filter(following=self)]

    def is_user_following(self, user):
        from follow.models import PeopleFollow
        return PeopleFollow.objects.filter(user=user, following=self).exists()


class Profile(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(blank=True, null=True, upload_to='profile_images')
    full_name = models.CharField(max_length=40, default=u'')
    location = models.CharField(max_length=140, default=u'')
    website = models.URLField(default=u'')
    description = models.TextField(default=u'')

    def __unicode__(self):
        return '%s' % self.full_name

from django.dispatch import receiver
from django.db.models.signals import post_save
@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    instance = kwargs['instance']
    created = kwargs['created']
    if created:
        Profile.objects.create(user=instance)

class SNWProfile(models.Model):
    user = models.ForeignKey(User)
    #1:weibo, 2: taobao
    type = models.IntegerField(null=False)
    snw_id = models.CharField(max_length=40,null=False)
    snw_nick = models.CharField(max_length=40,null=False)
