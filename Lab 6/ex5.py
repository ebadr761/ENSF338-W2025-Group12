import random
import timeit

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value <= value:
                current = current.next
        
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1
    
    def dequeue(self):
        if self.head is None:
            return None
        
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value


class Heap:
    def __init__(self):
        self.heap = []
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def sift_down(self, index, heap_size):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)
        
        if left < heap_size and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < heap_size and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.swap(index, smallest)
            self.sift_down(smallest, heap_size)
    
    def sift_up(self, index):
        if index == 0:
            return
        parent = self.parent(index)
        if self.heap[index] < self.heap[parent]:
            self.swap(index, parent)
            self.sift_up(parent)
    
    def heapify(self, arr):
        self.heap = arr.copy()
        
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(i, n)
        return self.heap
    
    def enqueue(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)
        return self.heap
    
    def dequeue(self):
        n = len(self.heap)
        if n == 0:
            return None
        
        min_val = self.heap[0]
        self.swap(0, n - 1)
        self.heap.pop()
        
        if self.heap:
            self.sift_down(0, len(self.heap))
        
        return min_val
    

class HeapPriorityQueue:
    def __init__(self):
        self.heap = Heap()
    
    def enqueue(self, value):
        self.heap.enqueue(value)
    
    def dequeue(self):
        return self.heap.dequeue()
    
    def __len__(self):
        return len(self.heap.heap)


def generate_random_tasks(n=1000):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(0, 10000)))
        else:
            tasks.append(("dequeue", None))
    return tasks


def measure_performance(queue_class, tasks):
    queue = queue_class()
    
    def process_tasks():
        for task, value in tasks:
            if task == "enqueue":
                queue.enqueue(value)
            else:
                queue.dequeue()
    
    total_time = timeit.timeit(process_tasks, number=1)
    avg_time_per_task = total_time / len(tasks)
    return total_time, avg_time_per_task

if __name__ == "__main__":

    tasks = generate_random_tasks(n=10000)

    # Measure performance for the linked-list-based PriorityQueue
    total_list, avg_list = measure_performance(ListPriorityQueue, tasks)
    print("ListPriorityQueue:")
    print(f"Overall time: {total_list:.4f} seconds")
    print(f"Avg time per task: {avg_list:.8f} seconds")

    # Measure performance for the heap-based PriorityQueue
    total_heap, avg_heap = measure_performance(HeapPriorityQueue, tasks)
    print("\nHeapPriorityQueue:")
    print(f"Overall time: {total_heap:.4f} seconds")
    print(f"Avg time per task: {avg_heap:.8f} seconds")

# The heap-based implementation is significantly faster than the linked list implementation, this is 
# because the time complexity of the heap operations are O(log n) while, list insertions are O(n).
# Also, heaps store data in a compact array, which makes accessing elements faster and more efficient than a scattered linked list.
# Lastly, whether adding or removing elements, the heap stays fast, while the linked list slows down as it grows.
# Bigger Data = Bigger Difference, The more elements you have the slower the linked list gets compared to the heap.
