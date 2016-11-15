#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django import forms
from django.forms.extras.widgets import SelectDateWidget
from profiles.models import Region
import re

#从数据库参数表中获取地区列表
def getProv():
	regSet = []
	for reg in Region.objects.all():
		regSet.append((reg.region_id,reg.region_dec))
	return tuple(regSet)


#账户资料修改表单
class ModifyUserForm(forms.Form):
	"""账户资料修改表单"""
	nickname = forms.CharField(max_length=100,label=u'昵称:')
	sex=forms.ChoiceField(label=u'性别:',   
                                   choices=((u'1', u'男'), (u'2', u'女'), ),   
                                   widget=forms.RadioSelect())
	birth=forms.DateField(label=u'生日:',widget=SelectDateWidget(years=tuple([i for i in xrange(1966,1997)])))
	#region=forms.ChoiceField(label=u'地区:',choices=((u'1',u'广东'),))
	region=forms.ChoiceField(label=u'地区:',choices=getProv())
	phone=forms.CharField(max_length=11,required=False,label='手机:')
	
	def clean_nickname(self):
		nickname = self.cleaned_data['nickname']
		num_words = len(nickname)
		if num_words < 4:
			raise forms.ValidationError("昵称必须超过4个字符!")
		return nickname

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		num_words = len(phone)

		ph = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')

		if (phone <> None and phone <> '') and num_words < 11:
			raise forms.ValidationError("手机号码必须为11位!")
		elif num_words == 11:
			if not ph.match(phone):
				raise forms.ValidationError(u'手机号码校验失败!')
		return phone

#密码修改表单
class ChangPwdForm(forms.Form):
	"""密码修改表单"""
	newpwd = forms.CharField(label= u'新的密码:',widget=forms.PasswordInput)
	confnewpwd = forms.CharField(label = u'确认密码:',widget=forms.PasswordInput)
	NEWPWD = ''

	def clean_newpwd(self):
		newpwd = self.cleaned_data['newpwd']
		self.NEWPWD = newpwd
		num_words = len(newpwd)
		if num_words < 8:
			raise forms.ValidationError(u'新的密码至少为8个字符!')
		return newpwd

	def clean_confnewpwd(self):
		confnewpwd = self.cleaned_data['confnewpwd']
		newpwd = self.NEWPWD
		num_words = len(confnewpwd)
		if num_words < 8:
			raise forms.ValidationError(u'确认密码至少为8个字符!')
		elif newpwd <> confnewpwd:
			raise forms.ValidationError(u'两次输入的密码不一致!')
		return confnewpwd
