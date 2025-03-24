import random
import timeit
import matplotlib.pyplot as plt

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.balance = 0

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right

    def calculate_balance(self, node):
        if not node:
            return 0
        
        def tree_height(n):
            if not n:
                return 0
            return 1 + max(tree_height(n.left), tree_height(n.right))
        
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)
        return abs(left_height - right_height)

    def search(self, value):
        current = self.root
        while current:
            if current.value == value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

def main():
    # Generate first 1000 integers
    numbers = list(range(1, 1001))
    
    search_times = []
    balance_values = []

    # Shuffle multiple times for search tasks
    for _ in range(1000):
        random.shuffle(numbers)
        
        # Create and populate BST
        tree = BST()
        for num in numbers:
            tree.insert(num)
        
        # Measure search performance using timeit
        def search_all():
            for num in numbers:
                tree.search(num)
        
        search_time = timeit.timeit(search_all, number=1)
        search_times.append(search_time)
        
        # Track tree balance
        max_balance = 0
        def traverse_and_find_max_balance(node):
            nonlocal max_balance
            if not node:
                return
            max_balance = max(max_balance, tree.calculate_balance(node))
            traverse_and_find_max_balance(node.left)
            traverse_and_find_max_balance(node.right)
        
        traverse_and_find_max_balance(tree.root)
        balance_values.append(max_balance)

    # Create scatterplot
    plt.figure(figsize=(10, 6))
    plt.scatter(balance_values, search_times, alpha=0.5)
    plt.xlabel('Absolute Balance Value')
    plt.ylabel('Search Time')
    plt.title('Balance vs Search Performance')
    plt.tight_layout()
    plt.savefig('balance_performance.png')
    plt.close()

if __name__ == "__main__":
    main()