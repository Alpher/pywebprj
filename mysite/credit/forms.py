#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django import forms
import re
from credit.models import PhoneNumType

class GetRewardForm(forms.Form):
	"""领取/兑换实物表单"""
	name = forms.CharField(max_length=50,label=u'领奖人姓名:')
	phone = forms.CharField(max_length=11,label=u'领奖人手机:')
	addr = forms.CharField(max_length=1000,label=u'领奖人地址:')
	addrcod = forms.CharField(max_length=6,label=u'领奖人邮编:')

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		num_words = len(phone)

		ph = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
		phnumtype = PhoneNumType.objects.filter(prefixnum=phone[:3])

		if num_words < 11:
			raise forms.ValidationError(u'手机号码必须为11位!')
		elif not ph.match(phone):
			raise forms.ValidationError(u'手机号码校验失败!')
		elif not phnumtype:
			raise forms.ValidationError(u'未识别的手机号段!')
		return phone

# class GetVRewardForm(forms.Form):
# 	"""领取/兑换虚拟物品表单"""
# 	phone = forms.CharField(max_length=11,label=u'领取/兑换人手机:')