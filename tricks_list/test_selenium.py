# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/4 22:21
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    
"""
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get(url='https://www.baidu.com')
time.sleep(20)
browser.quit()