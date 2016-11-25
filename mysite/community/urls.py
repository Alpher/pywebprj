#-*- coding:utf-8 -*-

__author__='Alpher'

from django.conf.urls import url
from community.views import visitcom

urlpatterns = [
	url(r'^', visitcom),
]