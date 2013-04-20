#coding=utf-8

from django.db import models

from post.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):
    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'

    time = models.DateTimeField(auto_now=True, verbose_name=u'时间')
    user = models.ForeignKey(User, verbose_name=u'用户')
    post = models.ForeignKey(Post, verbose_name=u'帖子')
    text = models.TextField(verbose_name=u'正文')
    show = models.BooleanField(default=True)

    def __unicode__(self):
        return '[%s] %s: %s' % (self.show, self.user.username, self.text[:80])
