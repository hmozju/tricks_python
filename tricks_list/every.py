# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 22:04
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    利用切片提取指定位置nth及其倍数位置的元素构成新列表
""" 
def every(lst,fn=lambda x:x):
    """
    方法用于
    """
    return all(map(fn,lst))

def every_nth(lst,nth):
    """
    方法用于构造满足nth的新列表
    """
    return lst[nth-1::nth]