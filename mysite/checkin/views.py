#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseServerError
from profiles.views import getName
from django.http import Http404
from checkin.models import *
import datetime
from django.db import transaction
from django.http import JsonResponse
from mysite.settings import TYPE_OF_CHKIN,TYPE_OF_EXCHG,TYPE_OF_VIOLT,CHKIN_SCORE,CHKIN_SCORE_PLUS,CHKIN_SCORE_INITIAL_DATE

# Create your views here.

#用户积分累加接口函数,参数：uname-账号,optype-操作类型,参见models,opscore-入账积分
#事务控制 do all or nothing
@transaction.atomic
def add_uscore(uname,optype,opscore):
	#用户资料
	try:
		with transaction.atomic():
			user = User.objects.select_for_update().get(username=uname)
			thisscore = opscore
			#签到积分
			if optype == TYPE_OF_CHKIN:
				sov = UScoreOv.objects.select_for_update().get(username=uname)
				sov.refresh_from_db()

				if sov.last_chkin_dt.strftime('%Y-%m-%d') == datetime.datetime.now().strftime("%Y-%m-%d"):
					pass
				else:
					#上次连续签到天数
					last_days_in_a_row = sov.days_in_a_row
			
					#昨天
					lastdate=(datetime.datetime.now() - datetime.timedelta(days = 1)).strftime('%Y-%m-%d')
					#上次签到日期
					last_chkindt=sov.last_chkin_dt.strftime('%Y-%m-%d')
					#今天
					cur_dt = datetime.datetime.now().strftime("%Y-%m-%d")
			
					thisscore = CHKIN_SCORE
			
					#每年清零日期
					if datetime.datetime.now().strftime("%m-%d") == CHKIN_SCORE_INITIAL_DATE:
						#初始化
						sov.days_in_a_row = 1
						sov.days_in_month = 1
						sov.days_in_year = 1
						sov.accum_score = CHKIN_SCORE
						user.scores = CHKIN_SCORE
					#断签
					elif lastdate <> last_chkindt:
						sov.days_in_a_row = 1
						sov.days_in_year += 1
						sov.accum_score += CHKIN_SCORE
						user.scores += CHKIN_SCORE
						#月初
						if datetime.datetime.now().strftime("%d") == '01':
							sov.days_in_month = 1
						else:
							sov.days_in_month += 1
					#连签
					else:
						sov.days_in_a_row += 1
						sov.days_in_year += 1
						#月初
						if datetime.datetime.now().strftime("%d") == '01':
							sov.days_in_month = 1
						else:
							sov.days_in_month += 1
			
						#连接签到10天及以上奖励15积分
						if last_days_in_a_row >= 9:
							sov.accum_score += CHKIN_SCORE_PLUS
							user.scores += CHKIN_SCORE_PLUS
							thisscore = CHKIN_SCORE_PLUS
						else:
							sov.accum_score += CHKIN_SCORE
							user.scores += CHKIN_SCORE
							thisscore = CHKIN_SCORE
			
					sov.last_chkin_score = thisscore
					sov.last_chkin_dt=datetime.datetime.now().strftime('%Y-%m-%d')
					sov.save()
					user.save(update_fields=['scores'])
					#积分日志
					newslog = UScoreLog(username=uname,score=thisscore,usot=UScoreOpType.objects.get(type_code=optype),opby='system')
					newslog.save()
			#其他计分
			else:
				user.scores += opscore
				user.save(update_fields=['scores'])
		
				#积分日志
				newslog = UScoreLog(username=uname,score=thisscore,usot=UScoreOpType.objects.get(type_code=optype),opby='system')
				newslog.save()
	except Exception as e:
		print e




@login_required
def mycheckin(request):
	"""每日签到页面逻辑"""
	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)
	userscore = user.scores

	#当前凌晨
	today_first=datetime.datetime.now().strftime('%Y-%m-%d')+r' 00:00:00'
	#读取签到顺序前五位
	uslogs = UScoreLog.objects.filter(username=request.user.username,usot__type_code=TYPE_OF_CHKIN,update_ts__gt=datetime.datetime.strptime(today_first,"%Y-%m-%d %H:%M:%S"))

	if uslogs:
		handle_chk = 0
	else:
		handle_chk = 1

	#如果不存在统计视图，则创建
	if UScoreOv.objects.filter(username=request.user.username):
		pass
	else:
		init_sov = UScoreOv(username=request.user.username,last_chkin_dt=datetime.datetime.strptime('1999-01-01',"%Y-%m-%d"))
		init_sov.save()

	return render(request,'checkin.html',locals())

@login_required
def checkin(request):
	"""ajax签到"""
	if request.method == 'GET' and request.is_ajax():
		try:
			add_uscore(request.user.username,TYPE_OF_CHKIN,CHKIN_SCORE)
			sov = UScoreOv.objects.get(username=request.user.username)
			user=User.objects.get(username=request.user.username)
			data={'days_in_a_row_1':sov.days_in_a_row,'last_chkin_score_1':sov.last_chkin_score,'userjf':user.scores}
			return JsonResponse(data)
		except Exception as e:
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/mycheckin/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())

@login_required
def getchkinday(request):
	"""ajax获取签到日历史数据"""
	if request.method == 'GET' and request.is_ajax():
		try:
			days = []
			#月初
			month_first = datetime.datetime.now().strftime('%Y-%m')+r'-01 00:00:00'
			#读取签到日志
			uslogs = UScoreLog.objects.filter(username=request.user.username,usot__type_code=TYPE_OF_CHKIN,update_ts__gt=datetime.datetime.strptime(month_first,"%Y-%m-%d %H:%M:%S")).order_by('update_ts')
			for uslog in uslogs:
				days.append(str(int(uslog.update_ts.strftime('%d'))))
			return HttpResponse(','.join(days))
		except Exception as e:
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/mycheckin/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())

@login_required
def getchkinov(request):
	"""ajax获取签到统计数据"""
	if request.method == 'GET' and request.is_ajax():
		try:
			sov = UScoreOv.objects.get(username=request.user.username)
			data={'days_in_a_row_2':sov.days_in_a_row,'days_in_month_2':sov.days_in_month,\
				  'days_in_year_2':sov.days_in_year,'accum_score_2':sov.accum_score,\
				 }

			#上次签到日期
			last_chkindt=sov.last_chkin_dt.strftime('%Y-%m-%d')

			#如果今天是1号且未签到，则本月签到显示为0
			if last_chkindt < datetime.datetime.now().strftime('%Y-%m-%d') and datetime.datetime.now().strftime('%d') == '01':
				data['days_in_month_2'] = 0

			#当前凌晨
			today_first=datetime.datetime.now().strftime('%Y-%m-%d')+r' 00:00:00'
			#读取签到顺序前五位
			uslogs = UScoreLog.objects.filter(usot__type_code=TYPE_OF_CHKIN,update_ts__gt=datetime.datetime.strptime(today_first,"%Y-%m-%d %H:%M:%S")).order_by('update_ts')[:5]
			idx=1
			for uslog in uslogs:
				data['top'+str(idx)+'num'] = idx
				user=User.objects.filter(username=uslog.username)
				if user:
					if user[0].nickname:
						# data['top'+str(idx)] = user[0].nickname+'('+uslog.username+')'
						data['top'+str(idx)] = user[0].nickname
					else:
						data['top'+str(idx)] = uslog.username
				else:
					data['top'+str(idx)] = uslog.username
				data['top'+str(idx)+'ts'] = uslog.update_ts.strftime("%Y-%m-%d %H:%M:%S")
				idx+=1
			# print data
			return JsonResponse(data)
		except Exception as e:
			print e
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/mycheckin/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())