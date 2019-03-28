# !/usr/bin/env python3
# -*- coding:utf-8 -*-

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high: #确保二分查找正确停止
        mid = int((low + high) / 2) #如果(low + high)不是偶数，Python自动将mid向下圆整
        print('low %d mid %d high %d' %(low, mid, high))
        guess = list[mid] #取数组list的第mid项
        print('guess ', guess)
        if guess == item: #猜对了，下面的就不用判断了。注：相比较下面注释掉的逻辑顺序，这个最终要省些时间
            return guess
        elif guess < item: #猜的数字小了
            low = mid + 1
        else: #猜的数字大了
            high = mid - 1
        '''
        if guess > item: #猜的数字大了
            high = mid -1
        elif guess < item: #猜的数字小了
            low = mid + 1
        else: # guess == item
            return guess
        '''
    return None

print(binary_search([1,3,4,7,9], 3))