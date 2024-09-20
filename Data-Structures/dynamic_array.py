"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

class DynamicArray:
    def __init__(self) -> None:
        self._capacity = 100 # Standard capacity, including empty blocks, start with 10
        self._size = 0 # Current number of blocks occupied (not including empty blocks)
        self._data = [None] * self._capacity # Start with an empty allocation of 10 units
        self._start = (self._capacity // 2) - (self._size // 2) # Index where we start filling data
        self._append_space = self._capacity - self._size - self._start # Free space at end
        self._prepend_space = self._start  # Free space at start
        self._is_reversed = False

    def __str__(self) -> str:
        """
        A helper that allows you to print a DynamicArray type
        via the str() method.
        """
        result = "["
        if (self._is_reversed == False): # If not reversed add normally
            for i in range(self._size):
                result += str(self._data[self._start + i]) + ", "
        else:
            for i in range(self._size):
                result += str(self._data[self._start + self._size - i - 1]) + ", "
        
        result += "]"
        return result

    def __resize(self) -> None:
        """ 
        Resize is O(n) but amortized it is O(1)
        """
        self._capacity = self._capacity * 2 # Double capacity
        new_data = [None] * self._capacity # New dumb array
        new_start = (self._capacity // 2) - (self._size // 2) # We want our list to fill at middle
        for i in range(self._size):
            new_data[new_start + i] = self._data[self._start + i]
        self._data = new_data
        self._start = new_start
        self._append_space = self._capacity - self._size - self._start
        self._prepend_space = self._start

    def get_at(self, index: int) -> Any | None:
        """
        Get element at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (0 <= index < self._size):
            if (self._is_reversed == False): # If not reversed
                return self._data[self._start + index]
            else: # If reversed
                return self._data[self._start + self._size - index - 1]
        else: # Index out of bounds
            return None

    def __getitem__(self, index: int) -> Any | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index) # Indexing handled in get_at()

    def set_at(self, index: int, element: Any) -> None:
        """
        Get element at the given index.
        Do not modify the list if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (0 <= index < self._size):
            if (self._is_reversed == False): # If not reversed
                self._data[self._start + index] = element
            else: # If reversed
                self._data[self._start + self._size - index - 1] = element
        

    def __setitem__(self, index: int, element: Any) -> None:
        """
        Same as set_at.
        Allows to use square brackets to index elements.
        """
        self.set_at(index, element) # Indexing handled in get_at()

    def append(self, element: Any) -> None:
        """
        Add an element to the back of the array.
        Time complexity for full marks: O(1*) (* means amortized)
        """
        if (self._is_reversed == False):
            if (self._append_space == 0): # If no more slots at end available
                self.__resize() 
            self._data[self._start + self._size] = element # New index will be start + size
            self._append_space -= 1
        else: # If list is reversed, we actually prepend on our dumb array
            if (self._prepend_space == 0):
                self.__resize()
            self._data[self._start - 1] = element 
            self._start -= 1  # Adjust start
            self._prepend_space -= 1

        self._size += 1 # Size is incremented in all cases
        
    def prepend(self, element: Any) -> None:
        """
        Add an element to the front of the array.
        Time complexity for full marks: O(1*)
        """

        if (self._is_reversed == False):
            if (self._prepend_space == 0): # If no more slots at end available
                self.__resize() 
            self._data[self._start - 1] = element # New index will be start + size
            self._start -= 1 # Since we prepend, our start changes
            self._prepend_space -= 1
        else: # If list is reversed, we actually append on our dumb array
            if (self._append_space == 0): # If no more slots at end available
                self.__resize() 
            self._data[self._start + self._size] = element # New index will be start + size
            self._append_space -= 1

        self._size += 1 # Size is incremented in all cases

    def reverse(self) -> None:
        """
        Reverse the array.
        Time complexity for full marks: O(1)
        """
        self._is_reversed = not self._is_reversed

    def remove(self, element: Any) -> None:
        """
        Remove the first occurrence of the element from the array.
        If there is no such element, leave the array unchanged.
        Time complexity for full marks: O(N)
        """
        for i in range(self._size):
            if (self._is_reversed == False): # If list not reversed, the index is i
                index = i
            else:
                index = self._size - i - 1 # If list is reversed, the actual index
                
            if self._data[self._start + index] == element: # If values match, remove at this index
                self.remove_at(i) # Removal at i, reverse case is handled in remove_at()
                return

    def remove_at(self, index: int) -> Any | None:
        """
        Remove the element at the given index from the array and return the removed element.
        If there is no such element, leave the array unchanged and return None.
        Time complexity for full marks: O(N)
        """
        if (0 <= index < self._size):
            if (self._is_reversed == True): # If list is reversed we simply change the index
                index = self._size - 1 - index
            removed = self._data[self._start + index] # We will return this later
            for i in range(index, self._size - 1): # We must shift all elements after this back by 1
                self._data[self._start + i] = self._data[self._start + i + 1]
                
            self._data[self._start + self._size - 1] = None # Empty last block
            self._size -= 1 # Decrement size
            self._append_space += 1 # Increase append space, prepend space remains same
            return removed

        return None # If index out of bounds or if no such element is present in array


    def is_empty(self) -> bool:
        """
        Boolean helper to tell us if the structure is empty or not
        Time complexity for full marks: O(1)
        """
        if (self._size == 0):
            return True
        else:
            return False

    def is_full(self) -> bool:
        """
        Boolean helper to tell us if the structure is full or not
        Time complexity for full marks: O(1)
        """
        if (self._size == self._capacity):
            return True
        else:
            return False

    def get_size(self) -> int:
        """
        Return the number of elements in the list
        Time complexity for full marks: O(1)
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the total capacity (the number of slots) of the list
        Time complexity for full marks: O(1)
        """
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        Time complexity for full marks: O(NlogN)

        Note that sorting an array resets the reversed state of an array.
        """
        # Uses a merge sort algorithm, with helper functions given below
        if self._is_reversed: # If list is reversed, we can just unsort
            self.reverse() 

        self.__merge_sort(0, self._size - 1)

    def __merge(self, l: int, m: int, r: int):
        """
        Merge two halves of an array given the first half A[l...m]
        and second half A[m...r].

        This code is pulled from the pseudocode in week 2 lectures.
        """
        n1 = m - l + 1 # The size of the first half of array
        n2 = r - m # The size of the second half of array

        L = [None] * n1 # Dumb array that will store left half
        R = [None] * n2 # Dumb array that will store right half

        for i in range(n1): # Fill L, starting from l up to the middle
            L[i] = self._data[self._start + l + i] # We actually store at index self._start
            
        for j in range(n2): # Fill R, starting from the middle up to r
            R[j] = self._data[self._start + m + j + 1] # We actually store at index self._start

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                self._data[self._start + k] = L[i]
                i += 1
            else: 
                self._data[self._start + k] = R[j]
                j += 1
            k += 1

        while i < n1: # Copy the rest of L into final data
            self._data[self._start + k] = L[i]
            i += 1
            k += 1
        
        while j < n2: # Copy the rest of R into final data
            self._data[self._start + k] = R[j]
            j += 1
            k += 1

    def __merge_sort(self, l: int, r: int) -> None:
        """
        Using recursion, sort an array with a merge sort algorithm.

        This code is pulled from the pseudocode in week 2 lectures.
        O(N log N) worst-case.
        """
        if l < r:
            m = (l + r) // 2 # Middle index, we use floor in case odd number
            self.__merge_sort(l, m)
            self.__merge_sort(m + 1, r)
            self.__merge(l, m, r)
