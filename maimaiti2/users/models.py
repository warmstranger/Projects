#coding=utf-8

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        user = self.model(username=username, email=UserManager.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.activated = True
        user.save()
        return user

class User(AbstractBaseUser):
    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'

    username = models.CharField(max_length=40, verbose_name=u'用户名', unique=True, db_index=True)
    email = models.CharField(max_length=40, verbose_name=u'邮箱', unique=True, db_index=True)
    connected_user = models.IntegerField(verbose_name=u'关联用户', default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __unicode__(self):
        return '%s[%s]' % (self.username, self.email)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.email

    def is_staff(self):
        return True

    def has_module_perms(self, module):
        return True

    def has_perm(self, perm):
        return True

class Profile(models.Model):
    class Meta:
        verbose_name = u'用户资料'
        verbose_name_plural = u'用户资料'

    user = models.OneToOneField(User, verbose_name=u'用户')
    image = models.ImageField(verbose_name=u'头像', blank=True, null=True, upload_to='profile_images')

    def __unicode__(self):
        return '%s' % self.user.username


