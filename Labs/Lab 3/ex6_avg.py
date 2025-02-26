import time
import random
import matplotlib.pyplot as plt
import sys
import matplotlib.ticker as ticker
sys.setrecursionlimit(200000)

# linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Sizes to test
sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear = []
quicksort_binary = []

# Run tests
for size in sizes:
    lin_time_total = 0
    qs_bin_time_total = 0
    
    for x in range(100):  # 100 random trials
        arr = [random.randint(0, size) for x in range(size)]
        target = random.choice(arr)  # Target must be in array
        
        # Linear search
        start_time = time.time()
        linear_search(arr, target)
        lin_time_total += (time.time() - start_time)
        
        # Quicksort + Binary search
        start_time = time.time()
        sorted_arr = quicksort(arr)
        binary_search(sorted_arr, target)
        qs_bin_time_total += (time.time() - start_time)
    
    linear.append(lin_time_total / 100)
    quicksort_binary.append(qs_bin_time_total / 100)

# Plot results
plt.figure(figsize=(8, 5))

plt.plot(sizes, linear, marker='o', label='Linear Search')
plt.plot(sizes, quicksort_binary, marker='s', label='Quicksort + Binary Search')

plt.xlabel('Size')
plt.ylabel('Average Time (s)')

plt.title('Linear Search vs. Quicksort + Binary Search')

plt.xscale("log")
plt.yscale("log")

plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter()) # Decimal notation
plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter()) # Decimal notation

plt.legend()
plt.grid()
plt.show()


# Linear search is faster for small input sizes becasuse it doesnt need sorting as
# it scans through the array once. Binary search requires sorting the array first
# which usually takes more time. the advantages of binary search only shows when
# the array is already sorted.

