#coding=utf8

from django.db import models
from post.models import Post
from comment.models import Comment

class Tag(models.Model):
    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

    name = models.CharField(max_length=40, verbose_name=u'名称')

class PostTag(models.Model):
    class Meta:
        verbose_name = u'帖子标签'
        verbose_name_plural = u'帖子标签'

    tag = models.ForeignKey(Tag, verbose_name=u'标签')
    post = models.ForeignKey(Post, verbose_name=u'帖子')

class CommentTag(models.Model):
    class Meta:
        verbose_name = u'评论标签'
        verbose_name_plural = u'评论标签'

    tag = models.ForeignKey(Tag, verbose_name=u'标签')
    comment = models.ForeignKey(Comment, verbose_name=u'评论')
