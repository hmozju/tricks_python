# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 22:16
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    剔除列表中出现多次的元素
"""
def filter_non_unique(lst):
    return [x for x in lst if lst.count(x) == 1]