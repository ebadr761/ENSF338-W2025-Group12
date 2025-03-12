# Exercise 2

# 1.
# Implement a binary search tree with insertion and search operations as seen in class,
# and binary search in arrays as seen in class

class Node:
    # Class to add node to tree
    def __init__(self, data, parent = None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class BinaryTree:
    # Binary Tree should be organized so that:
    #   - Every left child is less than (or equal to) the parent node
    #   - Every right child is greater than the parent node
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        # Insert a node into the Binary Tree
        if self.root is None:
            self.root = Node(data)
            return
        
        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right
        
        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)
        
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    
# 2.
# Measure BST performance using timeit as follows:
#   - Generate a 10,000-element sorted vector, shuffle, and use it to build a tree by inserting each element
#   - Search each element. Time the search (averaged across 10 tries for each element), and return average and total time
import timeit
import random

# Generate a sorted vector with 10,000 elements
vector = list(range(1, 10001))

# Shuffle the vector
random.shuffle(vector)

# Build the BST
bst = BinaryTree()
for data in vector:
    bst.insert(data)

# Measure search performance in BST
def bstTest():
    for data in vector:
        bst.search(data)

bstTime = timeit.timeit(bstTest, number=10) / 10
print(f"BST Search Average Time: {bstTime:.6f} seconds")


# 3.
# Using the same shuffled vector from question 2:
#   - Sort the vector
#   - Search each element using binary search. Time the search (averaged across 10 tries for each element), 
#     and return average and total time

vector.sort()

def binarySearch(arr, key):
    # Perform binary search on a sorted array.
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if key < arr[mid]:
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            return mid  # key found
    return -1   # failed in finding key


# 4.
# Discuss: which approach is faster? Why do you think that is?

# The worst-case complexity for the sorted array has a time complexity of O(log n). Meanwhile,
# The worst-case complexity for the Binary Search Tree can have a time complexity of O(n) if the 
# left and right subtrees differ in height (are not balanced). If the left and right subtree had the same height, it would
# have the same time complexity as the regular binary search.