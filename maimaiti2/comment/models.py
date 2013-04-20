#coding=utf-8

from django.db import models

from django.conf import settings
from post.models import Post

class Comment(models.Model):
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'

    time = models.DateTimeField(auto_now=True, verbose_name=u'时间')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=u'用户')
    post = models.ForeignKey(Post, verbose_name=u'帖子')
    text = models.CharField(max_length=1000, verbose_name=u'正文')

    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.text[:10])
