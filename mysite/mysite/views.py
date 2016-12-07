#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.http import HttpResponse
# from django.shortcuts import render_to_response
from profiles.views import getUserBase
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# import datetime

def aboutus(request):
	"""关于我们页面"""

	#参数列表
	parmdic={}

	#用户已登陆
	if request.user.is_authenticated():
		parmdic = getUserBase(request)
		parmdic['anymous'] = False
	else:
		parmdic['showname'] = u'游客'
		parmdic['anymous'] = True
		parmdic['hostinfo'] = request.get_host()
		parmdic['isStaff'] = request.user.is_staff
	return render(request,'about.html',parmdic)

#To be moved to market app
@login_required
def smarket(request):
	"""积分商城页面"""
	parmdic = getUserBase(request)
	return render(request,'scoremarket.html',parmdic)