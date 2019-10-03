# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 20:07
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    将列表按照特定的子规模分成若干份
"""
from math import ceil
def chunk(lst,size):
    return list(map(lambda x: lst[x*size : x*size+size], list(range(0,ceil(len(lst)/size)))))