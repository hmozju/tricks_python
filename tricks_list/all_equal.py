# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 17:59
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    检查列表中所有元素是否相等
"""

def all_equal(lst):
    return lst[1:] == lst[:-1]
