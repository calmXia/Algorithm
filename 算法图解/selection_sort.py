# !/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "calm.xia@gmail.com"

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    
def selectionSort(arr):
    newArr = []
    for i in range(0,len(arr)):
        smallest_index = findSmallest(arr)
        newArr.append(arr.pop(smallest_index)) # arr.length -1, new arr come out after arr.pop!
    return newArr
    
print(selectionSort([5,6,8,6,9]))
