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

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: int):
        self.__data = data  # Note: setter method need no return!

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, new_node):
        self.__next = new_node


class SinglyLinkedList(object):


    def __init__(self):
        """__head is the first node of linked list"""
        self.__head = None


    def find_by_value(self, value: int) -> Optional[Node]:
        node = self.__head
        while node != None and node.data != value:
            node = node.next
        return node


    def find_by_index(self, idx: int) -> Optional[Node]:
        node = self.__head
        pos = 0
        # "node != None" can cover cases "None list" and "last node of list"
        # pos != idx is the key!
        while node != None and pos != idx:
            node = node.next
            pos += 1
        return node


    def insert_value_to_head(self, value: int):
        if value != None:
            new_node = Node(value)
            self.insert_to_head(new_node)


    def insert_to_head(self, new_node: Node):
        """
        The new node will be inserted to replace the exist head node.
        Important: python variant is a reference(like pointer) to data, and not to storage data.
        Note: Inverse-sequence input: 这种操作将与输入的顺序相反，逆序
        """
        # Does it work when self.__head is None? Test it!
        if new_node != None:
            new_node.next = self.__head
            self.__head = new_node


    def insert_value_to_tail(self, value: int):
        """
        Sequence input
        """
        if value != None:
            new_node = Node(value)

        if self.__head == None:  # None linked list is a special case.
            self.__head = new_node
        else:
            self.insert_node_to_tail(new_node)


    def insert_node_to_tail(self, new_node: Node):

        if new_node == None:
            print("Error: insert None node")
            return
        if self.__head == None:
            print("Error: None list")
            return

        pos = self.__head
        while pos.next != None:
            pos = pos.next
        new_node.next = pos.next  # here pos node is tail
        pos.next = new_node
        # self.print_all()  # debug


    def insert_after(self, pos: Node, value: int):
        if value == None:
            return
        new_node = Node(value)
        if pos != None:  # must check
            new_node.next = pos.next
            pos.next = new_node


    def insert_before(self, pos: Node, value: int):
        """
        Need head
        """
        if value == None:
            return
        new_node = Node(value)
        if pos == None:
            return
        if pos == self.__head:
            '''
            new_node.next = self.__head
            self.__head = new_node
            '''
            self.insert_to_head(new_node)
            return
        else:
            q = self.__head
            while q != None and q.next != pos:
                q = q.next
            if q == None:  # Note: here pos is out of linked list, and q is tail-node.next
                return
            new_node.next = pos
            q.next = new_node


    def delete_by_node(self, d: Node):
        '''
        pos = self.__head
        if pos == None or d == None:
            return
        '''
        # the logic below is more clear than above
        if self.__head == None or d == None:
            return

        if d == self.__head:
            self.__head = self.__head.next
            return

        pos = self.__head
        while pos != None and pos.next != d:
            pos = pos.next
        if pos == None:  # d is out of list range
            return 
        pos.next = pos.next.next


    def delete_by_value(self, value: int):
        """
        Suppose the value is different with each other
        """
        if self.__head == None or value == None:
            return
        pos = self.__head
        q = None  # You should declare first
        while pos != None and pos.data != value:
            q = pos
            pos = pos.next
        
        if pos == None:  # value node is out of list range
            return
        
        if pos == self.__head:  # q == None. Find value in self.__head!
            self.__head = self.__head.next
        else:
            q.next = q.next.next


    def print_all(self):
        if self.__head == None:
            print("Error: NULL list")
            return
        pos = self.__head
        while pos != None:
            print(str(pos.data) + "->", end='')
            pos = pos.next
        print("None", end='\n')


    def inverse_linked_list(self):
        """
        inverse linked list that has no head
        1. How to inverse list?
        Keep list sequence, and just change the direction of node.next
        Ex:
                a --> b --> c --> ......--> m -->None
         None<--a <-- b <-- c <-- ......<-- m
        """
        pre = None
        pos = self.__head
        next = None
        while pos != None:
            next = pos.next
            pos.next = pre
            pre = pos
            pos = next
        self.__head = pre



'''
    def palindrome(self):
        """
        1. What is palindrome?
        A palindrome is a word or a phrase that is the same whether
        you read it backward or forward, for example, the word "refer", the list "1-2-3-2-1".

        3. How to judge a singly linked list is a palindrome list or not?
        Check weather the list is equal to the inverse list itself.
        """
'''

if __name__ == "__main__":
    list = SinglyLinkedList()
    for i in range(1,6):
        list.insert_value_to_tail(i)
    list.print_all()
    print("inverse...")
    list.inverse_linked_list()
    list.print_all()
