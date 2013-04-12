#coding=utf-8

from django.db import models

from django.contrib.auth.models import User
from post.models import  Post

class Collection(models.Model):
    class Meta:
        verbose_name = u'收藏'
        verbose_name_plural = u'收藏'

    time = models.DateTimeField(auto_now=True, verbose_name=u'时间')
    user = models.ForeignKey(User, verbose_name=u'用户')
    post = models.ForeignKey(Post, verbose_name=u'帖子')

    def __unicode__(self):
        return '%s => %s' % (self.user.username, self.post.title)
