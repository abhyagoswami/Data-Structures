"""
Skeleton for COMP3506/7505 A1, S2, 2024
The University of Queensland
Joel Mackenzie and Vladimir Morozov
"""

from typing import Any

from dynamic_array import DynamicArray


class BitVector:
    """
    A compact storage for bits that uses DynamicArray under the hood.
    Each element stores up to 64 bits, making BitVector 64 times more memory-efficient
    for storing bits than plain DynamicArray.
    """

    BITS_PER_ELEMENT = 4

    def __init__(self) -> None:
        """
        We will use the dynamic array as our data storage mechanism
        """
        self._data = DynamicArray() # Each element in data stores 64 bits
        self._size = 0 # Number of bits stored
        self._is_reversed = False
        self._flipped = False # Whether all bits are flipped or not

    def __str__(self) -> str:
        """
        A helper that allows you to print a BitVector type
        via the str() method.

        Each time we append it goes to the right-most bit.
        Index 0 is left-most bit.
        """
        result = "["
        bit_str = ""
        for i in range(self._size):
            integer_pos = i // self.BITS_PER_ELEMENT
            bit_position = i % self.BITS_PER_ELEMENT

            if self._flipped:
                bit_value = (self._data[integer_pos] >> bit_position) & 1 ^ 1
            else:
                bit_value = (self._data[integer_pos] >> bit_position) & 1

            if self._is_reversed:
                bit_str = str(bit_value) + bit_str
            else:
                bit_str += str(bit_value)

        result += bit_str
        result += "]"
        return result
        

    def __resize(self) -> None:
        # We simply add another 64 bits, which are currently all set to 0
        self._data.append(0)
        

    def get_at(self, index: int) -> int | None:
        """
        Get bit at the given index.
        Return None if index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (0 <= index < self._size):
            # The int position in dynamic array
            integer_position = index // self.BITS_PER_ELEMENT
            # The index position in integer
            bit_position = index % self.BITS_PER_ELEMENT

            # We will use AND to extract this bit
            if (self._is_reversed is False):
                bit = (self._data[integer_position] >> bit_position) & 1
            else:
                rev_bit_position = self.BITS_PER_ELEMENT - bit_position - 1
                bit = (self._data[integer_position] >> rev_bit_position) & 1
            
            if (self._flipped is True):
                bit = 1 - bit # Flip bit
            
            return bit
        
        else: # If out of bounds
            return None

    def __getitem__(self, index: int) -> int | None:
        """
        Same as get_at.
        Allows to use square brackets to index elements.
        """
        return self.get_at(index)

    def set_at(self, index: int) -> None:
        """
        Set bit at the given index to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (0 <= index < self._size):
            # The int position in dynamic array
            integer_position = index // self.BITS_PER_ELEMENT
            # The index position in integer
            bit_position = index % self.BITS_PER_ELEMENT

            if self._data[integer_position] is None:
                self._data[integer_position] = 0  # Initialize if None

            if (self._is_reversed is False):
                self._data[integer_position] |= (1 << bit_position) # OR
            else:
                rev_bit_position = self.BITS_PER_ELEMENT - 1 - bit_position
                self._data[integer_position] |= (1 << rev_bit_position) # OR
            

    def unset_at(self, index: int) -> None:
        """
        Set bit at the given index to 0.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        if (0 <= index < self._size):
            integer_position = index // self.BITS_PER_ELEMENT
            bit_position = index % self.BITS_PER_ELEMENT
            # To do this we use AND
            # We set all bits to 1 except the one we want as 0

            if self._data[integer_position] is None:
                self._data[integer_position] = 0  # Initialize if None
                
            if (self._is_reversed is False):
                # We set bit_position then we get complement, so it is actually 0
                and_with = ~(1 << bit_position) 
                self._data[integer_position] = self._data[integer_position] & (and_with)
            else:
                rev_bit_position = self.BITS_PER_ELEMENT - bit_position - 1
                and_with = ~(1 << rev_bit_position)
                self._data[integer_position] = self._data[integer_position] & (and_with)

        else: # If out of bounds
            return None

    def __setitem__(self, index: int, state: int) -> None:
        """
        Set bit at the given index.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Do not modify the vector if the index is out of bounds.
        Time complexity for full marks: O(1)
        """
        # Bounds of index handled in set_at and unset_at
        if (state == 0):
            self.unset_at(index)
        else:
            self.set_at(index)

    def append(self, state: int) -> None:
        """
        Add a bit to the back of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0; otherwise, set the bit to 1.
        Time complexity for full marks: O(1*)
        """
        # First determine what will be appended
        if (state == 0):
            bit = 0
        else:
            bit = 1

        # Account for flipping
        if (self._flipped is True):
            bit = 1 - bit

        # Resize if needed
        if self._size % self.BITS_PER_ELEMENT == 0: # Resize if needed
            self.__resize()

        if not self._is_reversed:  # Standard append
            integer_position = self._size // self.BITS_PER_ELEMENT
            bit_position = self._size % self.BITS_PER_ELEMENT
            self._data[integer_position] |= (bit << bit_position)
        
        else: # If list reversed, we actually prepend
            # Shift all bits to right by 1 index
            for i in range(self._size, 0, -1):
                curr_int_pos = i // self.BITS_PER_ELEMENT
                curr_bit_pos = i % self.BITS_PER_ELEMENT

                prev_int_pos = (i - 1) // self.BITS_PER_ELEMENT
                prev_bit_pos = (i - 1) % self.BITS_PER_ELEMENT

                # Extract the previous bit
                prev_bit_mask = 1 << prev_bit_pos # Mask to get prev_bit
                # We AND to extract bit from previous integer
                prev_bit = (self._data[prev_int_pos] & prev_bit_mask) >> prev_bit_pos

                # Set the next position to prev_bit value
                if (curr_bit_pos == 0 and curr_int_pos != prev_int_pos):
                    # If curr_bit_pos == 0 that means we take previous from last integer
                    # However, we must exclude cases where both are equal
                    self._data[curr_int_pos] = (self._data[curr_int_pos] << 1) | prev_bit
                else:
                    # Bit being moved within same integer
                    clear_mask = ~(1 << curr_bit_pos) # We invert because we want to clear
                    self._data[curr_int_pos] = self._data[curr_int_pos] & clear_mask
                    self._data[curr_int_pos] = self._data[curr_int_pos] | (prev_bit << curr_bit_pos)

            # Put new bit in 0th position
            clear_first_bit_mask = ~(1 << 0)
            self._data[0] = (self._data[0] & clear_first_bit_mask) | (bit << 0)

        self._size += 1  # Increment size in all cases


    def prepend(self, state: Any) -> None:
        """
        Add a bit to the front of the vector.
        Treat the integer in the same way Python does:
        if state is 0, set the bit to 0, otherwise set the bit to 1.
        Time complexity for full marks: O(1*)

        In str, each time we prepend it goes to the left-most bit.
        """
        # First determine what will be prepended
        if (state == 0):
            bit = 0
        else:
            bit = 1

        # Account for flipping
        if (self._flipped is True):
            bit = 1 - bit

        # Resize if needed
        if self._size % self.BITS_PER_ELEMENT == 0:  
            self.__resize()

        if not self._is_reversed:  # Standard prepend
            # Shift all values right by 1 index
            for i in range(self._size, 0, -1):
                curr_int_pos = i // self.BITS_PER_ELEMENT
                curr_bit_pos = i % self.BITS_PER_ELEMENT

                prev_int_pos = (i - 1) // self.BITS_PER_ELEMENT
                prev_bit_pos = (i - 1) % self.BITS_PER_ELEMENT

                # Extract the previous bit
                prev_bit_mask = 1 << prev_bit_pos # Use masking to get prev_bit
                # We AND to extract bit from previous integer
                prev_bit = (self._data[prev_int_pos] & prev_bit_mask) >> prev_bit_pos

                # Set the next position to prev_bit value
                if (curr_bit_pos == 0 and curr_int_pos != prev_int_pos):
                    # If curr_bit_pos == 0 that means we take previous from last integer
                    # However, we must exclude cases where both are equal
                    self._data[curr_int_pos] = (self._data[curr_int_pos] << 1) | prev_bit
                else:
                    # Bit being moved within same integer
                    clear_mask = ~(1 << curr_bit_pos) # We invert because we want to clear
                    self._data[curr_int_pos] = self._data[curr_int_pos] & clear_mask
                    self._data[curr_int_pos] = self._data[curr_int_pos] | (prev_bit << curr_bit_pos)

            # Put new bit in 0th position
            clear_first_bit_mask = ~(1 << 0)
            self._data[0] = (self._data[0] & clear_first_bit_mask) | (bit << 0)

        else:
            integer_position = self._size // self.BITS_PER_ELEMENT
            bit_position = self._size % self.BITS_PER_ELEMENT
            self._data[integer_position] |= (bit << bit_position)

        self._size += 1  # Increment size in all cases

    def reverse(self) -> None:
        """
        Reverse the bit-vector.
        Time complexity for full marks: O(1)
        """
        self._is_reversed = not self._is_reversed

    def flip_all_bits(self) -> None:
        """
        Flip all bits in the vector.
        Time complexity for full marks: O(1)
        """
        self._flipped = not self._flipped

    def get_size(self) -> int:
        """
        Return the number of *bits* in the list
        Time complexity for full marks: O(1)
        """
        return self._size
