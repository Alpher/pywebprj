# -*- coding: utf-8 -*-
from selenium import webdriver
from pyvirtualdisplay import Display

if __name__ == '__main__':
    display = Display(visible=0,size=(800, 800))  
    display.start()  
    browser = webdriver.Firefox(executable_path='')  
    browser.get('http://www.baidu.com')  
    print browser.title