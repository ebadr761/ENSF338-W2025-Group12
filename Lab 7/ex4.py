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

    def _lr_rotate(self, node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)

    def _rl_rotate(self, node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

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

        # Case 3b: Inside subtree (LR or RL rotation)
        if balance > 1 and value > root.left.value:
            print("Case #3b: adding a node to an inside subtree")
            return self._lr_rotate(root)

        if balance < -1 and value < root.right.value:
            print("Case #3b: adding a node to an inside subtree")
            return self._rl_rotate(root)

        return root

def main():
    # Test cases for Case 3b
    test_cases = [
        # Case 3b LR rotation (insert order: left-right)
        [30, 10, 40, 5, 15, 12],  # Inserting 12 will trigger LR
        
        # Case 3b RL rotation (insert order: right-left)
        [30, 20, 50, 40, 60, 35]  # Inserting 35 will trigger RL
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