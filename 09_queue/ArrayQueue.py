"""
Discription:
    Array Queue
    obj.capacity  get queue capacity
    obj.head      get queue index head
    obj.tail      get queue index tail
    enqueue()
    dequeue()
    print_all()

Author: calm.xia@gmail.com
"""

import sys

class ArrayQueue(object):


    def __init__(self, capacity: int):
        #self.__arrayqueue = [None] * capacity # Here can not work with self.__arrayqueue.append(item)
        # see: https://blog.csdn.net/xiaosaerjt/article/details/89013088
        self.__arrayqueue = []
        self.__capacity = capacity
        self.__head = 0
        self.__tail = 0


    @property
    def capacity(self):
        return self.__capacity


    @property
    def head(self):
        return self.__head


    @property
    def tail(self):
        return self.__tail


    def enqueue(self, item: int):
        """
        Return:
            False    fail
            True     sucess
        """
        if self.__tail == self.__capacity :
            return False
        #self.__arrayqueue[self.__tail] = item
        self.__arrayqueue.append(item)
        self.__tail += 1
        if self.__tail == self.__capacity :
            print("queue is full!")
        return True


    def dequeue(self):
        '''
        Return:
            None    fail
            item     success
        '''
        if self.__head == self.__tail :
            print("Aarray queue is NULL!")
            return
        #item = self.__arrayqueue.pop(self.__head)
        item = self.__arrayqueue[self.__head]
        self.__head += 1
        return item


    def print_all(self):
        item = None
        print(sys._getframe().f_code.co_name,"...")
        item = self.dequeue()
        if item == None:
            return
        
        print(item)
        while item != None:
            item = self.dequeue()
            if item == None:
                break
            print(item)
        print("No more data in queue!")


if __name__ == "__main__":
    aq = ArrayQueue(5)
    for i in range(2, 15, 2):
        #print("xxxxxxx head = %d tail = %d i =%d"%(aq.head, aq.tail, i))
        aq.enqueue(i)
    aq.print_all()
