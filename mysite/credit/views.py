#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from profiles.views import getName
from credit.models import MyRewards,Rewards,Ecards,PhoneNumType
from django.http import Http404
from credit.forms import GetRewardForm
from django.db import transaction
import datetime,time
from mysite.settings import ACTIONTYPEOFREWARD,TYPEOFACTUALREW
# Create your views here.


@login_required
def checkcredit(request):
	"""个人积分/兑换中心"""
	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)
	userscores = user.scores

	cur_dt = datetime.datetime.now().strftime("%Y-%m-%d")
	isOvdict = {}

	#中奖记录列表
	rewards=MyRewards.objects.filter(username=request.user.username,reward__action_type__actiontype_code=ACTIONTYPEOFREWARD)
	#rewards=MyRewards.objects.filter(username=request.user.username)

	#兑换记录列表
	exchanges = MyRewards.objects.filter(username=request.user.username).exclude(reward__action_type__actiontype_code=ACTIONTYPEOFREWARD)

	for rec in rewards:
		if rec.reward.reward_enddt.strftime("%Y-%m-%d") < cur_dt:
			isOvdict[rec.id] = 1
		else:
			isOvdict[rec.id] = 0

	return render(request,'mycredit.html',locals())

@login_required
def checkreward(request,reward_id):
	"""奖品/兑换查看页面"""
	try:
		offset = int(reward_id)
	except ValueError:
		raise Http404()

	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)
	showRew = False
	showXcg = False


	rewards=MyRewards.objects.filter(id=offset)
	if not rewards:
		reward=None
	else:
		reward = rewards[0]
		#根据实物/虚拟物品显不同信息
		if reward.reward.reward_type.rewardstype_code == TYPEOFACTUALREW:
			showRew = True
		else:
			showXcg = True
			ecards = Ecards.objects.filter(ecardnum=reward.ecardnum)
			if ecards:
				ecard = ecards[0]

	return render(request,'checkreward.html',locals())

@login_required
def getreward(request,reward_id):
	"""领取/兑换页面"""
	try:
		offset = int(reward_id)
	except ValueError:
		raise Http404()

	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)
	#是否实物页面
	showRew = False

	cur_dt = datetime.datetime.now().strftime("%Y-%m-%d") 

	rewards=MyRewards.objects.filter(id=offset)
	if not rewards:
		reward=None
	else:
		reward = rewards[0]
		#如果已经领奖，则跳转到查看奖品兑换详情页面，防止通过URL绕过程序修改数据
		if reward.isExchg == 1:
			return HttpResponseRedirect('/myrewards/'+str(offset)+'/')
		elif reward.reward.reward_enddt.strftime("%Y-%m-%d") < cur_dt:
			return HttpResponseRedirect('/mycredit/')
		else:
			#根据实物/虚拟物品显不同信息
			if reward.reward.reward_type.rewardstype_code == TYPEOFACTUALREW:
				showRew = True

	if request.method == 'POST':
		form = GetRewardForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			reward.isExchg = True
			reward.exchg_dt = cur_dt
			reward.exchg_name = cd['name']
			reward.exchg_phone = cd['phone']
			reward.exchg_addr = cd['addr']
			reward.addr_code = cd['addrcod']

			#虚拟物品,当前只支持话费卡自动获取卡密
			if not showRew:
				lockedcard = ''
				islocked = False
				error_return_link_lable = u'返回'
				error_tips = u'请联系管理员.'
				error_return_link = r'/mycredit/'
	
				#检索手机运营商
				phnumtype = PhoneNumType.objects.filter(prefixnum=cd['phone'][:3])
				if phnumtype:
					ecardtypeid = phnumtype[0].prefixnumtype.id
					#检索可用卡
					ecardlist = Ecards.objects.filter(ecardtype__id=ecardtypeid,isValid=True)
					if ecardlist:
						for ec in ecardlist:
							#会话行锁，防止并发问题
							try:
								with transaction.atomic():
									ecard = Ecards.objects.select_for_update().get(id=ec.id)
									#获得行锁后，从数据刷新数据，防止数据失效
									ecard.refresh_from_db()

									#如果卡品仍可用,则更新
									if ecard.isValid:
										ecard.isValid = False
										ecard.save(update_fields=['isValid'])
										
										#成功锁卡则跳出
										islocked = True
										lockedcard = ecard.ecardnum
										break
							except :
								#如果无法锁定该卡，则什么也不做
								pass
								#print '%s--pass' %ec.id
						if not islocked:
							error_info_strong = u'获取礼品卡失败!'
							return render(request,'innerror.html',locals())
					else:
						error_info_strong = u'无可用礼品卡!'
						return render(request,'innerror.html',locals())
				else:
					error_info_strong = u'无法识别运营商!'
					return render(request,'innerror.html',locals())
				reward.ecardnum=lockedcard
			reward.save()
			return HttpResponseRedirect('/myrewards/'+str(offset)+'/')
	elif showRew:
		form = GetRewardForm()
	else:
		form = GetRewardForm(initial={'name':'--','addr':'--','addrcod':'--',})

	return render(request,'getreward.html',locals())