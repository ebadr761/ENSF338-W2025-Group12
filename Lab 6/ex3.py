import sys
import re

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def shunting_yard(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence and precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()  # Remove '('
        else:
            raise ValueError(f"Invalid token: {token}")
    while stack:
        op = stack.pop()
        if op == '(':
            raise ValueError("Mismatched parentheses")
        output.append(op)
    return output

def build_tree(rpn):
    stack = []
    for token in rpn:
        if token in {'+', '-', '*', '/'}:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
        else:
            stack.append(Node(int(token)))
    if not stack:
        raise ValueError("No expression provided")
    return stack[0]

def evaluate(node):
    if isinstance(node.value, int):
        return node.value
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    if node.value == '+':
        res = left_val + right_val
    elif node.value == '-':
        res = left_val - right_val
    elif node.value == '*':
        res = left_val * right_val
    elif node.value == '/':
        res = left_val / right_val
    else:
        raise ValueError(f"Unknown operator: {node.value}")
    # Return as integer if the result is a whole number
    return int(res) if isinstance(res, float) and res.is_integer() else res

def tokenize(expr):
    # Use regular expression to split the expression into tokens
    return re.findall(r'\d+|[\+\-\*/()]', expr)

def main():
    if len(sys.argv) < 2:
        print("Usage: python ex3.py \"expression\"")
        sys.exit(1)
    expr = sys.argv[1]
    try:
        tokens = tokenize(expr)
        if not tokens:
            raise ValueError("No input provided")
        rpn = shunting_yard(tokens)
        if not rpn:
            print(0)
            return
        # Handle single number case
        if len(rpn) == 1:
            print(int(rpn[0]))
            return
        tree = build_tree(rpn)
        result = evaluate(tree)
        print(result)
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()