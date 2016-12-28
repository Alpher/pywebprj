#-*- coding:utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Alpher'

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EcardType(models.Model):
	"""卡品类型模型"""
	ecardtype_code = models.CharField(verbose_name=u'卡品类型编码', max_length=50)
	ecardtype_desc = models.CharField(verbose_name=u'卡品类型描述', max_length=200)

	def __unicode__(self):
		return self.ecardtype_desc

	class Meta:
		verbose_name = u'卡品类型'
		verbose_name_plural = u'卡品类型'

class ActionType(models.Model):
	"""活动类型模型"""
	actiontype_code = models.CharField(verbose_name=u'活动类型编码', max_length=50)
	actiontype_desc = models.CharField(verbose_name=u'活动类型描述', max_length=200)

	def __unicode__(self):
		return self.actiontype_desc

	class Meta:
		verbose_name = u'活动类型'
		verbose_name_plural = u'活动类型'

class RewardsType(models.Model):
	"""奖品类型模型"""
	rewardstype_code = models.CharField(verbose_name=u'奖品类型编码', max_length=50)
	rewardstype_desc = models.CharField(verbose_name=u'奖品类型描述', max_length=200)

	def __unicode__(self):
		return self.rewardstype_desc

	class Meta:
		verbose_name = u'奖品类型'
		verbose_name_plural = u'奖品类型'

class Ecards(models.Model):
	"""卡品模型"""
	ecardtype = models.ForeignKey(EcardType, verbose_name=u'卡品类型')
	ecardnum = models.CharField(verbose_name=u'卡号', max_length=200)
	ecardpsw = models.CharField(verbose_name=u'卡密', max_length=200)
	isValid = models.BooleanField(verbose_name=u'是否可用')

	def __unicode__(self):
		return self.ecardnum

	class Meta:
		verbose_name = u'卡品清单'
		verbose_name_plural = u'卡品清单'

class Actions(models.Model):
	"""活动"""
	action_code = models.CharField(max_length=50, verbose_name=u'活动编码')
	action_desc = models.CharField(verbose_name=u'活动描述', max_length=200)
	action_type = models.ForeignKey(ActionType,verbose_name=u'活动类型')
	is_cur_action = models.BooleanField(verbose_name=u'是否当前活动')
	create_ts = models.DateTimeField(verbose_name=u'创建时间',auto_now_add=True)

	def __unicode__(self):
		return self.action_desc

	class Meta:
		verbose_name=u'活动'
		verbose_name_plural=u'活动'

class Rewards(models.Model):
	"""奖品模型"""
	reward_code = models.CharField(verbose_name=u'奖品编码', max_length=50)
	reward_desc = models.CharField(verbose_name=u'奖品描述', max_length=200)
	reward_type = models.ForeignKey(RewardsType, verbose_name=u'奖品类型')
	action_type = models.ForeignKey(ActionType, verbose_name=u'活动类型')
	isphonecard = models.BooleanField(verbose_name=u'是否手机充值卡', default=False)
	reward_cost = models.IntegerField(verbose_name=u'抵扣积分', null=True, blank=True)
	reward_cost_ori = models.IntegerField(verbose_name=u'打拆前抵扣积分', null=True, blank=True)
	reward_effdt = models.DateField(verbose_name=u'生效日期')
	reward_enddt = models.DateField(verbose_name=u'失效日期')
	reward_nums = models.IntegerField(verbose_name=u'奖品总数')
	reward_left = models.IntegerField(verbose_name=u'奖品剩余数')
	reward_rmk = models.CharField(verbose_name=u'奖品备注', max_length=1000, null=True, blank=True)
	reward_pic = models.ImageField(verbose_name=u'奖品图片',upload_to='smarket/',default=r'static/images/smarket/default.jpg')

	def __unicode__(self):
		return self.reward_desc

	class Meta:
		verbose_name = u'奖品'
		verbose_name_plural = u'奖品'


class MyRewards(models.Model):
	"""中奖模型"""
	username = models.CharField(max_length=50, verbose_name=u'中奖账号')
	action = models.ForeignKey(Actions,verbose_name=u'活动')
	reward = models.ForeignKey(Rewards, verbose_name=u'奖品')
	reward_dt = models.DateField(verbose_name=u'中奖日期', null=True, blank=True)
	isExchg = models.BooleanField(verbose_name=u'是否已领奖')
	exchg_dt = models.DateField(verbose_name=u'兑换/领奖日期', null=True, blank=True)
	exchg_name = models.CharField(max_length=50, verbose_name=u'领奖人姓名', null=True, blank=True)
	exchg_phone = models.CharField(max_length=11, verbose_name=u'领奖人手机', null=True, blank=True)
	exchg_addr = models.CharField(max_length=1000, verbose_name=u'领奖人地址', null=True, blank=True)
	addr_code = models.CharField(max_length=10, verbose_name=u'领奖人邮编', null=True, blank=True)
	express_id = models.CharField(max_length=100, verbose_name=u'快递单号', null=True, blank=True)
	express_name = models.CharField(max_length=200, verbose_name=u'快递公司名称', null=True, blank=True)
	ecardnum = models.CharField(verbose_name=u'虚拟卡品卡号', max_length=200, null=True, blank=True)
	update_ts = models.DateTimeField(verbose_name=u'最后更新时间',auto_now=True)

	def __unicode__(self):
		return "中奖序号:%s--账号:%s" %(str(self.id),self.username)

	class Meta:
		verbose_name = u'中奖纪录'
		verbose_name_plural = u'中奖纪录'

class PhoneNumType(models.Model):
	"""运营商手机号段"""
	prefixnumtype = models.ForeignKey(EcardType, verbose_name=u'卡品类型')
	prefixnum = models.CharField(verbose_name=u'手机号前三位', max_length=11)


	def __unicode__(self):
		return self.prefixnum

	class Meta:
		verbose_name = u'运营商手机号段'
		verbose_name_plural = u'运营商手机号段'

class ActionConf(models.Model):
	"""活动配置"""
	action = models.ForeignKey(Actions,verbose_name=u'活动')
	reward = models.ForeignKey(Rewards,verbose_name=u'奖品')
	rw_order = models.IntegerField(verbose_name=u'奖品排序')
	act_base = models.IntegerField(verbose_name=u'概率基数')
	rwd_s_idx = models.IntegerField(verbose_name=u'概率范围开始数')
	rwd_e_idx = models.IntegerField(verbose_name=u'概率范围结束数')

	def __unicode__(self):
		return str(self.id)

	class Meta:
		verbose_name=u'活动配置'
		verbose_name_plural=u'活动配置'

class LotteryLog(models.Model):
	"""抽奖日志"""
	username = models.ForeignKey(User,verbose_name=u'账号')
	action = models.ForeignKey(Actions,verbose_name=u'活动')
	opt_ts = models.DateTimeField(verbose_name=u'抽奖时间',auto_now_add=True)
	random_num = models.IntegerField(verbose_name=u'抽奖随机数')
	opt_remark = models.CharField(verbose_name=u'备注', max_length=200)

	def __unicode__(self):
		return str(self.id)

	class Meta:
		verbose_name=u'抽奖日志'
		verbose_name_plural=u'抽奖日志'
			
		
			
			