# Exercise 5
import random
import timeit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 5.1
# Implement linear search and binary search
def linearSearch(vector, n, key):
    # Iterate through the vector
    for i in range(n):
        if vector[i] == key:
            return i    # Found, return the index  
    return -1           # Not found, return -1
      
def binarySearch(vector, first, last, key):
    # Works only with sorted arrays
    if first <= last:
        mid = (first + last) // 2
        if key == vector[mid]:
            # Success: key was found
            return mid 
        elif key < vector[mid]:
            return binarySearch(vector, first, mid - 1, key)
        elif key > vector[mid]:
            return binarySearch(vector, mid + 1, last, key)
    # Failure: key not found
    return -1

# 5.2
# Measure the performance of each on sorted vectors of 1000, 2000,
# 4000, 8000, 16000, 32000 elements . In each case, you must do the following 
# for 1000 times, and compute the average:

# a. Pick a random element in the vector

# b. Measure the time it takes to find the element using timeit, using 100 iterations
# (number = 100)

def measureTime(searchFunc, vector, key, iterations=100):
    # Measures the time taken to perform a search function with a given vector and key.
    return timeit.timeit(lambda: searchFunc(vector, key), number=iterations)

# Generate sorted vectors of increasing size
sizes = [1000, 2000, 4000, 8000, 16000, 32000]
linearTimes = []
binaryTimes = []
for size in sizes:
    vector = list(range(size))  # Sorted vector
    key = random.choice(vector)  # Pick a random element in vector
    
    
    #  Measure the time it takes to find the element using timeit, using 100 iterations
    # Measure time for linear search
    linearTime = measureTime(lambda v, k: linearSearch(v, len(v), k), vector, key)
    
    # Measure time for binary search
    binaryTime = measureTime(lambda v, k: binarySearch(v, 0, len(v) - 1, k), vector, key)
    
    # Append times to corresponding list
    linearTimes.append(linearTime)
    binaryTimes.append(binaryTime)
    
# 5.3
# Each plot should also interpolate the data points with an
# appropriate function. For example, linear complexity with a linear
# function, quadratic complexity with a quadratic function, etc.

# Define fitting functions
def linearFunc(x, a, b):
    # Linear function: f(x) = ax + b
    return a * x + b

def logFunc(x, a, b):
    # Logarithmic function: f(x) = a * log(x) + b
    return a * np.log(x) + b

# Convert lists to numpy arrays for curve fitting
sizesNp = np.array(sizes)
linearTimesNp = np.array(linearTimes)
binaryTimesNp = np.array(binaryTimes)

# Fit functions to measured times
linearParams, _ = curve_fit(linearFunc, sizesNp, linearTimesNp)
binaryParams, _ = curve_fit(logFunc, sizesNp, binaryTimesNp)

# Plot results
plt.figure(figsize=(10, 5))
plt.scatter(sizes, linearTimes, color='blue', label='Linear Search Times')
plt.plot(sizes, linearFunc(sizesNp, *linearParams), color='blue', linestyle='dashed', label='Linear Fit')

plt.scatter(sizes, binaryTimes, color='red', label='Binary Search Times')
plt.plot(sizes, logFunc(sizesNp, *binaryParams), color='red', linestyle='dashed', label='Log Fit')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Search Algorithm Complexity Visualization')
plt.show()

# Display fitted function parameters
print(f"Linear Fit: a={linearParams[0]:.6f}, b={linearParams[1]:.6f}")
print(f"Binary Fit: a={binaryParams[0]:.6f}, b={binaryParams[1]:.6f}")


# 5.4
# Discuss the results. For each interpolating function, describe (1) the
# type of function, and (2) the parameters of the function. Are the
# results what you expected? Why?

# The results align with expectations: linear search follows a linear function f(x)=ax+b,
# with parameters a = 0.000005 and b = −0.014002, showing a steady increase in time with input size. 
# Binary search follows a logarithmic function f(x) = alog(x)+b, with parameters a = 0.000032 and b = 0.000141, 
# demonstrating much slower growth in time as input size increases. 
# This confirms that binary search is more efficient than linear search for larger datasets.
# The results were expected, as linear search complexity is O(n) and binary search complexity is O(log n).
