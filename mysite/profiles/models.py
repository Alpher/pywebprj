#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.db import models

# Create your models here.

from django.contrib.auth.models import User  
from django.contrib.auth.admin import UserAdmin  
import datetime

class AcctType(models.Model):
    """账号类型定义"""
    acct_type_lev = models.IntegerField(verbose_name=u'账号类型ID')
    acct_type_dec = models.CharField(verbose_name=u'账号类型名称',max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.acct_type_dec

    class Meta:
        verbose_name = u'账号类型'
        verbose_name_plural = u'账号类型'

class AcctStatus(models.Model):
    """账号状态定义"""
    acctst_lev = models.IntegerField(verbose_name=u'账号状态ID')
    acctst_dec = models.CharField(verbose_name=u'账号状态名称',max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.acctst_dec

    class Meta:
        verbose_name = u'账号状态'
        verbose_name_plural = u'账号状态'

class Region(models.Model):
    """地区定义"""
    region_id = models.IntegerField(verbose_name=u'账号所属地区ID',null=True, blank=True)
    region_dec = models.CharField(verbose_name=u'账号所属地区名称',max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.region_dec

    class Meta:
        verbose_name = u'地区'
        verbose_name_plural = u'地区'

class UserTitle(models.Model):
    """头衔定义"""
    title_id = models.IntegerField(verbose_name=u'账号头衔ID')
    title_dec = models.CharField(verbose_name=u'账号头衔名称',max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.title_dec

    class Meta:
        verbose_name = u'头衔'
        verbose_name_plural = u'头衔'
        

class ProfileBase(type):  
    def __new__(cls, name, bases, attrs):  #构造器，（名字，基类，类属性）
        module = attrs.pop('__module__')  
        parents = [b for b in bases if isinstance(b, ProfileBase)]  
        if parents:  
            fields = []  
            for obj_name, obj in attrs.items():  
                if isinstance(obj, models.Field): fields.append(obj_name)  
                User.add_to_class(obj_name, obj)       ####最重要的步骤
            UserAdmin.fieldsets = list(UserAdmin.fieldsets)  
            UserAdmin.fieldsets.append((name, {'fields': fields}))  
        return super(ProfileBase, cls).__new__(cls, name, bases, attrs)  

class ProfileUser(object):  
    __metaclass__ = ProfileBase  

class ExtraInfo(ProfileUser):
    scores = models.IntegerField(default=0, verbose_name=u'积分', null=True, blank=True)
    title = models.ForeignKey(UserTitle, verbose_name=u'头衔', default=1)
    nickname = models.CharField(max_length=50, verbose_name=u'昵称', null=True, blank=True)
    sex = models.CharField(max_length=10, verbose_name=u'性别', null=True, blank=True)
    birth = models.DateField(verbose_name=u'生日', null=True, blank=True)
    region = models.ForeignKey(Region, verbose_name=u'地区', default=1)
    acct_type = models.ForeignKey(AcctType, verbose_name=u'账号类型', default=1)
    status = models.ForeignKey(AcctStatus, verbose_name=u'账号状态', default=1)
    phone= models.CharField(max_length = 20, verbose_name=u'手机', null=True, blank=True) 
