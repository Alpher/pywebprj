#-*- coding:utf-8 -*-
__author__ = 'Alpher'

'''自定义过滤器'''

from django import template
from mysite.settings import STATIC_URL
from credit.models import *
from django.contrib.auth.models import User

register = template.Library()

@register.filter
def showpicurl(picurl):
	strurl=str(picurl)
	pathlist=strurl.split('/')
	if pathlist:
		picname = pathlist[-1]
		if picname == 'default.jpg':
			return r'/'+strurl
		else:
			return STATIC_URL+r'images/'+strurl

@register.filter
def checkexchg(strline,actionid):
	"""返回值 1-成功 2-奖品已抢光 3-积分不足 5-相同物品只能兑换一次"""
	usrname,rewardid = strline.split('-')
	status = '1'

	myrewards = MyRewards.objects.filter(username=usrname,action=Actions.objects.get(id=actionid),reward=Rewards.objects.get(id=rewardid))
	if myrewards:
		status = '5'
	else:
		cur_user = User.objects.get(username=usrname)
		if cur_user.scores < Rewards.objects.get(id=rewardid).reward_cost:
			status = '3'
		else:
			if Rewards.objects.get(id=rewardid).reward_left < 1:
				status = '2'
	return status


@register.filter
def strusrew(usrname,rewardid):
	return '%s-%s' %(usrname,rewardid)