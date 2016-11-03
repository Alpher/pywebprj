#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django import forms
from django.forms.extras.widgets import SelectDateWidget

PROV_CHOICES=((u'1',u'北京'),(u'2',u'天津'),(u'3',u'上海'),(u'4',u'重庆'),(u'5',u'河北'),(u'6',u'河南'),
(u'7',u'云南'),(u'8',u'辽宁'),(u'9',u'黑龙江'),(u'10',u'湖南'),(u'11',u'安徽'),(u'12',u'山东'),
(u'13',u'新疆'),(u'14',u'江苏'),(u'15',u'浙江'),(u'16',u'江西'),(u'17',u'湖北'),(u'18',u'广西'),
(u'19',u'甘肃'),(u'20',u'山西'),(u'21',u'内蒙'),(u'22',u'陕西'),(u'23',u'吉林'),(u'24',u'福建'),
(u'25',u'贵州'),(u'26',u'广东'),(u'27',u'青海'),(u'28',u'西藏'),(u'29',u'四川'),(u'30',u'宁夏'),
(u'31',u'海南'),(u'32',u'台湾'),(u'33',u'香港'),(u'34',u'澳门'),)

class ModifyUserForm(forms.Form):
	"""docstring for ModifyUserForm"""
	nickname = forms.CharField(max_length=100,label=u'昵称:')
	sex=forms.ChoiceField(label=u'性别:',   
                                   choices=((u'1', u'男'), (u'2', u'女'), ),   
                                   widget=forms.RadioSelect())
	birthdt=forms.DateField(label=u'生日:',widget=SelectDateWidget(years=tuple([i for i in xrange(1966,1997)])))
	region=forms.ChoiceField(label=u'地区:',choices=PROV_CHOICES)
	
	def clean_nickname(self):
		nickname = self.cleaned_data['nickname']
		num_words = len(nickname)
		if num_words < 4:
			raise forms.ValidationError("昵称必须超过4个字符!")
		return nickname