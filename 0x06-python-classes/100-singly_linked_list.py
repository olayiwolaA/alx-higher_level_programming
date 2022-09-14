#!/usr/bin/python3
"Define class node"


class Node:
    "This is a singly-linked list node"
    def __init__(self, data, next_node=None):
        "Instantaite the node"
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        "get valte of node"
        return self.__data

    @data.setter
    def data(self, value):
        "to set it"
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        "get value of node"
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        "Set value of in node"
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    "defines a singly linked list"
    def __str__(self):
        "instantaiate the list"
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        "print the entire list in stdout"
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct
        sorted position in the list
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
