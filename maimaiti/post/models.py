#coding=utf-8

from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    class Meta:
        verbose_name = u'帖子'
        verbose_name_plural = u'帖子'

    time = models.DateTimeField(auto_now=True, verbose_name=u'时间')
    author = models.ForeignKey(User, verbose_name=u'发帖人')
    title = models.CharField(max_length=100, verbose_name=u'标题')
    cover_image = models.ImageField(upload_to='covers', verbose_name=u'封面')
    text = models.TextField(verbose_name=u'正文')

    def __unicode__(self):
        return '%s: %s' % (self.user.username, self.title)

class Attachment(models.Model):
    class Meta:
        verbose_name = u'附件'
        verbose_name_plural = u'附件'

    post = models.ForeignKey(Post, verbose_name=u'帖子')
    file = models.FileField(upload_to='attachments', verbose_name=u'文件')

    def __unicode__(self):
        return '%s: %s' % (self.post.title, self.file.name)

class Link(models.Model):
    class Meta:
        verbose_name = u'产品链接'
        verbose_name_plural = u'产品链接'

    post = models.ForeignKey(Post, verbose_name=u'帖子')
    link = models.URLField(verbose_name=u'链接')

    def __unicode__(self):
        return '%s: %s' % (self.post.title, self.link)


