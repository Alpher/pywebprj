#-*- coding:utf-8 -*-
__author__ = 'Alpher'

'''自定义过滤器'''

from django import template
from profiles.views import getNameByUn,getUserAvatarURL
from django.contrib.auth.models import User
from community.models import Comments,CbbsUserLog
import datetime
from mysite import settings


register = template.Library()

@register.filter
def showname(usrname):
	"""显示用户账号或昵称"""
	return getNameByUn(usrname)

@register.filter
def showavatar(usrname):
	"""显示用户头像"""
	return getUserAvatarURL(User.objects.get(username=usrname))

@register.filter
def showuserid(usrname):
	"""显示用户ID"""
	return User.objects.get(username=usrname).id

@register.filter
def showreplies(cmntid):
	"""显示所有评论的评论"""
	comment = Comments.objects.get(id=cmntid)
	orcom = comment
	comlist={}
	i = 1
	htmlstr=""
	while comment.ref_comment:
	 	comment = Comments.objects.get(id=comment.ref_comment.id)
	 	comlist[i]=getNameByUn(comment.username)+':'+comment.comment
	 	i+=1
	for k,v in comlist.items():
		htmlstr=htmlstr+'<div style="border:1px solid #987cb9;padding:10px;background:GhostWhite;">'+v
	for i in range(len(comlist)):
		htmlstr=htmlstr+"</div>"
	# print htmlstr
	return htmlstr

@register.filter
def showlatestrplyer(tpid):
	"""显示最新回复人"""
	comment = Comments.objects.filter(cbbs__id=tpid).order_by('-create_ts')

	if comment:
		return comment[0].username
	else:
		return ''

@register.filter
def showlatestrplyts(tpid):
	"""显示最新回复时间"""
	comment = Comments.objects.filter(cbbs__id=tpid).order_by('-create_ts')

	if comment:
		return comment[0].create_ts.strftime("%Y-%m-%d %H:%M:%S")
	else:
		return ''

@register.filter
def showthumb(cmntid,usrid):
	"""显示赞踩"""
	cmnt = Comments.objects.get(id=cmntid)
	uplog = CbbsUserLog.objects.filter(username__id=usrid,comment=cmnt,optctgy__opt_code=settings.LIKE_OPT_CODE)
	dwlog = CbbsUserLog.objects.filter(username__id=usrid,comment=cmnt,optctgy__opt_code=settings.DLIK_OPT_CODE)

	if uplog:
		return settings.LIKE_OPT_CODE
	elif dwlog:
		return settings.DLIK_OPT_CODE
	else:
		return '-1'