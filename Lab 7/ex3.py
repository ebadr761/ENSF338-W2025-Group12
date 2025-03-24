class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            node.balance = self._get_balance(node)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        self._update_height(z)
        self._update_height(y)

        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        self._update_height(y)
        self._update_height(x)

        return x

    def insert(self, root, value):
        # Standard BST insertion
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # Update height and balance
        self._update_height(root)

        # Get the balance factor
        balance = root.balance

        # Case 3a: Outside subtree (LL or RR rotation)
        if balance > 1 and value < root.left.value:
            print("Case #3a: adding a node to an outside subtree")
            return self._right_rotate(root)

        if balance < -1 and value > root.right.value:
            print("Case #3a: adding a node to an outside subtree")
            return self._left_rotate(root)

        # Case 3b: Not supported in this implementation
        if balance > 1 or balance < -1:
            print("Case 3b not supported")

        return root

def main():
    # Test cases
    test_cases = [
        # Case 3a: Will trigger when adding 5 (LL rotation)
        [10, 8, 12, 6, 9, 5],  
        
        # Case 3b: Will trigger "not supported" when adding 7 (LR imbalance)
        [10, 5, 15, 2, 8, 7]
    ]

    print("\nTest Cases Demonstrations:")
    for i, case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {case}")
        tree = AVLTree()
        tree.root = None
        for num in case:
            tree.root = tree.insert(tree.root, num)

if __name__ == "__main__":
    main()