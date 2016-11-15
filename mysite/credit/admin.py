#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.contrib import admin

# Register your models here.

from credit.models import *

#定义管理界面各模型显示字段
class ActionTypeAdmin(admin.ModelAdmin):
	"""ActionTypeAdmin"""
	list_display = ('actiontype_code','actiontype_desc',)

class MyRewardsAdmin(admin.ModelAdmin):
	"""MyRewardsAdmin"""
	list_display = ('id','username','reward','reward_dt','isExchg','exchg_dt',)

class RewardsTypeAdmin(admin.ModelAdmin):
	"""RewardsTypeAdmin"""
	list_display = ('rewardstype_code','rewardstype_desc',)

class RewardsAdmin(admin.ModelAdmin):
	"""RewardsAdmin"""
	list_display = ('reward_code','reward_desc','reward_type','action_type','reward_cost','reward_enddt',)

class EcardTypeAdmin(admin.ModelAdmin):
	"""EcardTypeAdmin"""
	list_display = ('ecardtype_code','ecardtype_desc',)

class EcardsAdmin(admin.ModelAdmin):
	"""EcardsAdmin"""
	list_display = ('ecardnum','ecardpsw','ecardtype','isValid',)

class PhoneNumTypeAdmin(admin.ModelAdmin):
	"""PhoneNumTypeAdmin"""
	list_display = ('prefixnum','prefixnumtype',)
		

admin.site.register(EcardType,EcardTypeAdmin)
admin.site.register(Ecards,EcardsAdmin)
admin.site.register(ActionType,ActionTypeAdmin)
admin.site.register(RewardsType,RewardsTypeAdmin)
admin.site.register(Rewards,RewardsAdmin)
admin.site.register(MyRewards,MyRewardsAdmin)
admin.site.register(PhoneNumType,PhoneNumTypeAdmin)

