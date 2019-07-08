"""
Discription:
    Circular Queue
    obj.capacity  get queue capacity
    obj.head      get queue index head
    obj.tail      get queue index tail
    enqueue()
    dequeue()
    print_all()
Author: calm.xia@gmail.com
"""

import sys

class CircularQueue(object):


    def __init__(self, capacity: int):
        self.__circularqueue = [None] * (capacity)
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
        print("enqueue... head %d tail %d"%(self.__head, self.__tail))
        # !Actually, the real item size is self.__capacity-1. Circular queue will waste a element space
        if (self.__tail + 1) % self.__capacity == self.__head : 
            print("enqueue error: circular queue is full ")
            return False
        else:
            self.__circularqueue[self.__tail] = item
            #self.__circularqueue[i] = None
            self.__tail = (self.__tail + 1) % self.__capacity
        return True


    def dequeue(self):
        '''
        Return:
            None    fail
            item     success
        '''
        print("dequeue... head %d tail %d"%(self.__head, self.__tail))
        if self.__head == self.__tail :
            print("Acircular queue is NULL!")
            return
        #item = self.__circularqueue.pop(self.__head)
        item = self.__circularqueue[self.__head]
        self.__circularqueue[self.__head] = None
        self.__head = (self.__head +1) % self.__capacity
        return item


    def print_all(self):
        print(sys._getframe().f_code.co_name,"...")

        for i in range(0, self.__capacity) : # print from index 0 to capacity
            item = self.__circularqueue[i]
            if item != None:
                print("index %d -- %d" %(i, item))
            else:
                print("index %d -- None" %(i))
        print("No more data in queue!")



if __name__ == "__main__":
    cq = CircularQueue(6)
    for i in range(0, cq.capacity):
        #print("xxxxxxx head = %d tail = %d i =%d"%(cq.head, cq.tail, i))
        cq.enqueue(i)
    cq.print_all()
    #cq.dequeue()
    #cq.print_all()
    #cq.enqueue(100)
    #cq.print_all()
    
