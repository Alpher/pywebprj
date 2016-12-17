#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.http import HttpResponseServerError
from profiles.views import getUserBase,getNameByUn
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from credit.models import *
from mysite import settings
import random
import datetime
from django.db import transaction
from django.contrib.auth.models import User
from checkin.views import add_uscore


# Create your views here.

#获取用户抽奖信息
def getuserltry(request):
	userltry = getUserBase(request)
	userltry['has_got_one'] = False
	userltry['mychance'] = 0
	cur_user=User.objects.get(username=request.user.username)
	cur_action = Actions.objects.filter(action_type__actiontype_code=settings.ACTIONTYPEOFREWARD,is_cur_action=True)
	if cur_action:
		myrwd=MyRewards.objects.filter(action=cur_action,username=request.user.username)
		#如果本次活动已中奖
		if myrwd:
			userltry['has_got_one'] = True
		else:
			today_first=datetime.datetime.now().strftime('%Y-%m-%d')+r' 00:00:00'
			ltylog = LotteryLog.objects.filter(username=cur_user,action=cur_action,opt_ts__gt=datetime.datetime.strptime(today_first,"%Y-%m-%d %H:%M:%S"))
			#如果今天已抽过奖
			if ltylog:
				userltry['mychance'] = 0
			else:
				userltry['mychance'] = settings.LOTTERY_CHANCE_DAILY
	else:
		userltry['mychance'] = 0
	return userltry

@login_required
def lottery(request):
	"""抽奖页面"""
	parmdic = getuserltry(request)
	rwdlist = []
	cur_action = Actions.objects.filter(action_type__actiontype_code=settings.ACTIONTYPEOFREWARD,is_cur_action=True)
	if cur_action:
		rewds = MyRewards.objects.filter(action=cur_action)
		for rwd in rewds:
			rwdlist.append(getNameByUn(rwd.username)+u' 获得了 '+rwd.reward.reward_desc+u'X1')
	parmdic['rewardlist'] = rwdlist
	return render(request,'lottery.html',parmdic)

@login_required
@transaction.atomic
def roll(request):
	if request.method == 'GET' and request.is_ajax():
		try:
			myltry = getuserltry(request)
			use_score = False
			data={}
			data['rollnum'] = settings.LOTTERY_INITIAL_IDX
			#服务器端校验
			if myltry['has_got_one']:
				data['status'] = 0
			elif myltry['mychance'] <= 0 and myltry['userscore'] < settings.LOTTERY_SCORE:
				data['status'] = -1
			elif myltry['mychance'] <= 0 and myltry['userscore'] >= settings.LOTTERY_SCORE:
				data['status'] = 1
				use_score = True
			else:
				data['status'] = 1
			if data['status'] == 1:
				cur_action = Actions.objects.filter(action_type__actiontype_code=settings.ACTIONTYPEOFREWARD,is_cur_action=True)
				act_conf = ActionConf.objects.filter(action=cur_action)
	
				max_random_num = act_conf[0].act_base
			
				cur_user_random = random.randint(1,max_random_num)
				all_idx_list=[0,1,2,3,4,5,6,7]
				rwd_index = -1
				for rwd in act_conf:
					all_idx_list.remove(rwd.rw_order)
					if cur_user_random >= rwd.rwd_s_idx and cur_user_random <= rwd.rwd_e_idx:
						rwd_index = rwd.rw_order
						myltry['has_got_one'] = True
						rwd_id = rwd.reward.id
				logremark=u''
				# print all_idx_list
				if rwd_index == -1:
					data['rollnum'] = random.choice(all_idx_list)
				else:
					data['rollnum'] = rwd_index
				if use_score:
					add_uscore(request.user.username,settings.TYPE_OF_EXCHG,(0-settings.LOTTERY_SCORE))
					logremark=u'积分抽奖'
				if myltry['has_got_one']:
					isSuccess = getreward(request.user.username,cur_action[0].id,rwd_id)
					if not isSuccess:
						data['rollnum'] = random.choice(all_idx_list)
				cur_user=User.objects.get(username=request.user.username)
				ltrylog=LotteryLog(username=cur_user,action=cur_action[0],random_num=cur_user_random,opt_remark=logremark)
				ltrylog.save()
				data['mychance']=getuserltry(request)['mychance']
				data['myscore']=cur_user.scores
				data['cur_username'] = getNameByUn(request.user.username)
			return JsonResponse(data)
		except Exception as e:
			print e
			return HttpResponseServerError()

	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/drawer/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())

def getreward(usrname,actionid,rewardid):
	has_got_one = False
	try:
		with transaction.atomic():
			myrwd=Rewards.objects.select_for_update().get(id=rewardid)
			myrwd.refresh_from_db()

			if myrwd.reward_left >= 1:
				myrwd.reward_left -= 1
				has_got_one = True
				myrwd.save()
				myrwdrec = MyRewards(username=usrname,action=Actions.objects.get(id=actionid),reward=Rewards.objects.get(id=rewardid),reward_dt=datetime.datetime.now().strftime('%Y-%m-%d'),isExchg=False)
				myrwdrec.save()
			else:
				has_got_one = False		
	except Exception as e:
		has_got_one = False
	finally:
		return has_got_one