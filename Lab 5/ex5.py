# 1.
# Implement such a queue based on a fixed-size Python array
class CircularQueueArr:
    def __init__(self, size):
        self.size = size  # Size of the circular queue
        self.queue = [None] * size  # Initialize the queue with None
        self.head = 0  # Points to the head of the queue
        self.tail = 0   # Points to the tail of the queue
        self.count = 0  # Tracks the number of elements in the queue
    
    # Enqueue method
    def enqueue(self, element):
        if self.count == self.size:
            print(f"enqueue None")  # Queue is full
        else:
            self.queue[self.tail] = element
            print(f"enqueue {element}")
            self.tail = (self.tail + 1) % self.size  # Wrap-around behavior
            self.count += 1
    
    # Dequeue method
    def dequeue(self):
        if self.count == 0:
            print("dequeue None")  # Queue is empty
        else:
            element = self.queue[self.head]
            self.queue[self.head] = None  # Remove the element
            print(f"dequeue {element}")
            self.head = (self.head + 1) % self.size  # Wrap-around behavior
            self.count -= 1
            return element
    
    # Peek method
    def peek(self):
        if self.count == 0:
            print("peek None")  # Queue is empty
        else:
            element = self.queue[self.head]
            print(f"peek {element}")
            return element
      
    # Method to print queue  
    def printQueue(self):
        if self.count == 0:
            print("Queue is empty")
        else:
            current = self.head
            queue_elements = []
            for _ in range(self.count):  # Iterate for the number of elements in the queue
                queue_elements.append(str(self.queue[current]))
                current = (current + 1) % self.size  # Wrap-around behavior
            print("Queue state: " + " -> ".join(queue_elements))

# 2.
# Implement the queue again, this time using a circular linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CircularQueueLL:
    def __init__(self):
        self.head = None  # Points to the head of the queue
        self.tail = None  # Points to the tail of the queue
    
    # Enqueue method
    def enqueue(self, element):
        node = Node(element)
        
        if not self.head:  # If the queue is empty
            self.head = self.tail = node
            self.tail.next = self.head  # Circular link
            print(f"enqueue {element}")
        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head  # Circular link
            print(f"enqueue {element}")
    
    # Dequeue method
    def dequeue(self):
        if not self.head:  # If the queue is empty
            print("dequeue None")
        else:
            element = self.head.data
            if self.head == self.tail:  # Only one element in the queue
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head  # Update the circular link
            print(f"dequeue {element}")
            return element
    
    # Peek method
    def peek(self):
        if not self.head:  # If the queue is empty
            print("peek None")
        else:
            print(f"peek {self.head.data}")
            return self.head.data
        
    # Method to print queue  
    def printQueue(self):
        if not self.head:
            print("Queue is empty")
        else:
            current = self.head
            queue_elements = []
            while True:
                queue_elements.append(str(current.value))
                current = current.next
                if current == self.head:
                    break
            print("Queue state: " + " -> ".join(queue_elements))

# 3.
# Generate a list of 40 operations, together with expected output, that can be used
# to test correctness of implementation
# Operations list
operations = [
                       # Expected outcomes:
    ("enqueue", 1),    # Array: enqueue 1 | Linked List: enqueue 1
    ("enqueue", 2),    # Array: enqueue 2 | Linked List: enqueue 2
    ("enqueue", 3),    # Array: enqueue 3 | Linked List: enqueue 3
    ("enqueue", 4),    # Array: enqueue None (full queue) | Linked List: enqueue 4
    ("peek", None),    # Array: peek 1 | Linked List: peek 1
    ("dequeue", None), # Array: dequeue 1 | Linked List: dequeue 1
    ("dequeue", None), # Array: dequeue 2 | Linked List: dequeue 2
    ("peek", None),    # Array: peek 3 | Linked List: peek 3
    ("enqueue", 5),    # Array: enqueue 5 | Linked List: enqueue 5
    ("enqueue", 6),    # Array: enqueue 6 | Linked List: enqueue 6
    ("peek", None),    # Array: peek 3 | Linked List: peek 3
    ("dequeue", None), # Array: dequeue 3 | Linked List: dequeue 3
    ("dequeue", None), # Array: dequeue 4 | Linked List: dequeue 4
    ("peek", None),    # Array: peek 5 | Linked List: peek 5
    ("dequeue", None), # Array: dequeue 5 | Linked List: dequeue 5
    ("peek", None),    # Array: peek 6 | Linked List: peek 6
    ("dequeue", None), # Array: dequeue 6 | Linked List: dequeue 6
    ("dequeue", None), # Array: dequeue None (empty queue) | Linked List: dequeue None (empty queue)
    ("peek", None),    # Array: peek None (empty queue) | Linked List: peek None (empty queue)
    ("enqueue", 7),    # Array: enqueue 7 | Linked List: enqueue 7
    ("enqueue", 8),    # Array: enqueue 8 | Linked List: enqueue 8
    ("peek", None),    # Array: peek 7 | Linked List: peek 7
    ("dequeue", None), # Array: dequeue 7 | Linked List: dequeue 7
    ("enqueue", 9),    # Array: enqueue 9 | Linked List: enqueue 9
    ("peek", None),    # Array: peek 8 | Linked List: peek 8
    ("dequeue", None), # Array: dequeue 8 | Linked List: dequeue 8
    ("dequeue", None), # Array: dequeue 9 | Linked List: dequeue 9
    ("peek", None),    # Array: peek None (empty queue) | Linked List: peek None (empty queue)
    ("enqueue", 10),   # Array: enqueue 10 | Linked List: enqueue 10
    ("enqueue", 11),   # Array: enqueue 11 | Linked List: enqueue 11
    ("peek", None),    # Array: peek 10 | Linked List: peek 10
    ("dequeue", None), # Array: dequeue 10 | Linked List: dequeue 10
    ("enqueue", 12),   # Array: enqueue 12 | Linked List: enqueue 12
    ("dequeue", None), # Array: dequeue 11 | Linked List: dequeue 11
    ("dequeue", None), # Array: dequeue 12 | Linked List: dequeue 12
    ("dequeue", None), # Array: dequeue None (empty queue) | Linked List: dequeue None (empty queue)
]

# Example of using the above operations:
myQueue = CircularQueueArr(3)  # For Array queue

print("\n---Testing Array Circular Queue---\n")
for operation, value in operations:
    if operation == "enqueue":
        myQueue.enqueue(value)
    elif operation == "dequeue":
        myQueue.dequeue()
    elif operation == "peek":
        myQueue.peek()
        
# Print result
myQueue.printQueue()

print("\n---Testing Linked List Circular Queue---\n")

myQueue = CircularQueueLL()  # For Linked List queue
for operation, value in operations:
    if operation == "enqueue":
        myQueue.enqueue(value)
    elif operation == "dequeue":
        myQueue.dequeue()
    elif operation == "peek":
        myQueue.peek()

# Print result
myQueue.printQueue()