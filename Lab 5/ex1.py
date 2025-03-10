import sys
#1. Recieve a string representing an expression as a command line parameter
#2. Implement a stack data structure
#3. Using the stack, compute the overall result of an expression
def main():
    if len(sys.argv) < 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)
    
    expr = sys.argv[1]
    # Insert spaces around parentheses and then split into tokens.
    tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
    
    stack = []
    
    for token in tokens:
        if token != ')':
            # Convert numbers to integers; leave parentheses and operators as strings.
            if token not in ('(', '+', '-', '*', '/'):
                try:
                    token = int(token)
                except ValueError:
                    print("Error: invalid token", token)
                    sys.exit(1)
            stack.append(token)
        else:
            # When a closing parenthesis is encountered,
            # pop tokens until the matching '(' is found.
            expr_list = []
            while stack:
                t = stack.pop()
                if t == '(':
                    break
                expr_list.append(t)
            # The tokens were pushed in order: operator, operand1, operand2,
            # but they were popped in reverse order. Reverse them back.
            expr_list.reverse()
            
            if len(expr_list) != 3:
                print("Error: invalid expression structure:", expr_list)
                sys.exit(1)
            
            op, a, b = expr_list
            
            if op == '+':
                res = a + b
            elif op == '-':
                res = a - b
            elif op == '*':
                res = a * b
            elif op == '/':
                # Use integer division (adjust if float division is desired)
                res = a // b
            else:
                print("Error: unknown operator", op)
                sys.exit(1)
            stack.append(res)
    
    if len(stack) != 1:
        print("Error: invalid expression. Final stack:", stack)
        sys.exit(1)
    
    print(stack[0])

if __name__ == '__main__':
    main()
