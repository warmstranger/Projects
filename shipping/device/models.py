#coding=utf8

__author__ = 'konglingkai'

from django.db import models

from daily.models import Department

class Device(models.Model):
    class Meta:
        verbose_name = u'设备'
        verbose_name_plural = u'设备'

    number = models.CharField(max_length=40, verbose_name=u'资产编号')
    name = models.CharField(max_length=40, verbose_name=u'设备名称')
    type = models.CharField(max_length=40, verbose_name=u'设备型号')
    description = models.TextField(default='', verbose_name=u'设备描述')
    capital = models.BooleanField(default=False, verbose_name=u'是否固定资产')
    date = models.DateField(verbose_name=u'日期')

    def __unicode__(self):
        return '[%s] %s' % (self.number, self.description)

class SpecialDevice(Device):
    class Meta:
        verbose_name = u'特种设备'
        verbose_name_plural = u'特种设备'

    old_number = models.CharField(max_length=40, verbose_name=u'老编号')
    safe_start = models.CharField(max_length=40, verbose_name=u'安全起重吨位')
    production_date = models.DateField(verbose_name=u'生产日期')
    manufacturer = models.CharField(max_length=100, verbose_name=u'制造厂商')
    license_unit = models.CharField(max_length=100, verbose_name=u'质监发证单位')
    license_period = models.CharField(max_length=50, verbose_name=u'证书有效期')
    license_number = models.CharField(max_length=100, verbose_name=u'证书编号/车辆证号')
    department = models.ForeignKey(Department, verbose_name=u'使用部门')
    memo = models.TextField(default='', verbose_name=u'备注')
    scan_document = models.FileField(upload_to='SpecialDevice')
