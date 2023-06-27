#!/usr/bin/python3
"""Declare class Node and class SinglyLinkedList for a singly linked list."""

class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a Node instance with data and next_node.

        Args:
            data (int): The data of the new Node
            next_node (Node): The next node of the new Node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the Node."""
        return self.__data
    
    @property
    def next_node(self):
        """Retrieves the next node in the linked list."""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Sets the data value of the node.

        Args:
            value (int): The data value of the node
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list.

        Args:
            value (Node): The next node in the linked list
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initalize a singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        Args:
            value (int): The value of the new Node to be inserted
        """

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        if self.__head is None:
            return ""
            
        items = []
        tmp = self.__head
        while tmp is not None:
            items.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(items)
