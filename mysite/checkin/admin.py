#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.contrib import admin

# Register your models here.

from checkin.models import *

#定义管理界面各模型显示字段
class UScoreOpTypeAdmin(admin.ModelAdmin):
	"""UScoreOpTypeAdmin"""
	list_display = ('type_code','type_desc',)

class UScoreLogAdmin(admin.ModelAdmin):
	"""UScoreLogAdmin"""
	list_display = ('id','username','score','usot','opby','update_ts',)

class UScoreOvAdmin(admin.ModelAdmin):
	"""UScoreOvAdmin"""
	list_display = ('username','days_in_a_row','days_in_month','days_in_year','accum_score','last_chkin_dt','last_chkin_score',)


admin.site.register(UScoreOpType,UScoreOpTypeAdmin)
admin.site.register(UScoreLog,UScoreLogAdmin)
admin.site.register(UScoreOv,UScoreOvAdmin)
