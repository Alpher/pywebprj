#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.contrib import admin

# Register your models here.
from profiles.models import *

#定义管理界面各模型显示字段
class AcctTypeAdmin(admin.ModelAdmin):
	"""AcctTypeAdmin"""
	list_display = ('acct_type_lev','acct_type_dec',)

class AcctStatusAdmin(admin.ModelAdmin):
	"""AcctStatusAdmin"""
	list_display = ('acctst_lev','acctst_dec',)

class RegionAdmin(admin.ModelAdmin):
	"""RegionAdmin"""
	list_display = ('region_id','region_dec',)

class UserTitleAdmin(admin.ModelAdmin):
	"""UserTitleAdmin"""
	list_display = ('title_id','title_dec',)


admin.site.register(AcctType,AcctTypeAdmin)
admin.site.register(AcctStatus,AcctStatusAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(UserTitle,UserTitleAdmin)