# Author: Matthew Armstrong
# Date: 11/10/2021
# Description: linked list class which is implemented with methods that use recursion

class Node:
    def __init__(self, data):
        """initializes node values"""
        self._data = data
        self._next = None

    def get_data(self):
        """returns node data"""
        return self._data

    def get_next(self):
        """returns next node"""
        return self._next

    def set_data(self, val):
        """sets data val in node"""
        self._data = val

    def set_next(self, val):
        """sets data val of next node"""
        self._next = val


class LinkedList:
    def __init__(self):
        """initializes the linked list"""
        self._head = None

    def get_head(self):
        """returns node object which is at the head of the linked list"""
        return self._head

    def set_head(self, node):
        """head setter method """
        self._head = node

    def rec_add(self, current, val):
        """helper function for the add method"""
        if current is None:
            return Node(val)
        else:
            current._next = self.rec_add(current._next, val)
            return current

    def add(self, val):
        """method which adds node containing val to the linked list"""
        if self._head is None:  # checks if the list is empty
            self._head = Node(val)
        else:
            self._head = self.rec_add(self._head, val)

    def remove(self, val):
        """method which removes a val from the linked list"""
        self._head = self.rec_remove(self._head, val)

    def rec_remove(self, current, val):
        """helper function for the remove method"""
        if current is None:  # checks if the list is empty
            return current
        if current.get_data() == val:  # checks if the node to remove is the head
            return current.get_next()
        else:
            current._next = self.rec_remove(current.get_next(), val)
            return current

    def contains(self, val):
        """method which returns true if the linked list contains a value, returns false otherwise"""
        if self._head is None:
            return False
        return self.rec_contains(val, self._head)

    def rec_contains(self, val, current):
        """helper function for contains method"""
        if current is None:
            return False
        if current.get_data() == val:
            return True
        else:
            return self.rec_contains(val, current.get_next())

    def insert(self, val, pos):
        """method which insert a node containing a val into the linked list at pos position"""
        if self._head is None:  # checks if the list is empty
            self.add(val)
            return

        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.set_next = temp
        else:
            self.rec_insert(val, pos - 1, self._head)

    def rec_insert(self, val, pos, current):
        """helper method for insert function"""
        if current is None:
            return Node(val)
        if pos == 0:
            temp = current.get_next()
            new_node = Node(val)
            current.set_next(new_node)
            new_node.set_next(temp)
        else:
            self.rec_insert(val, pos - 1, current.get_next())

    def reverse(self):
        """method which reverses the linked list"""
        if self._head is not None:
            self.rec_reverse(self._head, self._head.get_next())

    def rec_reverse(self, previous, current):
        """helper function for the reverse method"""
        if current is None:
            return current
        elif current.get_next() is None:
            self._head = current
            current.set_next(previous)
        else:
            temp = current.get_next()
            current.set_next(previous)
            self.rec_reverse(current, temp)

    def rec_to_plain_list(self, current, a_list):
        """helper method for to_plain_list function"""
        if current is not None:
            a_list.append(current.get_data())
            self.rec_to_plain_list(current.get_next(), a_list)
        return a_list

    def to_plain_list(self):
        """method which returns a regular Python list containing the same values,
        in the same order, as the linked list"""
        a_list = []
        if self._head is None:
            return a_list
        else:
            return self.rec_to_plain_list(self._head, a_list)
