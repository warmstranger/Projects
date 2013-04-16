#coding=utf-8

from django.db import models

from django.contrib.auth.models import User

class UserMapping(models.Model):
    class Meta:
        verbose_name = u'用户映射'
        verbose_name_plural = u'用户映射'

    user = models.ForeignKey(User, verbose_name=u'用户')
    original_user_id = models.IntegerField( verbose_name=u'接口用户')

    def __unicode__(self):
        return '%s => %s' % (self.original_user_id, self.user_id)

