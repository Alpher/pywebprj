from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def userLogin(request):
	now = datetime.datetime.now()
	return render_to_response('homepage.html',locals())
