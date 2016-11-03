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

from django.conf.urls import url
from django.contrib import admin
from mysite.views import userLogin
from django.contrib.auth.views import login, logout
from profiles.views import *
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', login,{'template_name':'login.html'}),
    url(r'^accounts/logout/$', logout,{'template_name':'logout.html'}),
    url(r'^$',homeindex),
    url(r'^myprofile/$',saveUserInfo),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
