"""
Discription:
    array stack init;
    stack push;
    stack pop.

Author:
    calm.xia@gmail.com

Date:
    201906
"""

class ArrayStack(object):
    
    def __init__(self, size: int):
        self.__array_stack = []
        self.__size = size
        self.__count = 0


    @property
    def size(self):
        return self.__size


    def push(self, value: int):
        if self.__count >= self.__size :
            print("stack is already full!")
            return
        else:
            self.__array_stack.append(value)
            self.__count += 1


    def pop(self):
        if self.__count > 0:
            self.__count -= 1
            return self.__array_stack.pop()
        else:
            print("stack null!")

    
    def print_all(self):
        '''
        range(start, stop[, step])
        '''
        print("stack elements' count = %d, they are:..." % self.__count)
        for i in range(self.__count, 0, -1):
            tmp = self.pop()
            print("stack pop: ", tmp)


if __name__ == "__main__":
    my_array_stack = ArrayStack(5)
    num = my_array_stack.size
    print("stack size: %d" % num)
    for i in range(2,10,2):
        my_array_stack.push(i)
    my_array_stack.print_all()
