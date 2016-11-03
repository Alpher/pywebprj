#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from profiles.forms import *

# Create your views here.

@login_required
def homeindex(request):
	'''首页'''
	has_login_bf=True
	return render(request,'index.html',{'username':request.user.username,'hostinfo':request.get_host(),'has_login_bf':has_login_bf})

@login_required
def saveUserInfo(request):
	'''账号管理页'''
	cur_user=User.objects.get(username=request.user.username)
	userid=cur_user.id
	username=cur_user.username
	userdj=cur_user.date_joined.strftime("%Y-%m-%d")
	useremail=cur_user.email
	if request.method == 'POST':
		form = ModifyUserForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			return HttpResponseRedirect('/myprofile/')
	else:
		form = ModifyUserForm(initial={'nickname':request.user.username,'sex':'1'})
	return render(request,'myprofile.html',locals())