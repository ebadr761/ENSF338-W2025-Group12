#1. Implement a stack that uses arrays
class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("Cannot pop from empty stack!")
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1] # Returns most recently added element
        
    def isEmpty(self):
        return len(self.stack) == 0 # returns true if length is 0, returns false otherwise
    
#2. Implement a stack that uses a singly-linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.isEmpty():
            popped_value = self.head.value
            self.head = self.head.next
            return popped_value
        else:
            raise IndexError("Cannot pop from empty stack!")
    
    def peek(self):
        if not self.isEmpty():
            return self.head.value
        else:
            raise IndexError("Cannot peek from empty stack!")
        
    def isEmpty(self):
        return self.head is None # returns true if self.head is None, returns false otherwise

#3. Write a function to generate random tasks (push with probability 0.7 and pull with probability 0.3)
import random

def generate_tasks(num_tasks=10000):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:
            tasks.append("push")
        else:
            tasks.append("pop")
    return tasks

#4. Measure the performance of both implementations using the timeit module
import timeit

# Time the performance for both StackArray and StackLinkedList
def measure_performance(stack_type, num_tasks=10000):
    tasks = generate_tasks(num_tasks)
    
    # Initialize the chosen stack type
    if stack_type == "array":
        stack = StackArray()
    elif stack_type == "linked_list":
        stack = StackLinkedList()
    
    def run_stack_operations():
        for task in tasks:
            if task == "push":
                stack.push(random.randint(1, 100))
            elif task == "pop":
                if not stack.isEmpty():
                    stack.pop()

    # Time the execution
    return timeit.timeit(run_stack_operations, number=100)  # 100 iterations

# Measure the performance for both stack implementations
array_time = measure_performance("array")
linked_list_time = measure_performance("linked_list")

print(f"Array-based Stack Time: {array_time:.4f} seconds")
print(f"Linked List-based Stack Time: {linked_list_time:.4f} seconds")

#5. Plot the distribution of times
import matplotlib.pyplot as plt

# Collect performance times for multiple runs
def collect_performance_data(stack_type, num_runs=100, num_tasks=10000):
    times = []
    for _ in range(num_runs):
        times.append(measure_performance(stack_type, num_tasks))
    return times

# Collect data for both stack implementations
array_times = collect_performance_data("array")
linked_list_times = collect_performance_data("linked_list")

# Plot the distribution of times
plt.figure(figsize=(10, 6))
plt.hist(array_times, bins=30, alpha=0.7, label="Array-based Stack", color='blue', edgecolor='black')
plt.hist(linked_list_times, bins=30, alpha=0.7, label="Linked List-based Stack", color='green', edgecolor='black')
plt.title('Stack Performance Distribution (Array vs Linked List)')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend()

# Save the plot as a PNG file (or you can choose other formats like PDF, SVG, etc.)
plt.savefig('stack_performance_distribution.png')

# Optional: Display the plot (if you still want to see it after saving)
plt.show()
# As shown by the plots which displayed the times it took to run 100 operations, the array based stack 
# is significantly faster than the linked list in performing operations.
