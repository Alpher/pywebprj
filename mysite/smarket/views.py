#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profiles.views import getUserBase,getName
from credit.models import *
from mysite.settings import ACTIONTYPEOFREWARD,STATIC_URL
from django.http import HttpResponseRedirect
from credit.views import grabreward
from django.http import Http404

# Create your views here.

@login_required
def smarket(request):
	"""积分商城页面"""
	parmdic = getUserBase(request)

	cur_exchg = Actions.objects.exclude(action_type__actiontype_code=ACTIONTYPEOFREWARD).filter(is_cur_action=True)

	parmdic['imgurl_prefix']=STATIC_URL+'images'

	if cur_exchg:
		parmdic['exchg_conf'] = ActionConf.objects.filter(action=cur_exchg)

	return render(request,'smarket.html',parmdic)

@login_required
def sexchange(request,offset1,offset2):
	try:
		action_id = int(offset1)
		reward_id = int(offset2)
	except ValueError:
		raise Http404()

	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)
	has_got_one = grabreward(request.user.username,action_id,reward_id)
	error_return_link_lable = u'返回'
	error_return_link = r'/smarket/'

	if has_got_one == 1:
		myreward = MyRewards.objects.filter(action__id=action_id,reward__id=reward_id).order_by('-update_ts')
	elif has_got_one == 2:
		error_info_strong = u'礼品已经被抢光!'
		return render(request,'innerror.html',locals())
	elif has_got_one == 3:
		error_info_strong = u'积分不足!'
		return render(request,'innerror.html',locals())
	elif has_got_one == 5:
		error_info_strong = u'相同物品只能兑换一次!'
		return render(request,'innerror.html',locals())
	else:
		error_info_strong = u'兑换失败!'
		return render(request,'innerror.html',locals())
	return HttpResponseRedirect('/getrewards/'+str(myreward[0].id)+'/')