# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 22:31
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    判断列表是否含有重复元素
"""
def has_duplicates(lst):
    """
    方法用于判断列表是否含有重复元素，是返回True，否返回False
    """
    return len(lst) != len(set(lst))