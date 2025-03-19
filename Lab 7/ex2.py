# Exercise 2

import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.balanceFactor = 0

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
        
        newNode = Node(data, parent)
        if data <= parent.data:
            parent.left = newNode
        else:
            parent.right = newNode
        
        # Implement code to identify the pivot node on node insertion [0.25 pts]
        pivot = self.findPivot(newNode)
        if pivot is None:
            # Implement code to identify case 1 (pivot does not exist) [0.25 pts]
            print("Case #1: Pivot not detected")
        else:
            if self.isInsertedInShorterSubtree(pivot, newNode):
                # Implement code to identify case 2 (pivot exist but node is being inserted into shorter subtree) [0.25 pts]
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case 3 not supported")
        
        # The code should also update node balances
        self.updateBalance(newNode)
    
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
    
    def findPivot(self, node):
        while node.parent:
            if abs(self.balance(node.parent)) > 1:
                return node.parent
            node = node.parent
        return None
    
    def isInsertedInShorterSubtree(self, pivot, node):
        leftHeight = self.height(pivot.left)
        rightHeight = self.height(pivot.right)
        return (leftHeight > rightHeight and node == pivot.right) or (rightHeight > leftHeight and node == pivot.left)
    
    def updateBalance(self, node):
        while node:
            node.balanceFactor = self.balance(node)
            node = node.parent

def generateSearchTasks(n = 1000):
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

# Measure performance
balanceValues, searchTimes = measurePerformance(bst, tasks)

# Generate scatterplot
plt.scatter(balanceValues, searchTimes)
plt.xlabel("Absolute Balance")
plt.ylabel("Average Search Time (s)")
plt.title("Balance vs. Search Time in BST")
plt.show()

# Implement four test cases. Each test case consists into adding an appropriate sequence of nodes: [0.25 pts]
bstTest = BinaryTree()
print("\nTest Case 1: Adding a node results in case 1")
bstTest.insert(10)

print("\nTest Case 2: Adding a node results in case 2")
bstTest.insert(5)
bstTest.insert(15)
bstTest.insert(3)

print("\nTest Case 3: Adding a node results in case 3 (the code should print 'Case 3 not supported')")
bstTest.insert(12)
bstTest.insert(18)
