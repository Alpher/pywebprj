#-*- coding:utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Alpher'

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	"""板块类型"""
	ctgy_code = models.CharField(verbose_name=u'板块类型编码', max_length=50)
	ctgy_desc = models.CharField(verbose_name=u'板块类型描述', max_length=200)

	def __unicode__(self):
		return self.ctgy_desc

	class Meta:
		verbose_name = u'板块类型'
		verbose_name_plural = u'板块类型'

class CbbsCategory(models.Model):
	"""主题类型"""
	cbbsctgy_code = models.CharField(verbose_name=u'主题类型编码', max_length=50)
	cbbsctgy_desc = models.CharField(verbose_name=u'主题类型描述', max_length=200)

	def __unicode__(self):
		return self.cbbsctgy_desc

	class Meta:
		verbose_name = u'主题类型'
		verbose_name_plural = u'主题类型'


class Cbbs(models.Model):
	"""社区主题"""
	title = models.CharField(verbose_name=u'主题', max_length=50)
	username = models.ForeignKey(User,verbose_name=u'账号')
	category = models.ForeignKey(Category,verbose_name=u'所属板块')
	cbbsctgy = models.ForeignKey(CbbsCategory,verbose_name=u'主题类型')
	content = models.TextField(verbose_name=u'内容')
	create_ts = models.DateTimeField(verbose_name=u'发布时间',auto_now_add=True)
	update_ts = models.DateTimeField(verbose_name=u'更新时间',auto_now=True)
	viewers = models.IntegerField(verbose_name=u'浏览数',default=0)
	comnts = models.IntegerField(verbose_name=u'评论数',default=0)
	priority = models.IntegerField(verbose_name=u'优先级',default=0)
	wanted_score = models.IntegerField(verbose_name=u'悬赏积分',default=0)
	wanted_ovddt = models.DateTimeField(verbose_name=u'悬赏过期时间',blank=True,null=True)
	tips_score = models.IntegerField(verbose_name=u'打赏积分',default=0)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'社区主题'
		verbose_name_plural = u'社区主题'
			

class Comments(models.Model):
	"""评论"""
	cbbs = models.ForeignKey(Cbbs,verbose_name=u'主题')
	username = models.ForeignKey(User,verbose_name=u'账号')
	comment = models.TextField(verbose_name=u'评论内容')
	create_ts = models.DateTimeField(verbose_name=u'评论时间',auto_now_add=True)
	ref_comment = models.ForeignKey('self',verbose_name=u'引用评论')
	favors = models.IntegerField(verbose_name=u'支持数',default=0)
	kicks = models.IntegerField(verbose_name=u'反对数',default=0)
	is_reward = models.BooleanField(verbose_name=u'是否获赏',default=False)
	reward_dt = models.DateTimeField(verbose_name=u'获赏时间',blank=True,null=True)
	reward_score = models.IntegerField(verbose_name=u'获赏积分',default=0)

	def __unicode__(self):
		return self.id

	class Meta:
		verbose_name = u'评论'
		verbose_name_plural = u'评论'


class CbbsTips(models.Model):
	"""打赏日志"""
	cbbs = models.ForeignKey(Cbbs,verbose_name=u'主题')
	comnt = models.ForeignKey(Comments,verbose_name=u'评论')
	from_user = models.ForeignKey(User,verbose_name=u'打赏账号',related_name='+')
	to_user = models.ForeignKey(User,verbose_name=u'获赏账号',related_name='+')
	score = models.IntegerField(verbose_name=u'积分')
	op_ts = models.DateTimeField(verbose_name=u'打赏时间',auto_now_add=True)

	def __unicode__(self):
		return self.id

	class Meta:
		verbose_name = u'打赏日志'
		verbose_name_plural = u'打赏日志'
			

class Announcement(models.Model):
	"""社区公告"""
	title = models.CharField(verbose_name=u'公告标题', max_length=50)
	anncm = models.TextField(verbose_name=u'公告内容')
	username = models.ForeignKey(User,verbose_name=u'账号')
	is_curanncm = models.BooleanField(verbose_name=u'是否设为当前公告',default=False)
	create_ts = models.DateTimeField(verbose_name=u'发布时间',auto_now_add=True)
	update_ts = models.DateTimeField(verbose_name=u'更新时间',auto_now=True)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = u'公告'
		verbose_name_plural = u'公告'
			

# To Do
# class CbbsAdminLog(models.Model):
# 	"""管理日志"""
# 	pass

# To Do
# class CbbsUserLog(models.Model):
# 	"""用户操作日志"""
# 	pass
