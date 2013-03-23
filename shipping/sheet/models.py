#coding=utf8

__author__ = 'konglingkai'

from django.db import models
from django.contrib.auth.models import User

from daily.models import Provider, Department
from device.models import Device

class AssignWork(models.Model):
    class Meta:
        verbose_name = u'派工单'
        verbose_name_plural = u'派工单'

    number = models.CharField(max_length=40, verbose_name=u'维修编号')
    assign_work_number = models.CharField(max_length=40, verbose_name=u'派工单编号')
    contractor = models.ForeignKey(Provider, verbose_name=u'维修队伍')
    assign_work_date = models.DateField(verbose_name=u'派工日期')
    require_finish_date = models.DateField(verbose_name=u'要求完工日期')
    description = models.TextField(default='', verbose_name=u'维修描述')
    capital = models.ForeignKey(Device, verbose_name=u'固定资产编号', null=True, blank=True, related_name='assign_capital')
    location = models.ForeignKey(Device, verbose_name=u'维修位置', null=True, blank=True, related_name='assign_location')
    device = models.ForeignKey(Device, verbose_name=u'所属设备', null=True, blank=True, related_name='assign_device')
    manager = models.ForeignKey(User, verbose_name=u'维修主管')
    safety_hint = models.CharField(max_length=40, verbose_name=u'安全提示')
    acceptance = models.CharField(max_length=40, verbose_name=u'验收要求')
    scan_document = models.FileField(upload_to=u'assign_work', verbose_name=u'扫描件')
    date = models.DateField(verbose_name=u'日期')

    def __unicode__(self):
        return u'维修编号:%s, 派工单编号%s' % (self.number, self.assign_work_number)

class Acceptance(models.Model):
    class Meta:
        verbose_name = u'验收单'
        verbose_name_plural = u'验收单'

    requirement = models.CharField(max_length=100, verbose_name=u'验收要求')
    other_requirement = models.CharField(max_length=100, verbose_name=u'其他要求')
    status = models.CharField(max_length=100, verbose_name=u'验收情况')
    check_date = models.DateField(verbose_name=u'验收日期')
    finish_date = models.DateField(verbose_name=u'完工日期')

    def __unicode__(self):
        return '[%s] %s' % (
            self.check_date,
            self.status
        )

class Bidding(models.Model):
    class Meta:
        verbose_name = u'报价单'
        verbose_name_plural = u'报价单'

    description = models.TextField(verbose_name=u'工作内容')
    date = models.DateField(verbose_name=u'日期')

    def __unicode__(self):
        return '[%s] %s' % (
            self.date,
            self.description
        )

class Estimate(models.Model):
    class Meta:
        verbose_name = u'估价单'
        verbose_name_plural = u'估价单'

    estimator = models.ForeignKey(User, verbose_name=u'估价员')
    description = models.TextField(verbose_name=u'工作内容')
    date = models.DateField(verbose_name=u'日期')
    scan_document = models.FileField(upload_to=u'estimation', verbose_name=u'扫描件')

    def __unicode__(self):
        return '[%s] %s' % (
            self.date,
            self.description
        )

class Payment(models.Model):
    class Meta:
        verbose_name = u'支付费用'
        verbose_name_plural = u'支付费用'

    date = models.DateField(verbose_name=u'申请日期')
    department = models.ForeignKey(Department, verbose_name=u'申请部门')
    description = models.TextField(verbose_name=u'支付内容')
    operator = models.ForeignKey(User, verbose_name=u'经办人')
    account = models.CharField(max_length=20, verbose_name=u'账号')
    provider = models.ForeignKey(Provider, verbose_name=u'支付对象')
    amount = models.IntegerField(verbose_name=u'支付金额')
    number = models.CharField(max_length=40, verbose_name=u'费用编号')
    category = models.CharField(max_length=40, verbose_name=u'类别')
    will_pay = models.BooleanField(default=True, verbose_name=u'是否支付')

    def __unicode__(self):
        return '[%s] %s' % (
            self.date,
            self.description
        )