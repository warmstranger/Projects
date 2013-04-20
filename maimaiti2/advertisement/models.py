#coding=utf-8

from django.db import models

class Advertisement(models.Model):
    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = u'广告'

    time = models.DateTimeField(auto_now=True, verbose_name=u'时间')
    image = models.FileField(upload_to='advertisement', verbose_name=u'图片')

    def __unicode__(self):
        return '%s: %s' % (self.time, self.image.name)
