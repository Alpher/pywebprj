#-*- coding:utf-8 -*-
from __future__ import unicode_literals

__author__ = 'Alpher'

from django.contrib import admin
from community.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	"""docstring for ClassName"""
	list_display = ('ctgy_code','ctgy_desc',)

class CbbsCategoryAdmin(admin.ModelAdmin):
	"""docstring for CbbsCategoryAdmin"""
	list_display = ('cbbsctgy_code','cbbsctgy_desc',)

class CbbsAdmin(admin.ModelAdmin):
	"""docstring for CbbsAdmin"""
	list_display = ('title','username','category','cbbsctgy','update_ts',)		


class CommentsAdmin(admin.ModelAdmin):
	"""docstring for CommentsAdmin"""
	list_display = ('cbbs','username','create_ts','favors','kicks','is_reward',)

class CbbsTipsAdmin(admin.ModelAdmin):
	"""docstring for CbbsTipsAdmin"""
	list_display = ('cbbs','from_user','to_user','score','op_ts',)	

class AnnouncementAdmin(admin.ModelAdmin):
	"""docstring for AnnouncementAdmin"""
	list_display = ('title','username','is_curanncm','update_ts',)	

admin.site.register(Category,CategoryAdmin)
admin.site.register(CbbsCategory,CbbsCategoryAdmin)
admin.site.register(Cbbs,CbbsAdmin)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(CbbsTips,CbbsTipsAdmin)
admin.site.register(Announcement,AnnouncementAdmin)