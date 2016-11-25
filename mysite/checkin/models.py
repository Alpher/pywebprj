#-*- coding:utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Alpher'

from django.db import models

# Create your models here.

class UScoreOpType(models.Model):
	"""用户积分操作类型"""
	type_code = models.CharField(verbose_name=u'操作类型编码', max_length=50)
	type_desc = models.CharField(verbose_name=u'操作类型描述', max_length=200)

	def __unicode__(self):
		return self.type_desc

	class Meta:
		verbose_name = u'用户积分操作类型'
		verbose_name_plural = u'用户积分操作类型'

class UScoreLog(models.Model):
	"""用户积分操作历史"""
	username = models.CharField(max_length=50, verbose_name=u'账号')
	score = models.IntegerField(verbose_name=u'入账积分')
	usot = models.ForeignKey(UScoreOpType, verbose_name=u'操作类型')
	opby = models.CharField(max_length=50, verbose_name=u'操作账号')
	remark = models.CharField(verbose_name=u'备注', max_length=1000, null=True, blank=True)
	update_ts = models.DateTimeField(verbose_name=u'操作时间',auto_now=True)

	def __unicode__(self):
		return "用户:%s,日志ID:%s" %(self.username,self.id)

	class Meta:
		verbose_name = u'用户积分操作历史'
		verbose_name_plural = u'用户积分操作历史'

class UScoreOv(models.Model):
	"""用户积分统计预览"""
	username = models.CharField(max_length=50, verbose_name=u'账号')
	days_in_a_row = models.IntegerField(verbose_name=u'连续签到天数',default=0)
	days_in_month = models.IntegerField(verbose_name=u'本月签到天数',default=0)
	days_in_year = models.IntegerField(verbose_name=u'本年签到天数',default=0)
	accum_score = models.IntegerField(verbose_name=u'签到累计积分',default=0)
	last_chkin_dt = models.DateField(verbose_name=u'上次签到日期',auto_now=True)
	last_chkin_score = models.IntegerField(verbose_name=u'上次签到积分',default=0)

	def __unicode__(self):
		return self.username

	class Meta:
		verbose_name = u'用户积分统计预览'
		verbose_name_plural = u'用户积分统计预览'