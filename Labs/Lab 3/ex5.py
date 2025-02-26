# Exercise 5
# Task: 
# 1. Implement both "traditional" insertion sort and binary insertion sort
# 2. Devise and run an experiment where you test each algorithm on a number of average-case inputs of increasing length
# 3. Plot the results of both algorithms within the same plot, together with appropriate interpolating functions
# 4. Discuss the results: which algorithm is faster? Why?


# Traditional Insertion Sort
def insertionSort(arr):
    # begin from the 2nd element in the sequence
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # compare arr[i] to its left neighbour (arr[j])
        while j >= 0 and key < arr[j]:
            # if arr[i] is smaller, traverse backwards to find correct position to insert
            arr[j + 1] = arr[j]
            j -= 1
        
        # otherwise, do nothing
        # this line of code also ends up inserting the key at it's correct position after loop
        arr[j + 1] = key
        
# Binary Insertion Sort
def binaryInsertionSort(arr):
    # begin from the 2nd element in the sequence
    for i in range(1, len(arr)):
        key = arr[i]
        left = 0
        right = i - 1
        
        # use binary search to find insertion point for key
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
                
        # shift elements to the right to make room for key
        j = i
        while j > left:
            arr[j] = arr[j - 1]
            j -= 1
        
        # insert the key at it's correct position after loop
        arr[left] = key


# Testing each algorithm on a number of average-case inputs of increasing length
# Then plotting the results of both algorithms on the same plot, together with appropriate
# interpolating functions

import time
import random
import matplotlib.pyplot as plt

# function to measure execution time
def measureTime(sort_function, arr):
    startTime = time.time()
    sort_function(arr)
    return time.time() - startTime

# experiment parameters
sizes = [100, 500, 1000, 5000, 10000]  # input sizes to test
numTrials = 5  # number of trials per input size

# store results
insertionSortTimes = []
binaryInsertionSortTimes = []

# run the experiment
for size in sizes:
    insertionTime = 0
    binaryTime = 0

    for trial in range(numTrials):
        arr = [random.randint(1, 10000) for n in range(size)]  # generate random list
        
        # measure traditional insertion sort time
        insertionTime += measureTime(insertionSort, arr.copy())

        # measure binary insertion sort time
        binaryTime += measureTime(binaryInsertionSort, arr.copy())

    # store average times
    insertionSortTimes.append(insertionTime / numTrials)
    binaryInsertionSortTimes.append(binaryTime / numTrials)

# plot results
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertionSortTimes, marker='o', label='Traditional Insertion Sort')
plt.plot(sizes, binaryInsertionSortTimes, marker='s', label='Binary Insertion Sort')
plt.xlabel('Input Size (N)')
plt.ylabel('Execution Time (seconds)')
plt.title('Insertion Sort vs Binary Insertion Sort Performance')
plt.legend()
plt.grid(True)
plt.show()


# The Binary Insertion Sorting algorithm was faster. 
# This is due to binary search cutting the number of elements to be compared in half with each step, 
# leading to a logarithmic number of comparisons.