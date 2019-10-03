# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 22:22
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    将列表里的元素按照特定条件分类成字典的形式
"""
def group_by(lst,fn):

    return {key:[element for element in lst if fn(element) == key] for key in map(fn,lst)}