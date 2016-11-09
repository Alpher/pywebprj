#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.contrib import admin

# Register your models here.

from credit.models import *

admin.site.register(RewardsType)
admin.site.register(Rewards)
admin.site.register(MyRewards)
