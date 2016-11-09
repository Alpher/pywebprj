#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from profiles.forms import *
#from django.http import HttpResponse

# Create your views here.

@login_required
def homeindex(request):
	"""首页"""
	return render(request,'index.html',{'showname':getName(request),'hostinfo':request.get_host(),'isStaff':request.user.is_staff})

@login_required
def saveUserInfo(request):
	"""账号管理页"""
	SEX={u'男':'1',u'女':'2'}

	cur_user=User.objects.get(username=request.user.username)
	userid=cur_user.id
	username=cur_user.username
	userdj=cur_user.date_joined.strftime("%Y-%m-%d")
	useremail=cur_user.email
	userscores=cur_user.scores
	usertitle=cur_user.title
	showname=getName(request)
	isStaff=cur_user.is_staff
	accttype=cur_user.acct_type
	acctstatus=cur_user.status

	if cur_user.birth <> None and cur_user.birth <> '':
		birth = cur_user.birth.strftime("%Y-%m-%d")
	else:
		birth = '1967-01-01'

	if cur_user.sex <> None and cur_user.sex <> '':
		usersex = SEX[cur_user.sex]
	else:
		usersex = SEX[u'男']

	if cur_user.region <> None and cur_user.region <> '':
		region = cur_user.region_id
	else:
		region = '1'

	if request.GET.get('saveresult'):
		showSaveAlert = True
	else:
		showSaveAlert = False

	if request.method == 'POST':
		form = ModifyUserForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			#{'birthdt': datetime.date(1967, 1, 1), 'region': u'1', 'nickname': u'admin', 'phone': u'', 'sex': u'2'}
			user = User.objects.get(username = request.user.username)
			user.birth = cd['birth']
			user.region_id = cd['region']
			user.nickname = cd['nickname']
			user.sex = list(SEX.keys())[list(SEX.values()).index(cd['sex'])]
			user.phone = cd['phone']
			user.save()
			return HttpResponseRedirect('/myprofile/?saveresult=True')
	else:
		form = ModifyUserForm(initial={'nickname':showname,'sex':usersex,'birth':birth,'region':region,'phone':cur_user.phone,'showSaveAlert':showSaveAlert})
	return render(request,'myprofile.html',locals())

def getName(request):
	"""页面用户名/昵称显示"""
	cur_user=User.objects.get(username=request.user.username)
	nickname=cur_user.nickname
	#如果设置了昵称，则显示昵称，否则显示账号
	if nickname <> None and nickname <> '':
		username = nickname
	else:
		username = request.user.username
	return username

@login_required
def changepwd(request):
	user=User.objects.get(username=request.user.username)
	isStaff=user.is_staff
	showname=getName(request)

	if request.method == 'POST':
		form = ChangPwdForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			newpasswd = cd['confnewpwd']
			user.set_password(newpasswd)
			user.save()
			return HttpResponseRedirect('/pwdchanged/')
	else:
		form = ChangPwdForm()
	return render(request,'passwd.html',locals())


def pwdchanged(request):
	showname=u'匿名'
	return render(request,'pwdchanged.html',locals())