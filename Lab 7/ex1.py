# Exercise 1

import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
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
    
    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))
    
    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.right) - self.height(node.left)

def generateSearchTasks(n=1000):
    lst = list(range(1, 1001))
    tasks = []
    for i in range(n):
        random.shuffle(lst)
        tasks.append(lst[:])  # Store a shuffled copy
    return tasks

def measurePerformance(bst, tasks):
    searchTimes = []
    balanceValues = []
    
    for task in tasks:
        def bstSearch():
            for value in task:
                node = bst.search(value)
                if node:
                    balanceValues.append(abs(bst.balance(node)))
        
        searchTime = timeit.timeit(bstSearch, number = 1)
        searchTimes.append(searchTime / len(task))  # Average time per search
    
    return balanceValues, searchTimes

# Build the BST with numbers 1 to 1000
values = list(range(1, 1001))
random.shuffle(values)
bst = BinaryTree()
for value in values:
    bst.insert(value)

# Generate 1000 random search tasks
tasks = generateSearchTasks()

# Measure average performance and largest absolute balance value
balanceValues, searchTimes = measurePerformance(bst, tasks)

# Generate scatterplot with absolute balance on the X axis and search time on the Y axis
plt.scatter(balanceValues, searchTimes)
plt.xlabel("Absolute Balance")
plt.ylabel("Average Search Time (s)")
plt.title("Balance vs. Search Time in BST")
plt.show()
