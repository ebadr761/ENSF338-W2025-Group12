import time
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker 
import sys
sys.setrecursionlimit(200000)

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Quicksort (Worst-Case)
def quicksort_worst(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  #  First element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_worst(left) + middle + quicksort_worst(right)

# Binary Search
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

# Sizes for testing
sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
linear_times = []
quicksort_worst_times = []

# Run tests
for size in sizes:
    lin_time_total = 0
    qs_worst_time_total = 0

    for x in range(100): # reducing number of trials could reduce time to run
        target = random.randint(0, size - 1) 

        # Generate Worst-Case Input for Quicksort
        worst_case_arr = list(range(size)) 

        # Linear Search times
        start_time = time.perf_counter()
        linear_search(worst_case_arr, target)
        lin_time_total += (time.perf_counter() - start_time)

        # Worst-case Quicksort + Binary Search times
        start_time = time.perf_counter()
        sorted_worst_arr = quicksort_worst(worst_case_arr) 
        binary_search(sorted_worst_arr, target)
        qs_worst_time_total += (time.perf_counter() - start_time)

    # Store runtimes
    linear_times.append(lin_time_total / 100)
    quicksort_worst_times.append(qs_worst_time_total / 100)

# Plot results(TAKES LONG TIME TO RUN)
plt.figure(figsize=(8, 5))

plt.plot(sizes, linear_times, marker='o', label='Linear Search') 
plt.plot(sizes, quicksort_worst_times, marker='s', label='Worst-Case Quicksort + Binary Search')  
plt.xlabel('Size')
plt.ylabel('Average Time (s)')

plt.title('Linear Search vs. Worst-Case Quicksort + Binary Search')

plt.xscale("log")
plt.yscale("log")

plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter()) 
plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter())

plt.legend()
plt.grid()
plt.show()

# Linear search is faster than  quicksort + binary search in worst-case because quicksort performs poorly on sorted arrays leading to O(n^2) time complexity.
# Quicksort + binary serach is only useful if sorting is effecient O(nlogn), otherwise linear search O(n) is better.
# If multiple searches are neeed, it better to sort the array once then use bianry search can be more benificial.
