# Exercise 7
# Tasks:
# 1. Implement a standard binary search, with the following tweak: the 
#    midpoint for the first iteration must be configurable (all successive
#    iterations will just split the array in the middle)

# 2. Time the performance of each search task w/ different midpoints for each task. 
#    You can use whatever strategy you want to check different midpoints. 
#    Then, choose the best midpoint for each task

# 3. Produce a scatterplot visualizing each task and the corresponding
#    chosen midpoint

# 4. Comment on the graph. Does the choice of initial midpoint appear to affect performance? 
#    Why do you think that is?


# Binary Search Implementation
def binarySearch (arr, first, last, key, initialMid = None):
    # the midpoint for the first iteration must be configurable
    # (all successive iterations will just split the array in the middle
    if initialMid is not None:
        mid = initialMid
    else:
        mid = (first + last) // 2
        
    # validate search interval
    while first <= last:
        if key == arr[mid]:
            return mid  # key successfully found
        elif key < arr[mid]:
            # search the lower half if key is smaller than the midpoint value
            last = mid - 1
        else:
            # search the upper half if key is larger than the midpoint value
            first = mid + 1
            
        # calculate midpoint for successive iterations
        mid = (first + last) // 2
    
    # if loop ends, failed to find key
    return -1

# import necessary modules and gain access to provided .json files
import json
import time
import random
import matplotlib.pyplot as plt

# Load data from JSON files
with open('ex7data.json', 'r') as f:
    data = json.load(f)

with open('ex7tasks.json', 'r') as f:
    tasks = json.load(f)
    
# function to measure execution time of binary search with a given initial midpoint
def measureTime(arr, key, initialMid):
    startTime = time.time()
    binarySearch(arr, 0, len(arr) - 1, key, initialMid)
    return time.time() - startTime

# experiment to find the best initial midpoint for each task
bestMidpoints = []
executionTimes = []

# instead of testing ALL midpoints, we sample some to find a near-optimal one
sampleSize = 100  # instead of testing all 999,999 indices, test 100 random midpoints


for task in tasks:
    bestTime = float('inf')
    bestMid = 0

    # randomly sample midpoints instead of iterating through ALL
    for initialMid in random.sample(range(len(data)), min(sampleSize, len(data))):
        execTime = measureTime(data, task, initialMid)
        if execTime < bestTime:
            bestTime = execTime
            bestMid = initialMid
    
    bestMidpoints.append(bestMid)
    executionTimes.append(bestTime)

# Plot the results in scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(tasks, bestMidpoints, marker='o', label='Best Initial Midpoint')
plt.xlabel('Search Task (Key)')
plt.ylabel('Best Initial Midpoint')
plt.title('Best Initial Midpoint for Each Search Task')
plt.legend()
plt.grid(True)
plt.show()

# Does the choice of initial midpoint appear to affect performance?
# Yes but it seems dependent on the key being searched.
 
# Why do you think that is?
# The optimal midpoint is not going to be the same every time as the best initial
# midpoint varies based on what the key is. For example, always using the center as the midpoint
# won't be the fastest option for EVERY search task.