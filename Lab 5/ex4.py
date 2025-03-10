# 1.
# Implement a queue which internally uses Python arrays. enqueue() must insert an
# element at the head, and dequeue() must remove an element from the tail.

class ArrQueue:
    def __init__(self):
        self.array = []        # Reference array (queue)
        self.head = 0          # Head points to start of queue
        self.tail = -1         # Tail points to end of queue
    
    # Function to add an element to queue at the head
    def enqueue(self, value):
        self.array.insert(self.head, value)
        
        # Tail index should be incremented
        self.tail += 1
        
    # Function to pop an element from queue
    def dequeue(self):
        # Check if queue is empty
        if self.tail == -1:
            print("Queue is empty. There is nothing to dequeue.")
            return None
        
        self.array.pop(self.tail)
        
        # Decrement tail
        self.tail -= 1
    

# 2.
# Implement a queue which internally uses a singly-linked list.
# enqueue() must add an element at the head, and dequeue() must remove
# the tail element (make sure to keep a tail pointer!)

# First we make a node class to which we use to enqueue
class Node:
    def __init__(self, newValue):
        self.data = newValue
        self.next = None

class LLQueue:
    def __init__(self):
        self.head = None
        self.tail= None
    
    # Function to add node containing element to queue
    def enqueue(self, value):
        
        # Create a new node storing desired value
        node = Node(value)
        
        # If queue, was previously empty, this node now becomes the head and tail
        if self.tail is None:
            self.head = self.tail = node
            return
        
        # Otherwise, add node at head (end of queue)
        self.head.next = node   # Set node currently at tail to point to this new node
        self.head = node        # Then make tail point to new tail
    
    # Function to remove an element from start of queue
    def dequeue(self):
        
        # Check if queue was already empty
        if self.head is None and self.tail is None:
            print("There are no elements currently in the queue to dequeue")
            return
        
        if self.head == self.tail:  # If there's only one element
            self.head = self.tail = None
            return
        
        # Traverse to the second-to-last node
        current = self.head
        while current.next and current.next.next:  
            current = current.next
        
        # Now `current` is the second-to-last node prior to removing the element at the start of queue
        current.next = None
        self.tail = current  # Update tail to the node next in line
        
# 3.
# Write a function which generates random lists of 10000 tasks. Each task is either an enqueue w/ probability 0.7, or a dequeue w/ probability 0.3
import random
def generateTasks(nTasks = 10000):
    tasks = []
    for n in range(nTasks):
        if random.random() < 0.7:   # 70% chance of enqueue
            tasks.append(('enqueue', random.randint(1, 100)))
        else:                       # 30% chance of dequeue
            tasks.append(('dequeue', None))
    return tasks

# 4.
# Measure the performance of both implementations on 100 such lists of tasks using timeit and print the results
import timeit
def measurePerformance(qClass, tasks):
    queue = qClass()
    for task in tasks:
        if task[0] == 'enqueue':
            queue.enqueue(task[1])
        elif task[0] == 'dequeue':
            queue.dequeue()

def main():
    tasksList = [generateTasks() for n in range(100)]
    
    arrQTimes = timeit.repeat(lambda: [measurePerformance(ArrQueue, tasks) for tasks in tasksList], repeat = 3, number = 1)
    LLQTimes = timeit.repeat(lambda: [measurePerformance(LLQueue, tasks) for tasks in tasksList], repeat = 3, number = 1)
    
    print("Array Queue Performance (seconds):", arrQTimes)
    print("Linked List Queue Performance (seconds):", LLQTimes)
    
    plotResults(arrQTimes, LLQTimes)

# 5.
# Plot the distribution of times (distributions for each implementation should be overlayed in the same plot; make sure to use consistent ranges) and discuss the results
import matplotlib.pyplot as plt
def plotResults(arrQTimes, LLQTimes):
    plt.hist(arrQTimes, bins = 30, alpha = 0.5, label = 'Array Queue')
    plt.hist(LLQTimes, bins = 30, alpha = 0.5, label = 'Linked List Queue')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Performance Distribution of Queue Implementations')
    plt.legend(loc = 'upper right')
    plt.show()

if __name__ == "__main__":
    main()