#-*- coding:utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Alpher'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class AcctType(models.Model):
	"""账号类型定义"""
	acct_type_lev = models.IntegerField(default=1)
	acct_type_dec = models.CharField(max_length=50)

	def __unicode__(self):
		return self.acct_type_dec

class AcctStatus(models.Model):
	"""账号状态定义"""
	acctst_lev = models.IntegerField(default=1)
	acctst_dec = models.CharField(max_length=50)

	def __unicode__():
		return self.acctst_dec

class Profile(models.Model):
	"""用户模型扩展"""
	user = models.OneToOneField(User)
	scores = models.IntegerField(default=0)
	title = models.CharField(max_length=50)
	nickname = models.CharField(max_length=50)
	sex = models.CharField(max_length=10)
	birth = models.DateField(null=True,blank=True)
	region = models.CharField(max_length=20)
	acct_type = models.ForeignKey(AcctType)
	status = models.ForeignKey(AcctStatus)

	def __unicode__(self):
		return self.user.username

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = Profile.objects.get_or_create(user=instance)  
  
post_save.connect(create_user_profile, sender=User)
