import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_number(token): # used to convert tokens to numbers
    try:
        return int(token)
    except ValueError:
        return None

def parse_expression(tokens):
    # Base case: empty list
    if not tokens:
        return None
    
    # If we only have a single token, it must be a number
    if len(tokens) == 1:
        num = is_number(tokens[0])
        if num is not None:
            return Node(num)
        raise ValueError(f"Expected number, got {tokens[0]}")
    
    # If the expression is surrounded by parentheses, remove them
    if tokens[0] == '(' and tokens[-1] == ')':
        # Find matching parenthesis
        count = 0
        for i, token in enumerate(tokens):
            if token == '(':
                count += 1
            elif token == ')':
                count -= 1
                if count == 0 and i == len(tokens) - 1:
                    # This is the matching closing parenthesis
                    return parse_expression(tokens[1:-1]) # use recursion to evaluate inside ()
    
    # Find the operator at the root level (not inside nested parentheses)
    paren_count = 0
    for i in range(len(tokens) - 1, -1, -1):  # Scan right-to-left for lower precedence ops (+, -) first
        if tokens[i] == ')':
            paren_count += 1
        elif tokens[i] == '(':
            paren_count -= 1
        elif paren_count == 0 and tokens[i] in ['+', '-']:
            return create_operator_node(tokens, i)
    
    # No +/- found, look for * and / (higher precedence)
    for i in range(len(tokens) - 1, -1, -1):
        if tokens[i] == ')':
            paren_count += 1
        elif tokens[i] == '(':
            paren_count -= 1
        elif paren_count == 0 and tokens[i] in ['*', '/']:
            return create_operator_node(tokens, i)
    
    # If we reach here, the expression might be malformed
    raise ValueError(f"Invalid expression: {' '.join(tokens)}")

def create_operator_node(tokens, op_index):
    node = Node(tokens[op_index])
    node.left = parse_expression(tokens[:op_index])
    node.right = parse_expression(tokens[op_index+1:])
    return node
'''Binary Search Tree built from parse_expression and create_operator_node'''

def evaluate(node):
    if node is None:
        return 0
    
    # Leaf node (number)
    if isinstance(node.value, int):
        return node.value
    
    # Post-order traversal: evaluate left, then right, then apply operator
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
# IDEA: it processes the left and right subexpressions on each side of op
                #ex. for 3+2:    "+" 
#                                / \
#                               3   2
    # Apply the operator
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val
    else:
        raise ValueError(f"Unknown operator: {node.value}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python ex3.py \"EXPRESSION\"")
        return
    
    expression = sys.argv[1]
    
    # Handle simple number case (if input is just a single number)
    try:
        value = int(expression)
        print(value)
        return
    except ValueError:
        pass
    
    # Parse and evaluate the expression
    try:
        tokens = expression.split()
        root = parse_expression(tokens)
        result = evaluate(root)
        
        # Print as integer if possible, otherwise as float
        if result == int(result):
            print(int(result))
        else:
            print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()