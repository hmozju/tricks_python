# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 18:19
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    检查列表里的元素是否都是唯一的
"""

def all_unique(lst):
    return len(lst) == len(set(lst))