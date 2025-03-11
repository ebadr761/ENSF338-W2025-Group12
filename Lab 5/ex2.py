import random 
import timeit  

# Merge sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Priority Queue implementation using Merge Sort
class PriorityQueueMerge:
    def __init__(self):
        self.items = [] 
    
    def enqueue(self, item):
        self.items.append(item)
        self.items = merge_sort(self.items)
    
    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

# Priority Queue implementation using Insertion
class PriorityQueueInsert:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        index = 0
        while index < len(self.items) and self.items[index] < item:
            index += 1
        self.items.insert(index, item)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

# generate a list of 1000 tasks with 70% chance enqueue and 30% dequeue
def generate_tasks():
    tasks = []
    for _ in range(1000):
        if random.random() < 0.7: 
            value = random.randint(1, 1000000)
            tasks.append(('enqueue', value))
        else: 
            tasks.append(('dequeue', None))
    return tasks


def run_tasks(tasks, queue_class):
    q = queue_class()
    for op, val in tasks:
        if op == 'enqueue':
            q.enqueue(val)
        else:
            q.dequeue()


def measure_performance():
    task_lists = [generate_tasks() for _ in range(100)]
    
    merge_times = []
    for tasks in task_lists:
        time_taken = timeit.timeit(lambda: run_tasks(tasks, PriorityQueueMerge), number=1)
        merge_times.append(time_taken)
    
    insert_times = []
    for tasks in task_lists:
        time_taken = timeit.timeit(lambda: run_tasks(tasks, PriorityQueueInsert), number=1)
        insert_times.append(time_taken)
    
    avg_merge = sum(merge_times) / 100
    avg_insert = sum(insert_times) / 100
    
    print(f"MergeSort-based Priority Queue: {avg_merge:.6f} seconds")
    print(f"Insert-based Priority Queue: {avg_insert:.6f} seconds")

if __name__ == "__main__":
    measure_performance()

# The Insert-based Priority Queue is faster than the MergeSort-based Priority Queue.
# This is because the MergeSort-based approach sorts the entire list with every enqueue operation, this results in a O(n log n) complexity,
# which is computationally expensive. The Insert-based approach inserts elements in the correct position immediately, 
# requiring at most a O(n) time per insertion. Since both implementations have O(1) dequeue time, the performance difference is 
# entirely due to enqueue operations. Overall, the Insert-based Priority Queue is the more efficient choice for handling large 
# numbers of enqueue operations.