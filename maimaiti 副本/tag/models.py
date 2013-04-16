#coding=utf-8

from django.db import models
from post.models import Post
from comment.models import Comment

class Tag(models.Model):
    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'

    name = models.CharField(max_length=40, verbose_name=u'名称')

    def __unicode__(self):
        return self.name

class PostTag(models.Model):
    class Meta:
        verbose_name = u'帖子标签'
        verbose_name_plural = u'帖子标签'

    tag = models.ForeignKey(Tag, verbose_name=u'标签')
    post = models.ForeignKey(Post, verbose_name=u'帖子')

    def __unicode__(self):
        return '%s: %s' % (self.tag.name, self.post.title)

class CommentTag(models.Model):
    class Meta:
        verbose_name = u'评论标签'
        verbose_name_plural = u'评论标签'

    tag = models.ForeignKey(Tag, verbose_name=u'标签')
    comment = models.ForeignKey(Comment, verbose_name=u'评论')

    def __unicode__(self):
        return '%s: %s' % (self.tag.name, self.comment.text[:10])