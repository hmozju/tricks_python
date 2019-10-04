# author: hmin
# contact: hmin@zju.edu.cn
# datetime: 2019/10/3 19:03
# software: PyCharm 2017.1.2-Python 3.6.0(Anaconda)
# -*-coding:utf-8-*-
"""
    文件说明
    
"""

from tricks_list.all_equal import all_equal

a = [1,2,3,4,5,6]
b = [1,1,1,1,1,1]

print(all_equal(a))
print(all_equal(b))

from tricks_list.all_unique import all_unique

a = [1,2,3,4,5,6]
b = [1,2,3,3,4,5,6]
print(all_unique(a))
print(all_unique(b))


from tricks_list.bifurcate import bifurcate

a = ['beep','boop','foo','bar']
b = bifurcate(a,filter=[True,True,False,True])

print(b)

from tricks_list.bifurcate import bifurcate_by

a = ['beep','boop','foo','bar']
b = bifurcate_by(a, lambda x: x[0] == 'b')
print(b)

from tricks_list.compact import compact
a = [False,0,None, '',"",'1',2,'b','e']
print(compact(a))


# from package.module import function & use: function
# import package.module & use: package.module.function

import tricks_list.chunk
a = [1,2,3,4,5,6,7]
b = tricks_list.chunk.chunk(a,2)
print(b)

import tricks_list.counts
from math import floor
a = [6.4,5.1,6.12,7.01]
b = ['one', 'two', 'three']
key1 = tricks_list.counts.count_by(a,floor)
key2 = tricks_list.counts.count_by(b,len)
print(key1,key2)

import tricks_list.counts
a = [1,2,3,1,2,3,4,3,6]
key3 = tricks_list.counts.count_occurences(a,1)
key4 = tricks_list.counts.count_occurences(a,2)
key5 = tricks_list.counts.count_occurences(a,3)
print(key3,key4,key5)

import tricks_list.flatten
a = [[1,2],[3,4]]
b = tricks_list.flatten.flatten(a)
print(b)

c = [[[1,2],5],[6,7,[8,[9]]],[3,4]]
print(tricks_list.flatten.flatten(c))

import tricks_list.deep_flatten
print(tricks_list.deep_flatten.deep_flatten(c))
print(tricks_list.deep_flatten.spread(c))

import tricks_list.difference
a = [1,0,2]
b = [1,3,4]
c = tricks_list.difference.difference(a,b)
print(c)

from tricks_list.difference import difference_by
from math import floor
a = [1.2,2.3,3.4]
b = [2.3,3.4,3.8]
c = difference_by(a,b,floor)
print(c)
print(difference_by([{'x':2},{'x':1},{'x':3}],[{'x':1}],lambda v: v['x']))

from tricks_list.every import every, every_nth
a = [1,2,3,4]
b = [1,2,3,0]
print(every(a,lambda x:x > 0.5),every(b,bool))

c = [1,2,3,4,5,6,7,8,9]
print(every_nth(c,3))


from tricks_list.filter_non_unique import filter_non_unique
print(filter_non_unique([1,2,2,3,4,4,5,6,6,7,7]))

from tricks_list.group_by import group_by
from math import ceil
a = [4.3,4.1,5.7,5.1,5.2,6.8]
b = ['one','two','three']
print(group_by(a,ceil))
print(group_by(b,len))

from tricks_list.has_duplicates import has_duplicates
a = [1,2,3,3,4,5,6]
b = [1,2,3,4,5,6,7]
print(has_duplicates(a))
print(has_duplicates(b))

from tricks_list.head import head
print(head([1,2,3]))


from tricks_list.initial import initial
print(initial([1,2,3,4]))
print("hello world")
#test

from tricks_list.initialize_2d_list import  initialize_2d_list
print(initialize_2d_list(3,2,6))