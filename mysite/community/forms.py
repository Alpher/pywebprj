#-*- coding:utf-8 -*-
__author__ = 'Alpher'

from django import forms
from ckeditor.fields import RichTextFormField

class TopicForm(forms.Form):
	"""新主题表单"""
	title = forms.CharField(max_length=50,label=u'主题:')
	# username = forms.CharField(max_length=50,label=u'账号:')
	# ctgy = forms.CharField(max_length=50,label=u'所属板块:')
	# topic_ctgy = forms.CharField(max_length=50,label=u'主题类型:')
	content = RichTextFormField(label=u'内容:')

	def clean_content(self):
		icontent = self.cleaned_data['content']
		nums = len(icontent)
		if nums < 2:
			raise forms.ValidationError("内容不能为空!")
		return icontent