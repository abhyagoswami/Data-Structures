"""
Tests (informal) for data structures demonstrating their behaviour via the string representation.
Written by Abhya Goswami.
"""
from __future__ import annotations

# Imports
from dynamic_array import DynamicArray
from linked_list import Node
from linked_list import DoublyLinkedList
from bit_vector import BitVector
from typing import Any


def test_linked_list():
    """
    Basic tests for all methods of DoublyLinkedList. These can be extended or modified as the 
    user desires, and are left as strings instead of format tests to urge real-world usage.
    """
    print("\n \n================Executing DoublyLinkedList tests.================")
    test_list = DoublyLinkedList()
    # Insert to front will insert on the LHS of list
    test_list.insert_to_front("second")
    test_list.insert_to_front("first")
    test_list.insert_to_back(3) # Different types supported
    test_list.insert_to_front(0)

    print("\nCurrent list: " + str(test_list)) # List should be: 0, "first", "second", 3
    print("List head: " + str(test_list.get_head())) # Head should be 0
    print("List tail: " + str(test_list.get_tail())) # Tail should be 3
    print("Element \"first\" in list: " + str(test_list.find_element("first"))) # shound return True
    print("Element 4 in list: " + str(test_list.find_element(4))) # should return False

    test_list.set_head("new head")
    # List should be: "new head", "first", "second", 3
    print("\nNew list after setting head: " + str(test_list)) 
    test_list.set_tail("new tail")
    # List should be: "new head", "first", "second", "new tail"
    print("New list after setting tail: " + str(test_list)) 

    test_list.remove_from_front()
    # List should be: "first", "second", "new tail"
    print("\nNew list after removing from front: " + str(test_list)) 

    test_list.remove_from_back()
    # List should be: "first", "second"
    print("New list after removing from back: " + str(test_list)) 

    # Renew our list for upcoming test cases
    test_list.insert_to_front("zeroth")
    test_list.insert_to_back("third")
    # List should be: "zeroth", "first", "second", "third"
    print("\nUpdated list for next test cases: " + str(test_list)) 

    test_list.reverse()
    # List should be: "third", "second", "first", "zeroth"
    print("After reversal: " + str(test_list))
    test_list.find_and_remove_element("second")
    # List should be: "third", "first", "zeroth"
    print("After finding and removing \"second\": " + str(test_list))


def test_dynamic_array():
    """
    Basic tests for all methods of DynamicArray. These can be extended or modified as the 
    user desires, and are left as strings instead of format tests to urge real-world usage.
    """
    print("\n \n================Executing DynamicArray tests.================")

    test_arr = DynamicArray()
    print("\nFirst we test appending, prepending, sizing and capacity.")
    # Dynamic array has elements [51, 52, ... 99]
    for i in range(51, 100):
        test_arr.append(i)
    # Dynamic array has elements [1, 2, ... 99]
    for i in range(50, 0, -1):
        test_arr.prepend(i)

    print("Current list: " + str(test_arr))
    # Should be 100
    print("List capacity: " + str(test_arr.get_capacity()))
    # Should be 99
    print("List elements: " + str(test_arr.get_size()))


    print("\nNow we test resizing. At 100 elements," + 
          "we reach our limit so adding another will resize array.")

    # Dynamic array has elements [0, 1, 2, ... 100]
    test_arr.prepend(0) 
    print("List after resizing and adding element 0: " + str(test_arr))
    # Should be 200
    print("New capacity: " + str(test_arr.get_capacity()))
    # Should be 100
    print("New elements: " + str(test_arr.get_size()))

    print("\nNow we test getting and setting.")
    # Should return 50
    print("Get value at index 50: " + str(test_arr.get_at(50)))
    test_arr.set_at(50, "fifty")
    # Should return [0, 1, 2, ... 49, "fifty", 51, ..., 99]
    print("List after setting index 50 to \"fifty\": " + str(test_arr))

    print("\nNow we test reversal and sorting.")
    # We will change it back to [0, 1, 2, ... 99]
    test_arr.set_at(50, 50)
    print("Current list for future tests: " + str(test_arr))
    test_arr.reverse()
    # Should be [99, 98, ... 1, 0]
    print("List after reversal: " + str(test_arr))
    test_arr.sort()
    # Should be back to [0, 1, ..., 99]
    print("List after sorting: " + str(test_arr))

def test_bitvector():
    """
    Basic tests for all methods of DynamicArray. These can be extended or modified as the 
    user desires, and are left as strings instead of format tests to urge real-world usage.
    """
    print("\n \n================Executing BitVector tests.================")

    test_bv = BitVector()
    print("\nFirst we test appending, prepending, and size.")
    # Appending bits to BitVector
    for i in range(10):
        test_bv.append(i % 2)  # Appending alternating 0s and 1s

    print("Current BitVector after appending [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]: " + str(test_bv))
    # Should be 10
    print("BitVector size: " + str(test_bv.get_size()))


    print("\nNow we test getting and setting bits.")
    # Should return 0 for index 0
    print("Get bit at index 0: " + str(test_bv.get_at(0)))
    # Should return 1 for index 1
    print("Get bit at index 6: " + str(test_bv.get_at(6)))
    test_bv.set_at(6)  # Set bit at index 6 to 1
    print("BitVector after setting bit at index 6 to 1: " + str(test_bv))
    # Should return 1 at index 6
    print("Get bit at index 6 after setting: " + str(test_bv.get_at(6)))
    test_bv.unset_at(6)  # Set bit at index 5 back to 0
    print("BitVector after unsetting bit at index 6 to 0: " + str(test_bv))
    # Should return 0 at index 6
    print("Get bit at index 6 after unsetting: " + str(test_bv.get_at(6)))

    print("\nNow we test flipping and reversing bits.")
    # Flip all bits in BitVector
    test_bv.flip_all_bits()
    print("BitVector after flipping all bits: " + str(test_bv))
    # Reverse the BitVector
    test_bv.reverse()
    print("BitVector after reversing: " + str(test_bv))

test_linked_list()
test_dynamic_array()
test_bitvector()
