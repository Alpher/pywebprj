#-*- coding:utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from mysite.views import aboutus
from django.contrib.auth.views import login, logout
from profiles.views import *
from credit.views import *
from checkin.views import *
from lottery.views import lottery,roll
from smarket.views import smarket,sexchange
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login,{'template_name':'login.html'}),
    url(r'^accounts/logout/$', logout,{'template_name':'logout.html'}),
    url(r'^$',homeindex),
    url(r'^about/$',aboutus),
    url(r'^smarket/$',smarket),
    url(r'^myprofile/$',saveUserInfo),
    url(r'^changepwd/$',changepwd),
    url(r'^pwdchanged/$',pwdchanged),
    url(r'^mycredit/$',checkcredit),
    url(r'^myrewards/(\d{1,2})/$',checkreward),
    url(r'^getrewards/(\d{1,2})/$',getreward),
    url(r'^changeavatar/$',changeavatar),
    url(r'^saveavatar/$',saveavatar),
    url(r'^mycheckin/$',mycheckin),
    url(r'^checkin/$',checkin),
    url(r'^getchkinday/$',getchkinday),
    url(r'^getchkinov/$',getchkinov),
    url(r'^community/',include('community.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^syncusers/$',syncusers),
    url(r'^drawer/$',lottery),
    url(r'^roll/',roll),
    url(r'^exchange/(\d{1,2})-(\d{1,2})/$',sexchange)
]
