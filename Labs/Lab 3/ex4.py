import time
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.setrecursionlimit(20000)

# Quicksort implementation
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

# Partition function
def partition(arr, low, high):
    pivot = arr[low]  # This sets the pivot as the FIRST element
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[low] = arr[low], arr[i + 1] # Swaps the pivot to the correct position
    return i + 1

# Quicksort on worst-case
sizes = [100, 500, 1000, 3000, 5000]
time_taken = [] # store time taken for each size
for size in sizes:
    worst_case = list(range(size)) # Sorted list
    start_time = time.time()
    quicksort(worst_case, 0, len(worst_case) - 1)
    end_time = time.time()
    time_taken.append(end_time - start_time)
    print(f"Size: {size}, Time: {end_time - start_time:.6f}")

# Plotting the time
plt.figure(figsize=(8, 5))
plt.plot(sizes, time_taken, 'o-', label='Time')

# Quadratic function O(n^2)
coeffs = np.polyfit(sizes, time_taken, 2)
x_interp = np.linspace(min(sizes), max(sizes), 100)
y_interp = np.polyval(coeffs, x_interp)
plt.plot(x_interp, y_interp, '--', label='Quadratic Fit')

plt.xlabel('Size')
plt.ylabel('Time (seconds)')
plt.title('Quicksort Worst-Case: O(n^2)')
plt.legend()
plt.grid()
plt.show()
