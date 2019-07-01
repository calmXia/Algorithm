# !/usr/bin/env python3
# -*- coding:utf-8 -*-
#! python3

__author__ = 'calm.xia@gmail.com'

# 4.1 D&C
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list.pop(0) + sum(list)


# 4.2 D&C
def count(list):
    #print(list)
    if not list:
        return 0 
    else:
        list.pop()
        return 1 + count(list)


#4.3 D&C
def max(list):
    print(list)
    # base case
    if len(list) == 2:
        print('----')
        return list[0] if list[0] > list[1] else list[1]
    # recursive case
    print('++++')
    sub_max = max(list[1:]) #切片
    print('****', list)
    return list[0] if list[0] > sub_max else sub_max
        
        
    
    
    
#print(sum([2,4,6]))
#print('Total items number: %d' % count([1,2,3]))
print('The max number is %d' % max([13,2,4,8]))

'''
C:\Users\calm.xia\Desktop>py -3 quick_sort.py
[13, 2, 4, 8]
++++
[2, 4, 8]
++++
[4, 8]
----
**** [2, 4, 8]
**** [13, 2, 4, 8]
The max number is 13
'''
