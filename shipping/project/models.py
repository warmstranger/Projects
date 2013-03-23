#coding=utf8

__author__ = 'konglingkai'

from django.db import models
from django.contrib.auth.models import User
from sheet.models import AssignWork, Acceptance, Bidding, Estimate, Payment
from django.contrib import admin

class Project(models.Model):
    class Meta:
        verbose_name = u'项目'
        verbose_name_plural = u'项目'

    type = models.IntegerField(verbose_name=u'项目类型', choices=(
        (0, u'基建'),
        (1, u'技改'),
    ), default=0)

#    number = models.CharField(max_length=40, verbose_name=u'项目编号', unique=True)
    name = models.CharField(max_length=40, verbose_name=u'项目名称', unique=True)
    description = models.TextField(default='', verbose_name=u'项目简介')
    manager = models.ForeignKey(User, verbose_name=u'项目主管')
    investment = models.IntegerField(default=0, verbose_name=u'项目投资')
    reply = models.TextField(default='', verbose_name=u'项目批复')
    date = models.DateField(verbose_name=u'日期')

    def __unicode__(self):
        return '[%s] %s' % (self.id, self.name)


class ProjectItem(models.Model):
    project = models.ForeignKey(Project, verbose_name=u'项目')
    date = models.DateField(verbose_name=u'日期')
    parent=models.ForeignKey('self',default='',null=True,blank=True)
    rank=models.IntegerField(default="-1",null=True,blank=True)
    index=models.IntegerField(default='-1',null=True,blank=True)
    def __unicode__(self):
        return '%s' %self.date



class Event(ProjectItem):
    class Meta:
        verbose_name = u'事件'
        verbose_name_plural = u'事件'

    description = models.TextField(default='', verbose_name=u'描述')
    def __unicode__(self):
            return '%s' %self.date

class AssignWork(ProjectItem):
    class Meta:
        verbose_name = u'派工'
        verbose_name_plural = u'派工'

    assign_work_sheet = models.ForeignKey(AssignWork, verbose_name=u'派工单', null=True, blank=True)
    acceptance_sheet = models.ForeignKey(Acceptance, verbose_name=u'验收单', null=True, blank=True)
    bidding_sheet = models.ForeignKey(Bidding, verbose_name=u'报价单', null=True, blank=True)
    estimate_sheet = models.ForeignKey(Estimate, verbose_name=u'派工单', null=True, blank=True)
    payment = models.ForeignKey(Payment, verbose_name=u'支付费用', null=True, blank=True)
    def __unicode__(self):
        return '%s' %self.date

class ClaimMaterial(ProjectItem):
    class Meta:
        verbose_name = u'领料'
        verbose_name_plural = u'领料'

    claimer = models.ForeignKey(User, verbose_name=u'领料人')
    price = models.FloatField(default=0, verbose_name=u'费用')
    description = models.TextField(default='', verbose_name=u'描述')
    def __unicode__(self):
        return '%s' %self.date

class Contract(ProjectItem):
    class Meta:
        verbose_name = u'合同'
        verbose_name_plural = u'合同'

    name = models.CharField(max_length=40, verbose_name=u'名称')
    description = models.TextField(default='', verbose_name=u'描述')
    scan_document = models.FileField(upload_to=u'contract')
    payment = models.ForeignKey(Payment, verbose_name=u'支付费用', null=True, blank=True)
    def __unicode__(self):
        return '%s' %self.name


