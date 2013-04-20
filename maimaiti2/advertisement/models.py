#coding=utf-8

from django.db import models

class Advertisement(models.Model):
    class Meta:
        verbose_name = u'广告'
        verbose_name_plural = u'广告'

    enabled = models.BooleanField(default=True, verbose_name=u'使用')
    image = models.FileField(upload_to='advertisement', verbose_name=u'图片')
    order = models.IntegerField(default=0, verbose_name=u'排序')

    def __unicode__(self):
        return '[%s]: [%d] - %s' % (self.enabled, self.order, self.image.name)
