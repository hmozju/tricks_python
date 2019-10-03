# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 20:52
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    将多层次（多维度）的列表降为1维
    
"""

def flatten(lst):
    """
    方法用于将二维列表降为1维
    """
    return [x for y in lst for x in y]


