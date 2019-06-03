""" singly linked list

1. Find, insert, delete to singly linked list;
2.

Important:
    The trail node`s __next is None.
    Python variant is a reference(like pointer) to data, and not to storage data.

Author: calm.xia@gmail.com
"""
from typing import Optional

class Node(object):


    def __init__(self, data:int, next=None):
        """construction method of class Node

        Parameters:
            __data: data of Node
            __next: reference to next Node
        """
        self.__data = data
        self.__next = next


class SinglyLinkedList(object):


    def __init__(self):
        """__head is the first node of linked list"""
        self.__head = None

    def find_by_value(self, value: int) -> Optional[Node]:
        node = self.__head
        while node != None and node.__data != value:
            node = node.__next
        return node

    def find_by_index(self, idx: int) -> Optional[Node]:
        node = self.__head
        pos = 0
        # "node != None" can cover cases "None list" and "last node of list"
        # pos != idx is the key!
        while node != None and pos != idx:
            node = node.__next
            pos += 1
        return node

    def insert_value_to_head(self, value: int):
        if value != None:
            new_node = Node(value)
            self.insert_to_head(new_node)
        
        """
        The new node will be inserted to replace the exist head node.
        Important: python variant is a reference(like pointer) to data, and not to storage data.
        Note: 这种操作将与输入的顺序相反，逆序
        """
    def insert_to_head(self, new_node=None):
        '''
        if self.__head == None:
            self.__head = new_node
        else:
            new_node.__next = self.__head
            self.__head = new_node
        '''
        # Does it work when self.__head is None? Test it!
        if new_node != None:
            new_node.__next = self.__head
            self.__head = new_node
