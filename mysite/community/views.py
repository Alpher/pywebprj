#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseServerError,Http404
from profiles.views import getUserBase,getName,getNameByUn,getUserAvatarURL
import datetime,time,os
from mysite import settings
from django.db import transaction
from django.http import JsonResponse
from community.models import *
from PIL import Image
from community.forms import *

# Create your views here.

@login_required
def visitcom(request):
	parmdic = getUserBase(request)
	anns = Announcement.objects.filter(is_curanncm=True).order_by('-update_ts')
	if anns:
		parmdic['announce'] = anns[0]
	# 闲聊区主题列表
	parmdic['cbbslist'] = Cbbs.objects.filter(category__ctgy_code=settings.XL_MODULE_CODE).order_by('-priority','-update_ts')
	# 提问区主题列表
	parmdic['cbbslist2'] = Cbbs.objects.filter(category__ctgy_code=settings.TW_MODULE_CODE).order_by('-priority','-update_ts')
	# 反馈区主题列表
	parmdic['cbbslist3'] = Cbbs.objects.filter(category__ctgy_code=settings.FK_MODULE_CODE).order_by('-priority','-update_ts')
	return render(request,"community.html",parmdic)

@login_required
def visittopic(request,offset):
	try:
		topic_id = int(offset)
	except ValueError:
		raise Http404()

	parmdic = getUserBase(request)

	topic = Cbbs.objects.get(id=topic_id)
	topic_user = User.objects.get(username=topic.username)
	tp_comments = Comments.objects.filter(cbbs=topic).order_by('-create_ts')
	parmdic['topic_title'] = '['+topic.cbbsctgy.cbbsctgy_desc+']'+topic.title
	parmdic['topic_content'] = topic.content
	parmdic['topic_userid'] = topic_user.id
	parmdic['topic_useravatar'] = getUserAvatarURL(topic_user)
	parmdic['ctgy'] = topic.category.ctgy_desc
	parmdic['ctgyidx'] = int(topic.category.ctgy_code)-1
	parmdic['topic_create_ts'] = topic.create_ts
	parmdic['topic_id'] = topic.id
	parmdic['comments'] = tp_comments
	# parmdic['topic_viewers'] = topic.viewers
	parmdic['topic_comnts'] = topic.comnts
	if topic_user.nickname:
		parmdic['topic_showname'] = topic_user.nickname
	else:
		parmdic['topic_showname'] = topic_user.username

	saveuserlog(request.user.username,settings.VIEW_OPT_CODE,topic.id)
	topic.refresh_from_db()
	parmdic['topic_viewers'] = topic.viewers

	return render(request,"topic.html",parmdic)

def sceneImgUpload(request):
	if request.method == 'POST':
		callback = request.GET.get('CKEditorFuncNum')
		try:
			imgfname = request.user.username+'_'+time.strftime("%Y%m%d%H%M%S",time.localtime())+'_article_image.jpg'
			dest = os.path.join(settings.STATICFILES_DIRS[0],'images','article_images', imgfname)
			f = request.FILES["upload"]
			with open(dest, "wb") as destination:
				for chunk in f:
					destination.write(chunk)
				destination.close()
			#调整上传图片最大尺寸
			img = Image.open(dest)
			w,h = img.size
			if w > settings.IMGWIDTH:
				w = settings.IMGWIDTH
			if h > settings.IMGHEIGHT:
				h = settings.IMGHEIGHT
			img.resize((w,h),Image.ANTIALIAS).save(dest)
		except Exception as e:
			print e
		res = r"<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/static/images/article_images/"+imgfname+"','');</script>"
		return HttpResponse(res)
	else:
		raise Http404()


def savetopic(request):
	"""ajax发布新主题"""
	if request.method == 'POST' and request.is_ajax():
		try:
			vtitle = request.POST['title']
			vcontent = request.POST['content']
			vctgy = Category.objects.get(ctgy_code=request.POST['ctgy'])
			vcbbsctgy = CbbsCategory.objects.get(cbbsctgy_code=request.POST['topicctgy'])
			vusername = User.objects.get(username=request.user.username)

			tabidx = int(request.POST['ctgy'])-1

			topic = Cbbs(title=vtitle,username=vusername,category=vctgy,cbbsctgy=vcbbsctgy,content=vcontent)
			topic.save()

			return HttpResponse(tabidx)
		except Exception as e:
			print e
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/changeavatar/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())

def savetopiccomnt(request):
	"""ajax回复"""
	if request.method == 'POST' and request.is_ajax():
		try:
			vtopic = Cbbs.objects.get(id = request.POST['topic_id'])
			vcontent = request.POST['comment']
			vusername = User.objects.get(username=request.user.username)
			cmntid = -1
			
			if request.POST['cmntid']:
				vrefcmt = Comments.objects.get(id=request.POST['cmntid'])
				cmntid = request.POST['cmntid']
				comment = Comments(cbbs=vtopic,username=vusername,comment=vcontent,ref_comment=vrefcmt)
			else:
				comment = Comments(cbbs=vtopic,username=vusername,comment=vcontent)
			comment.save()

			saveuserlog(request.user.username,settings.CMNT_OPT_CODE,request.POST['topic_id'],cmntid)

			return HttpResponse("success")
		except Exception as e:
			print e
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/changeavatar/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())

@transaction.atomic
def saveuserlog(usrname,optcod,tpid=-1,cmntid=-1):
	user = User.objects.get(username=usrname)
	opttyp = CUserOptCtgy.objects.get(opt_code=optcod)

	if tpid == -1:
		topic = None
	else:
		topic = Cbbs.objects.get(id=tpid)

	if cmntid == -1:
		comment = None
	else:
		comment = Comments.objects.get(id=cmntid)

	if optcod == settings.VIEW_OPT_CODE:
		uloghist = CbbsUserLog.objects.filter(username=user,optctgy=opttyp,topic__id=tpid)
		if not uloghist:
			ulog = CbbsUserLog(username=user,optctgy=opttyp,topic=topic,comment=comment)
			ulog.save()
			updateviewers(tpid)
	elif optcod == settings.LIKE_OPT_CODE or optcod == settings.DLIK_OPT_CODE:
		uloghist = CbbsUserLog.objects.filter(username=user,optctgy=opttyp,topic__id=tpid,comment__id=cmntid)
		if not uloghist:
			ulog = CbbsUserLog(username=user,optctgy=opttyp,topic=topic,comment=comment)
			ulog.save()
			if optcod == settings.LIKE_OPT_CODE:
				updatelikes(tpid,cmntid)
			else:
				updatekicks(tpid,cmntid)
	else:
		ulog = CbbsUserLog(username=user,optctgy=opttyp,topic=topic,comment=comment)
		ulog.save()
		updatecomnts(tpid)

def updateviewers(tpid):
	"""更新浏览数"""
	try:
		with transaction.atomic():
			topic = Cbbs.objects.select_for_update().get(id=tpid)
			topic.viewers += 1
			topic.save(update_fields=['viewers'])
	except Exception as e:
		print e

def updatecomnts(tpid):
	"""更新回复数"""
	try:
		with transaction.atomic():
			topic = Cbbs.objects.select_for_update().get(id=tpid)
			topic.comnts += 1
			topic.save(update_fields=['comnts'])
	except Exception as e:
		print e

def updatelikes(tpid,cmntid):
	"""更新点赞数"""
	try:
		with transaction.atomic():
			cmnt = Comments.objects.select_for_update().get(cbbs__id=tpid,id=cmntid)
			cmnt.favors += 1
			cmnt.save(update_fields=['favors'])
	except Exception as e:
		print e

def updatekicks(tpid,cmntid):
	"""更新踩踏数"""
	try:
		with transaction.atomic():
			cmnt = Comments.objects.select_for_update().get(cbbs__id=tpid,id=cmntid)
			cmnt.kicks += 1
			cmnt.save(update_fields=['kicks'])
	except Exception as e:
		print e

def thmbup(request,offset1,offset2):
	if request.method == 'GET' and request.is_ajax():
		try:
			# tpid = int(offset1)
			# cmntid = int(offset2)
			saveuserlog(request.user.username,settings.LIKE_OPT_CODE,offset1,offset2)
			cmnt = Comments.objects.get(id=offset2)
			return HttpResponse(cmnt.favors)
		except Exception as e:
			print e
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/changeavatar/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())

def thmbdw(request,offset1,offset2):
	if request.method == 'GET' and request.is_ajax():
		try:
			# tpid = int(offset1)
			# cmntid = int(offset2)
			saveuserlog(request.user.username,settings.DLIK_OPT_CODE,offset1,offset2)
			cmnt = Comments.objects.get(id=offset2)
			return HttpResponse(cmnt.kicks)
		except Exception as e:
			print e
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/changeavatar/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())