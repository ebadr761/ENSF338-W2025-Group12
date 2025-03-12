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

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if not node:
            return Node(key)
        if random.random() < 0.5:  # Randomized insertion to prevent skewed trees
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if not node or node.key == key:
            return node is not None
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

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
# Using randomized insertion reduces the risk of creating a skewed tree.
# A standard BST built from sorted data is skewed, leading to O(n) search time.
# Randomized insertion creates a more balanced tree, leading to improved search efficiency.