"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

# so we can hint Node get_next
from __future__ import annotations

from typing import Any

class Node:
    """
    A simple type to hold data and a next pointer
    """
    def __init__(self, data: Any) -> None:
        self._data = data # This is the payload data of the node
        self._next = None # This is the "next" pointer to the next Node
        self._prev = None # This is the "previous" pointer to the previous Node

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: Node) -> None:
        self._next = node

    def get_next(self) -> Node | None:
        return self._next

    def set_prev(self, node: Node) -> None:
        self._prev = node

    def get_prev(self) -> Node | None:
        return self._prev


class DoublyLinkedList:
    """
    A doubly linked list that supports the storage of a Node type.
    """
    def __init__(self) -> None:
        # You probably need to track some data here...
        self._head = None # Head of list, first node
        self._tail = None # Tail of list, last node
        self._size = 0 # Total number of nodes
        self._is_reversed = False # Use as a flag

    def __str__(self) -> str:
        """
        A helper that allows you to print a DoublyLinkedList type
        via the str() method.
        """
        result = ""
        if (self._head is None):
            return result
        
        if (self._is_reversed is False): # Is not reverse
            current_node = self._head
            while (current_node != None):
                result += str(current_node.get_data()) + " "
                current_node = current_node.get_next()
        else: # Is reversed
            current_node = self._tail
            while (current_node != None):
                result += str(current_node.get_data()) + " "
                current_node = current_node.get_prev()

        return result

    """
    Simple Getters and Setters below
    """

    def get_size(self) -> int:
        """
        Return the size of the list.
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_head(self) -> Any | None:
        """
        Return the data of the leftmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if (self._head == None):
            return None
        else:
            if (self._is_reversed is False):
                return self._head.get_data()
            else: # If list is reversed
                return self._tail.get_data()

    def set_head(self, data: Any) -> None:
        """
        Replace the leftmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if (self._is_reversed is False):
            if (self._size != 0):
                self._head.set_data(data)
        else:
            if (self._size != 0):
                self._tail.set_data(data)

    def get_tail(self) -> Any | None:
        """
        Return the data of the rightmost node in the list, if it exists.
        Time complexity for full marks: O(1)
        """
        if (self._tail == None):
            return None
        else:
            if (self._is_reversed is False):
                return self._tail.get_data()
            else: # If list is reversed
                return self._head.get_data()

    def set_tail(self, data: Any) -> None:
        """
        Replace the rightmost node's data with the given data.
        If the list is empty, do nothing.
        Time complexity for full marks: O(1)
        """
        if (self._is_reversed is False):
            if (self._size != 0):
                self._tail.set_data(data)
        else:
            if (self._size != 0):
                self._head.set_data(data)

    """
    More interesting functionality now.
    """

    def insert_to_front(self, data: Any) -> None:
        """
        Insert the given data to the front of the list.
        Hint: You will need to create a Node type containing
        the given data.
        Time complexity for full marks: O(1)
        """
        node = Node(data) # Create new node
        if (self._head != None):
            if (self._is_reversed is False):
                node.set_next(self._head) # Move current head to right
                self._head.set_prev(node) # New node comes before head, tail remains same
                self._head = node # New node becomes new head
            else: # If list is reversed
                node.set_prev(self._tail)
                self._tail.set_next(node)
                self._tail = node
        
        else:
            # If empty, new node will be both head and tail
            self._head = node
            self._tail = node
        
        self._size += 1 # Increment in all cases
        
    def insert_to_back(self, data: Any) -> None:
        """
        Insert the given data (in a node) to the back of the list
        Time complexity for full marks: O(1)
        """
        node = Node(data) # Create new node
        if (self._tail != None):
            if (self._is_reversed is False): # If not reversed
                node.set_prev(self._tail) # Move current head to left
                self._tail.set_next(node) # New node comes after tail, head remains same
                self._tail = node # New node becomes new tail
            else: # If is reversed
                node.set_next(self._head)
                self._head.set_prev(node)
                self._head = node # New node becomes new head

        else:
            # If empty, new node will be both head and tail
            self._head = node
            self._tail = node
        
        self._size += 1 # Size incremented in all cases

    def remove_from_front(self) -> Any | None:
        """
        Remove the front node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        if (self._head == None): # If 0 elements
            return None
        
        elif (self._head == self._tail): # If 1 element
            old_head = self._head.get_data() # We will return this
            self._head = None
            self._tail = None
            self._size -= 1
            return old_head
        
        else: # If > 1 element
            if (self._is_reversed is False): # If not reversed
                old_head = self._head.get_data() # Return this later
                new_head = self._head.get_next()
                new_head.set_prev(None)
                self._head = new_head
                self._size -= 1
                return old_head
            else: # If list is reversed
                old_head = self._tail.get_data()
                new_head = self._tail.get_prev()
                new_head.set_next(None)
                self._tail = new_head
                self._size -= 1
                return old_head

    def remove_from_back(self) -> Any | None:
        """
        Remove the back node, and return the data it holds.
        Time complexity for full marks: O(1)
        """
        if (self._tail == None): # If 0 elements
            return None
        
        elif (self._head == self._tail): # If 1 element
            old_tail = self._tail.get_data() # We will return this
            self._head = None
            self._tail = None
            self._size -= 1
            return old_tail
        
        else: # If > 1 element
            if (self._is_reversed is False): # If not reversed
                old_tail = self._tail.get_data() # Return this later
                new_tail = self._tail.get_prev()
                new_tail.set_next(None)
                self._tail = new_tail
                self._size -= 1
                return old_tail
            else: # If list is reversed
                old_tail = self._head.get_data()
                new_tail = self._head.get_next()
                new_tail.set_prev(None)
                self._head = new_tail
                self._size -= 1
                return old_tail

    def find_element(self, elem: Any) -> bool:
        """
        Looks at the data inside each node of the list and returns True
        if a match is found; False otherwise.
        Time complexity for full marks: O(N)
        """
        check_node = self._head # Start by checking head
        found = False
        while (check_node != None): # Stop while loop when we reach end of list
            if (check_node.get_data() == elem):
                found = True
                break
            else:
                check_node = check_node.get_next() # Check next node
        
        return found # Return result

    def find_and_remove_element(self, elem: Any) -> bool:
        check_node = self._head # Start by checking head
        found = False

        # Stop while loop when we reach end of list or if check_node = elem
        while (check_node != None): 
            if (check_node.get_data() == elem):
                if (self._is_reversed is False): # If not reversed
                    if (check_node == self._head): # Check if desired element is our head
                        self.remove_from_front() # Remove first element, decrementing handled
                    elif (check_node == self._tail): # Otherwise, check if desired element is tail
                        self.remove_from_back() # Remove last element, decrementing handled
                    else: # Neither head nor tail
                        next_node = check_node.get_next()
                        last_node = check_node.get_prev()
                        next_node.set_prev(last_node)
                        last_node.set_next(next_node)
                        self._size -= 1 # Decrement manually

                else: # If list is reversed
                    if (check_node == self._head): # Tail in reverse is actual head 
                        self.remove_from_back()
                    elif (check_node == self._tail): # Head in reverse is actual tail
                        self.remove_from_front()
                    else: # Neither head nor tail
                        next_node = check_node.get_next()
                        last_node = check_node.get_prev()
                        next_node.set_prev(last_node)
                        last_node.set_next(next_node)
                        self._size -= 1
                found = True
                break
        
            else: # If this node is not the desired element, check next node
                check_node = check_node.get_next()
    
        return found # Return boolean flag
    
    def reverse(self) -> None:
        """
        Reverses the linked list
        Time complexity for full marks: O(1)
        """
        self._is_reversed = not self._is_reversed