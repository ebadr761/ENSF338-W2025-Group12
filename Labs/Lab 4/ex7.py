import timeit
import matplotlib.pyplot as plt
import numpy as np

class Node:
    # Class to represent a node in a linked list.
    def __init__(self, data):
        self.data = data  # Store integer data
        self.next = None  # Pointer to the next node


# This class includes the answer to question 7.2
class LinkedList:
    # Class to represent a singly linked list storing integers.
    def __init__(self):
        self.head = None  # Head of the linked list

    def appendNode(self, data):
        # Append a new node with given data to the end of the list.
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
            return
        
        tempNode = self.head
        
        while tempNode.next:
            tempNode = tempNode.next
        tempNode.next = newNode

    def getElementAtPos(self, pos):
        # Retrieve the node at a specific position.
        tempNode = self.head
        index = 0
        
        while tempNode and index < pos:
            tempNode = tempNode.next
            index += 1
        return tempNode

    def getSize(self):
        # Get the size of the linked list.
        size = 0
        tempNode = self.head
        
        while tempNode:
            size += 1
            tempNode = tempNode.next
        return size
    
    def reverseOriginal(self):
        # Original O(n^2) reverse method.
        newHead = None
        prevNode = None
        
        for i in range(self.getSize() - 1, -1, -1):
            currNode = self.getElementAtPos(i)
            currNewNode = Node(currNode.data)
            if newHead is None:
                newHead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newHead
    
    # Answer to 7.2
    def reverseOptimized(self):
        # Optimized O(n) reverse method.
        prevNode = None
        currNode = self.head
        
        while currNode:
            next = currNode.next  # Store next node
            currNode.next = prevNode  # Reverse pointer
            prevNode = currNode  # Move prevNode forward
            currNode = next  # Move currNode forward
        self.head = prevNode  # Update head

# Function to measure execution time of a given reverse method using timeit
def measureTime(reverseMethod, size, runs=100):
    def setup():
        linkedList = LinkedList()
        for i in range(size):
            linkedList.appendNode(i)
        return linkedList
    
    # Reduce the number of runs for reverseOriginal to prevent long execution time
    runs = 100 if reverseMethod == 'reverseOptimized' else max(10, 100000 // (size * size))
    
    return timeit.timeit(lambda: getattr(setup(), reverseMethod)(), number=runs) / runs  # Average time

# List sizes to test
sizes = [1000, 2000, 3000, 4000]
originalTimes = []
optimizedTimes = []

# Measure time for both methods
for size in sizes:
    originalTimes.append(measureTime('reverseOriginal', size))
    optimizedTimes.append(measureTime('reverseOptimized', size))

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(sizes, originalTimes, marker='o', label='Original Reverse (O(n^2))')
plt.plot(sizes, optimizedTimes, marker='s', label='Optimized Reverse (O(n))')
plt.xlabel('Input Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Performance Comparison of Reverse Methods')
plt.legend()
plt.grid(True)
plt.show()