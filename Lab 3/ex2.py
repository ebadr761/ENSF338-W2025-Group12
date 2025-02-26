import time
import random
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Create test cases for best,worst,average cases
def generate_best_case(size):
    return list(range(size))

def generate_worst_case(size):
    return list(range(size, 0, -1))

def generate_average_case(size):
    return random.choices(range(size), k=size)

# Timing Function(Mesasures exectution time of a function)
def time_function(func, arr):
    start_time = time.time()
    func(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Sizes to Test
sizes = [10,20,30,40,50,60,70,80,100,200,300,400,500,600,700,800,1000,2000,3000,5000]
results = [] # Store results

# Performance Measurement
for size in sizes:
    best_case = generate_best_case(size)
    worst_case = generate_worst_case(size)
    average_case = generate_average_case(size)

    # Only run Bubble Sort for small inputs(Program will take too long to compile for large inputs)
    if size <= 1000:
        bubble_best = time_function(bubble_sort, best_case)
        bubble_worst = time_function(bubble_sort, worst_case)
        bubble_avg = time_function(bubble_sort, average_case)
    else:
        bubble_best = None
        bubble_worst = None
        bubble_avg = None

    # Quicksort runs on all sizes
    quick_best = time_function(quicksort, best_case)
    quick_worst = time_function(quicksort, worst_case)
    quick_avg = time_function(quicksort, average_case)

    results.append((size, bubble_best, bubble_worst, bubble_avg, quick_best, quick_worst, quick_avg))

# Get the results for Plotting
sizes = [result[0] for result in results]

bubble_best_times = [result[1] for result in results]
bubble_worst_times = [result[2] for result in results]
bubble_avg_times = [result[3] for result in results]

quick_best_times = [result[4] for result in results]
quick_worst_times = [result[5] for result in results]
quick_avg_times = [result[6] for result in results]

# Plotting
def plot_performance(sizes, bubble_times, quick_times, title):
    plt.figure()
    
    # Filter None values for Bubble Sort(Errors wiil occour if None values are plotted)
    valid_sizes = np.array([sizes[i] for i in range(len(sizes)) if bubble_times[i] is not None])
    valid_bubble_times = np.array([bubble_times[i] for i in range(len(sizes)) if bubble_times[i] is not None])
    quick_times = np.array(quick_times)  # numpy array for easier calculations

    # Find the index where QuickSort first outperforms Bubble Sort
    threshold_index = np.argmax(valid_bubble_times > quick_times[:len(valid_sizes)])
    threshold_size = valid_sizes[threshold_index] if threshold_index > 0 else None

    # Plot performance curves
    plt.plot(valid_sizes, valid_bubble_times, label="Bubble Sort", marker='s', color='blue')
    plt.plot(sizes, quick_times, label="QuickSort", marker='o', color='green')


    # Threshold where QuickSort outperforms Bubble Sort
    if threshold_size:
        plt.axvline(x=threshold_size, color='r', linestyle='--', label=f"Threshold (n={threshold_size})")


    plt.xlabel("Size")
    plt.ylabel("Time (seconds)")
   
    plt.xscale("log")
    plt.yscale("log")
    
    # Threshold Line
    plt.axvline(x=1000, color='r', linestyle='--', label="Threshold (n=1000)")

    plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter()) # Decimal notation
    plt.gca().yaxis.set_major_formatter(ticker.ScalarFormatter()) # Decimal notation

    plt.title(title)
    plt.legend()
    plt.show()

# Best Case Plot
plot_performance(sizes, bubble_best_times, quick_best_times, "Best Case Performance")

# Worst Case Plot
plot_performance(sizes, bubble_worst_times, quick_worst_times, "Worst Case Performance")

# Average Case Plot
plot_performance(sizes, bubble_avg_times, quick_avg_times, "Average Case Performance")
