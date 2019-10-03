# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 19:06
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    bifurcate将列表按照filter条件分成两个分列表
    bifurcate_by将列表按照fn条件（自定义）分成两个分列表
    
"""

def bifurcate(lst,filter):
    return[
        [x for i,x in enumerate(lst) if filter[i] == True],
        [x for i,x in enumerate(lst) if filter[i] == False]
    ]

"""
    文件说明
    将列表按照自定义条件fn分成两分
"""

def bifurcate_by(lst,fn):
    return[
        [x for i,x in enumerate(lst) if fn(x)],
        [x for i,x in enumerate(lst) if not fn(x)]
    ]
#bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')