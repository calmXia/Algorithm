"""
Discription:
    array stack init;
    stack push;
    stack pop.

Author:
    calm.xia@gmail.com
"""

class ArrayStack(object):
    
    def __init__(self, size: int):
        self.__array_stack = []
        self.__size = size
        self.__top = 0


    def push(self, value: int):
        if self.__top >= self.__size -1 :
            return
        else:
            self.__array_stack.append(value)
            self.__top = self.__top + 1
        