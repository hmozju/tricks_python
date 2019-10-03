# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 21:21
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    筛选两个列表中特定条件的元素
"""

def difference(lsta,lstb):
    """
    方法用于筛选出属于lsta,但不属于lstb的元素
    """
    _lstb = set(lstb)
    return [item for item in lsta if item not in _lstb]

def difference_by(lsta,lstb,fn):
    """
    方法用于筛选出满足特定条件fn，属于lsta,但不属于lstb的元素
    """
    _lstb = set(map(fn,lstb))
    return [item for item in lsta if fn(item) not in _lstb]

