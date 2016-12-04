#-*- coding:utf-8 -*-
__author__ = 'Alpher'

'''自定义过滤器'''

from django import template
from profiles.views import getNameByUn,getUserAvatarURL
from django.contrib.auth.models import User
from community.models import Comments


register = template.Library()

@register.filter
def showname(usrname):
	return getNameByUn(usrname)

@register.filter
def showavatar(usrname):
	return getUserAvatarURL(User.objects.get(username=usrname))

@register.filter
def showuserid(usrname):
	return User.objects.get(username=usrname).id

@register.filter
def showreplies(cmntid):
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