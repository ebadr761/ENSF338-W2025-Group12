class Node:
    # Class to represent a node in a linked list.
    def __init__(self, data):
        self.data = data  # Store integer data
        self.nextNode = None  # Pointer to the next node

class LinkedList:
    # Class to represent a singly linked list storing integers.
    def __init__(self):
        self.headNode = None  # Head of the linked list

    def appendNode(self, data):
        # Append a new node with given data to the end of the list.
        newNode = Node(data)
        if not self.headNode:
            self.headNode = newNode
            return
        tempNode = self.headNode
        while tempNode.nextNode:
            tempNode = tempNode.nextNode
        tempNode.nextNode = newNode

    def binarySearch(self, num):
        # Performs binary search on the linked list (requires sorting).
        valuesArray = []  # Convert linked list to an array
        tempNode = self.headNode
        while tempNode:
            valuesArray.append(tempNode.data)
            tempNode = tempNode.nextNode
        
        valuesArray.sort()  # Sort the values for binary search
        
        start, end = 0, len(valuesArray) - 1
        while start <= end:
            mid = (start + end) // 2
            if valuesArray[mid] == num:
                return True  # Number found
            elif valuesArray[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        return False  # Number not found

class Array:
    # Class to represent an array storing integers with binary search.
    def __init__(self):
        self.dataArray = []  # Internal Python array to store integers

    def appendElement(self, num):
        # Append an integer to the array.
        self.dataArray.append(num)

    def binarySearch(self, num):
        # Performs binary search on the sorted array.
        self.dataArray.sort()  # Ensure the array is sorted
        start, end = 0, len(self.dataArray) - 1
        while start <= end:
            mid = (start + end) // 2
            if self.dataArray[mid] == num:
                return True  # Number found
            elif self.dataArray[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        return False  # Number not found

# Example Usage:
linkedList = LinkedList()
linkedList.appendNode(3)
linkedList.appendNode(1)
linkedList.appendNode(4)
linkedList.appendNode(2)
print(linkedList.binarySearch(3))  # Output: True
print(linkedList.binarySearch(5))  # Output: False

array = Array()
array.appendElement(3)
array.appendElement(1)
array.appendElement(4)
array.appendElement(2)
print(array.binarySearch(3))  # Output: True
print(array.binarySearch(5))  # Output: False

# Question 1.4
# Since we already know that the complexity of a binary search for array is O(logn). 
# What is the complexity of binary search of binary search for linked lists?

# An array allows direct access to any element using indexing which has a complexity of O(n)
# A linked list does NOT support direct access to elements by index.
# Binary search has it's O(log n) by jumping to the middle index and then halving the search space.
# To find the middle element in a linked list requires us to traverse sequentially which has a complexity of O(n).
# This means that every time we half the list, our new complexity is O(n/2) and so forth.
# Therefore, this results in the complexity being O(n) + O(n/2) + ... + O(n/(2x)) with x being the number
# of times the binarySearch halves the linked list.
# Finally, our linked list binary search complexity can just be represented with O(n).

# Performance Measurement for Binary Search in Linked List vs Array
import time
import matplotlib.pyplot as plt
import numpy as np

sizes = [1000, 2000, 4000, 8000]
linkedListTimes = []
arrayTimes = []

for size in sizes:
    # Create Linked List and Array
    linkedList = LinkedList()
    arrayList = Array()
    elements = list(range(size))  # Sorted elements
    for elem in elements:
        linkedList.appendNode(elem)
        arrayList.appendElement(elem)
    
    # Measure Linked List Binary Search Time
    start = time.time()
    linkedList.binarySearch(size // 2)
    end = time.time()
    linkedListTimes.append(end - start)
    
    # Measure Array Binary Search Time
    start = time.time()
    arrayList.binarySearch(size // 2)
    end = time.time()
    arrayTimes.append(end - start)

# Plot Results
plt.figure(figsize=(8, 6))
plt.plot(sizes, linkedListTimes, marker='o', label='Linked List Binary Search (O(n))')
plt.plot(sizes, arrayTimes, marker='s', label='Array Binary Search (O(log n))')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Binary Search Performance in Linked List vs Array')
plt.legend()
plt.grid(True)
plt.show()
