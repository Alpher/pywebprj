#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseServerError
from profiles.views import getUserBase
import datetime
from django.db import transaction
from django.http import JsonResponse
from community.models import *

# Create your views here.

@login_required
def visitcom(request):
	parmdic = getUserBase(request)
	anns = Announcement.objects.filter(is_curanncm=True).order_by('-update_ts')
	if anns:
		parmdic['announce'] = anns[0]
	parmdic['cbbslist'] = Cbbs.objects.filter(category__ctgy_code=1).order_by('-priority')
	return render(request,"community.html",parmdic)