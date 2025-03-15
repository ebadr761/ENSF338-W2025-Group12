import timeit
import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key): #From lec 19 slides
        current = self.root
        parent = None
        while current is not None:
            parent = current
            if key <= current.key:
                current = current.left
            else:
                current = current.right
        if self.root is None: # if the Binary Search Tree is empty just add the node as it's root
            self.root = Node(key)
        elif key <= parent.key:
            parent.left = Node(key)
        else:
            parent.right = Node(key)

    def search(self, key): #From lec 19 slides
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

def measure_search_performance(data):
    bst = BST()
    for num in data:
        bst.insert(num)

    def search_all():
        for num in data:
            bst.search(num)

    total_time = timeit.timeit(search_all, number=10)
    avg_time = total_time / (len(data) * 10)
    return avg_time, total_time

# Generate sorted and shuffled data
sorted_data = list(range(10000))
shuffled_data = sorted_data[:]
random.shuffle(shuffled_data)

# Measure times
sorted_avg, sorted_total = measure_search_performance(sorted_data)
shuffled_avg, shuffled_total = measure_search_performance(shuffled_data)

print(f"Sorted insertion BST - Avg search time: {sorted_avg:.8f}, Total time: {sorted_total:.8f}")
print(f"Shuffled insertion BST - Avg search time: {shuffled_avg:.8f}, Total time: {shuffled_total:.8f}")

# Discussion:
# A BST built from sorted data results in a skewed tree (like a linked list), leading to O(n) search time.
# A BST built from shuffled data is more balanced, leading to O(log n) search time, making searches MUCH faster.
