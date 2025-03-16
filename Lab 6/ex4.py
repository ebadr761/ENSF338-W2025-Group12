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

    
def test_sorted_array():
    print("\nTest 1: Input array is already a correctly sorted heap")

    input_array = [1, 3, 2, 7, 8, 4, 5]
    expected_output = input_array.copy() 
    
    heap = Heap()
    actual_output = heap.heapify(input_array)
    
    print(f"Input:    {input_array}")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {actual_output}")


def test_empty_array():
    print("\nTest 2: Input array is empty")
    
    input_array = []
    expected_output = []
    
    heap = Heap()
    actual_output = heap.heapify(input_array)
    
    print(f"Input:    {input_array}")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {actual_output}")


def test_random_array():
    import random
    
    print("\nTest 3: Input array is a long, randomly shuffled list of integers")
    
    input_array = [random.randint(0, 1000) for _ in range(20)]
    
    heap = Heap()
    actual_output = heap.heapify(input_array)
    
    print(f"Input:  {input_array}")
    print(f"Output: {actual_output}\n")

if __name__ == "__main__":
    test_sorted_array()
    test_empty_array()
    test_random_array()