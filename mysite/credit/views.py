#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from profiles.views import getName
from credit.models import MyRewards
from django.http import Http404

# Create your views here.

@login_required
def checkcredit(request):
	"""个人积分/兑换中心"""
	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)
	userscores = user.scores

	rewards=MyRewards.objects.filter(username=request.user.username)

	return render(request,'mycredit.html',locals())

@login_required
def checkreward(request,reward_id):
	"""查看奖品兑换详情"""
	try:
		offset = int(reward_id)
	except ValueError:
		raise Http404()

	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)


	rewards=MyRewards.objects.filter(id=offset)
	if not rewards:
		reward=None
	else:
		reward = rewards[0]

	return render(request,'checkreward.html',locals())