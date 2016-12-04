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
	parmdic['cbbslist'] = Cbbs.objects.filter(category__ctgy_code=1).order_by('-priority','-update_ts')
	parmdic['cbbslist2'] = Cbbs.objects.filter(category__ctgy_code=2).order_by('-priority','-update_ts')
	parmdic['cbbslist3'] = Cbbs.objects.filter(category__ctgy_code=3).order_by('-priority','-update_ts')
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
	if topic_user.nickname:
		parmdic['topic_showname'] = topic_user.nickname
	else:
		parmdic['topic_showname'] = topic_user.username

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
			
			if request.POST['cmntid']:
				vrefcmt = Comments.objects.get(id=request.POST['cmntid'])
				comment = Comments(cbbs=vtopic,username=vusername,comment=vcontent,ref_comment=vrefcmt)
			else:
				comment = Comments(cbbs=vtopic,username=vusername,comment=vcontent)
			comment.save()

			return HttpResponse("success")
		except Exception as e:
			print e
			return HttpResponseServerError()
	else:
		error_return_link_lable = u'返回'
		error_return_link = r'/changeavatar/'
		error_info_strong = u'无效访问!'
		return render(request,'innerror.html',locals())