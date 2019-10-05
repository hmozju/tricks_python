# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/4 22:31
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    
"""
from splinter.browser import Browser
import time
browser = Browser(driver_name='chrome')
browser.visit(url='https://www.taobao.com')
time.sleep(20)
browser.quit()