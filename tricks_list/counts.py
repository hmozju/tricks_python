# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 20:22
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    count_by:根据给定的函数将列表分组，并统计符合条件的元素数目
    count_occurences:统计列表中元素出现的次数
    
""" 

def count_by(arr,fn=lambda x:x):
    """
    方法用于根据给定的函数将列表分组，并统计符合条件的元素数目
    """
    key = {}
    for element in map(fn,arr):
        key[element] = 1 if element not in key else key[element] + 1
    return key


def count_occurences(lst,val):
    """
    方法用于统计列表中元素出现的次数
    """
    return len([x for x in lst if x == val and type(x) ==  type(val)])