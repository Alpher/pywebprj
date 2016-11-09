#-*- coding:utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Alpher'

from django.db import models

# Create your models here.

class RewardsType(models.Model):
	"""奖品类型模型"""
	rewardstype_code = models.CharField(verbose_name=u'奖品类型编码', max_length=50)
	rewardstype_desc = models.CharField(verbose_name=u'奖品类型描述', max_length=200)

	def __unicode__(self):
		return self.rewardstype_desc

	class Meta:
		verbose_name = u'奖品类型'
		verbose_name_plural = u'奖品类型'


class Rewards(models.Model):
	"""奖品模型"""
	reward_code = models.CharField(verbose_name=u'奖品编码', max_length=50)
	reward_desc = models.CharField(verbose_name=u'奖品描述', max_length=200)
	reward_type = models.ForeignKey(RewardsType, verbose_name=u'奖品类型')
	reward_cost = models.IntegerField(verbose_name=u'抵扣积分', null=True, blank=True)
	reward_effdt = models.DateField(verbose_name=u'生效日期')
	reward_enddt = models.DateField(verbose_name=u'失效日期')

	def __unicode__(self):
		return self.reward_desc

	class Meta:
		verbose_name = u'奖品'
		verbose_name_plural = u'奖品'


class MyRewards(models.Model):
	"""中奖模型"""
	username = models.CharField(max_length=50, verbose_name=u'中奖账号')
	reward = models.ForeignKey(Rewards, verbose_name=u'奖品')
	reward_dt = models.DateField(verbose_name=u'中奖时间', null=True, blank=True)
	isExchg = models.IntegerField(verbose_name=u'是否已领奖', default=0)
	exchg_name = models.CharField(max_length=50, verbose_name=u'领奖人姓名', null=True, blank=True)
	exchg_phone = models.CharField(max_length=11, verbose_name=u'领奖人手机', null=True, blank=True)
	exchg_addr = models.CharField(max_length=1000, verbose_name=u'领奖人地址', null=True, blank=True)
	addr_code = models.CharField(max_length=10, verbose_name=u'领奖人邮编', null=True, blank=True)
	express_id = models.CharField(max_length=100, verbose_name=u'快递单号', null=True, blank=True)
	express_name = models.CharField(max_length=200, verbose_name=u'快递公司名称', null=True, blank=True)
	update_ts = models.DateTimeField(verbose_name=u'最后更新时间',auto_now=True)

	def __unicode__(self):
		return "中奖序号:%s--账号:%s" %(str(self.id),self.username)

	class Meta:
		verbose_name = u'中奖纪录'
		verbose_name_plural = u'中奖纪录'