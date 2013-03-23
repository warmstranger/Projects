#coding=utf8

__author__ = 'konglingkai'

from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
    class Meta:
        verbose_name = u'分包商'
        verbose_name_plural = u'分包商'

    name = models.CharField(max_length=40, verbose_name=u'名称', unique=True)

    def __unicode__(self):
        return self.name

class Department(models.Model):
    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门'

    name = models.CharField(max_length=40, verbose_name=u'名称', unique=True)

    def __unicode__(self):
        return self.name

class EnergyLog(models.Model):
    class Meta:
        verbose_name = u'能源记录'
        verbose_name_plural = u'能源记录'

    date = models.DateField(verbose_name=u'日期')
    user = models.ForeignKey(User, verbose_name=u'员工')
    type = models.IntegerField(verbose_name=u'种类', choices=(
        (0, u'电力'),
        (1, u'柴油'),
        (2, u'压缩空气'),
    ))
    amount = models.IntegerField(default=0, verbose_name=u'费用')

    def __unicode__(self):
        return '[%s] %s: %d' % (
            self.date,
            self.type,
            self.amount
        )

class WorkLog(models.Model):
    class Meta:
        verbose_name = u'工作记录'
        verbose_name_plural = u'工作记录'

    date = models.DateField(verbose_name=u'日期')
    user = models.ForeignKey(User, verbose_name=u'员工')
    log = models.TextField(default='', verbose_name=u'工作日志')

    def __unicode__(self):
        return '[%s] %s: %s' % (
            self.date,
            self.user,
            self.log
        )

class ToolLog(models.Model):
    class Meta:
        verbose_name = u'工具记录'
        verbose_name_plural = u'工具记录'

    date = models.DateField(verbose_name=u'日期')
    type = models.CharField(max_length=40, verbose_name=u'类型')
    description = models.TextField(default='', verbose_name=u'描述')
    status = models.IntegerField(default=0, verbose_name=u'状态', choices=(
        (0, u'购置'),
        (1, u'转移'),
        (2, u'报废'),
    ))
    owner = models.ForeignKey(User, verbose_name=u'所有者')
    amount = models.IntegerField(default=0, verbose_name=u'费用')

    def __unicode__(self):
        return '[%s] %s: %d' % (
            self.date,
            self.owner,
            self.amount
        )
