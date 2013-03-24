#coding=utf8

from django.db import models

from django.contrib.auth.models import User
from tag.models import Tag

class UserFollow(models.Model):
    class Meta:
        verbose_name = u'买手关注'
        verbose_name_plural = u'买手关注'

    time = models.DateTimeField(auto_now=True, verbose_name=u'时间')
    user = models.ForeignKey(User, related_name='user_follow_user', verbose_name=u'用户')
    following = models.ForeignKey(User, related_name='user_follow_following', verbose_name=u'关注')

class TagFollow(models.Model):
    class Meta:
        verbose_name = u'标签关注'
        verbose_name_plural = u'标签关注'

    time = models.DateTimeField(auto_now=True, verbose_name=u'时间')
    user = models.ForeignKey(User, verbose_name=u'用户')
    following = models.ForeignKey(Tag, verbose_name=u'关注')
