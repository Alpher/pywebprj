#-*- coding:utf-8 -*-

__author__='Alpher'

from django.conf.urls import url
from community.views import *

urlpatterns = [
	url(r'^$', visitcom),
	url(r'^topic/(\d{1,10})/$',visittopic),
	url(r'^uploadimg/$',sceneImgUpload),
	url(r'^posttopic/$',savetopic),
	url(r'^posttpcmt/$',savetopiccomnt),
]