# Data-Structures
 A Python implementation of data structures including a dynamic array, doubly linked list and bitvector.
 
# Description
- All three data structures are implemented manually without the use of in-built Python methods or data structures (Python lists are used only as "storage containers", but their list functionality is not used).
- The data structures are built in such a way to optimize their time complexity, aiming for efficiency. Each function docstring will describe this.
- The code skeleton is credited to The University of Queensland - Joel Mackenzie and Vladimir Morozov.
- All implementations are credited to author - Abhya Goswami.
  
# Features
- A Doubly Linked List class which supports appending and prepending to any side of the list in O(1) complexity. The list can also be reversed in O(1), whereas, finding and removing an element from any index takes O(N) complexity.
- A Dynamic Array class which supports the retrieval, allocation and reversal of pre-existing elements in O(1). Appending and prepending new elements are supported in O(1*) amortised time. Removal at any index takes O(N) time, and a sort function is present which uses an efficient merge sort algorithm, sorting values in O(NlogN).
- A BitVector class which uses the previosuly implemented DynamicArray class to store 64-bit elements under the hood. It supports the retrieval, allocation, reversal and complement of pre-existing bits in O(1). Appending and prepending bits are supported in O(1*) amortised time.

# Instructions
1. Download folder.
2. Go to test.py in Data-Structures folder and run it (provided tests).
3. Modify or extend tests as required,or create new test based on functionality needed.