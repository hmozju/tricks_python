# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 21:05
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    
"""
def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i,list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret
def deep_flatten(lst):
    """
    方法用于将多维度的列表降为1维
    """
    result = []
    result.extend(
        spread(list(map(lambda x:deep_flatten(x) if type(x) == list else x,lst)))
    )
    return result