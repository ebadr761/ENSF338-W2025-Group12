class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 1
        self.balance = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def _calculate_height(self, node):
        if not node:
            return 0
        return node.height

    def _update_balance(self, node):
        while node:
            # Calculate heights of children
            left_height = self._calculate_height(node.left)
            right_height = self._calculate_height(node.right)

            # Update node height
            node.height = 1 + max(left_height, right_height)
            
            # Update balance factor
            node.balance = right_height - left_height

            node = node.parent

    def insert(self, value):
        # First insertion
        if not self.root:
            self.root = Node(value)
            return self.root

        # Find insertion point
        current = self.root
        parent = None
        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        # Create new node
        new_node = Node(value, parent)
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        # Update balance and find pivot
        self._update_balance(new_node)

        # Find pivot
        pivot = self._find_pivot(new_node)

        # Case identification
        if not pivot:
            print("Case #1: Pivot not detected")
        elif self._is_shorter_subtree(pivot, value):
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        else:
            print("Case 3 not supported")

        return self.root

    def _find_pivot(self, node):
        """Find the first unbalanced ancestor"""
        while node:
            if abs(node.balance) >= 2:
                return node
            node = node.parent
        return None

    def _is_shorter_subtree(self, pivot, value):
        """Determine if node is inserted into shorter subtree"""
        if pivot.balance > 0:
            # Right-heavy: check if inserted to left
            return value < pivot.value
        else:
            # Left-heavy: check if inserted to right
            return value > pivot.value

def main():
    # Test cases
    test_cases = [
        # Case 1: No pivot
        [10, 5, 15],
        
        # Case 2: Pivot exists, node added to shorter subtree
        [50, 30, 70, 80, 20],
        
        # Case 3: Not supported (right-heavy)
        [50, 30, 70, 80, 90],
        
        # Case 3: Not supported (left-heavy)
        [50, 30, 70, 20, 10]
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {case}")
        tree = AVLTree()
        for num in case:
            tree.insert(num)

if __name__ == "__main__":
    main()