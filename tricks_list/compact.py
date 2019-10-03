# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 19:48
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    移除列表中“false”,'0','None'等值
"""

def compact(lst):
    return list(filter(bool,lst))