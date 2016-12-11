# -*- coding: utf-8 -*-
__author__='Alpher'

"""
依赖自动化测试库selenium
Chrome浏览器及chromedriver
"""

from selenium import webdriver
import time,os

driver = webdriver.Chrome(r'C://Program Files (x86)//Google//Chrome//Application//chromedriver')

#设置浏览器窗口的位置和大小
driver.set_window_position(20, 40)
driver.set_window_size(1100,700)

#打开一个页面（QQ群空间登录页）
driver.get('http://qun.qzone.qq.com/group#!/92112862/member')
#登录表单在页面的框架中，所以要切换到该框架
driver.switch_to_frame('login_frame')
#通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys('****') #需要登录的QQ号
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys('****') #需要登录的QQ号对应的密码
driver.find_element_by_id('login_button').click()

time.sleep(10)
#定位群成员号码元素
memberlist = driver.find_elements_by_css_selector("span.member_id")
userlist=[]
i=0
for member in memberlist:
	i+=1
	print str(i)+'->'+member.text.replace('(','').replace(')','')
	userlist.append(member.text.replace('(','').replace(')','')+'\n')

#写入数据文件
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'members.txt'),'w') as f:
	f.writelines(userlist)

#3秒后退出浏览器，结束程序
time.sleep(3)
driver.quit()
