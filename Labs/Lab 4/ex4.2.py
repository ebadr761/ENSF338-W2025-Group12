#Now, consider the tasks of searching in a sorted array
#3. Provide the code for an inefficient implementation and an efficient implementation.
#   The inefficient implementation is a linear search that iterates through each element in the array until the target
#   value is found. The time complexity is O(n) because the worst-case scenario is when the target value is at the end
#   of the array or not present. The space complexity is O(1) because the function does not use any additional data
#   structures.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
#   The efficient implementation is a binary search that divides the array in half and compares the middle element to
#   the target value. If the middle element is equal to the target value, the function returns the index. Otherwise, it
#   recursively searches the left or right half of the array based on the comparison. The time complexity is O(log n)
#   because the search space is halved in each iteration. The space complexity is O(log n) due to the recursive calls.
def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)
    
#State the worst-case complexity of each implementation.
#4. The worst-case time complexity of linear search is O(n) because it iterates through each element in the array
#   until the target value is found or the end of the array is reached. The worst-case time complexity of binary search
#   is O(log n) because it divides the search space in half in each iteration, reducing the number of elements to search
#   exponentially.

#5. Provide the code for an experiment that demonstrates the difference. [0.1 pts] The experiment should: 1. Time the 
#   execution of both implementations on realistic, large inputs (1000 elements or above) 2. Plot the distribution of
#   measured values across multiple measurements (>= 100 measurements per task)
import random
import time
import matplotlib.pyplot as plt
# Generate a large sorted array
def generate_sorted_array(size):
    return sorted(random.sample(range(1, size * 10), size))

# Experiment to compare linear and binary search
def run_experiment(array_size, num_measurements):
    # Generate a sorted array
    arr = generate_sorted_array(array_size)
    target = random.choice(arr)  # Choose a random target from the array

    # Lists to store execution times
    linear_times = []
    binary_times = []

    # Measure execution times
    for _ in range(num_measurements):
        # Time linear search
        start_time = time.time_ns()
        linear_search(arr, target)
        end_time = time.time_ns()
        linear_times.append(end_time - start_time)

        # Time binary search
        start_time = time.time_ns()
        binary_search(arr, target, 0, len(arr) - 1)
        end_time = time.time_ns()
        binary_times.append(end_time - start_time)

    return linear_times, binary_times

# Plot the distribution of execution times
def plot_distributions(linear_times, binary_times):
    plt.figure(figsize=(10, 6))

    # Plot histogram for linear search
    plt.hist(linear_times, bins=50, alpha=0.5, label="Linear Search", color="blue")

    # Plot histogram for binary search
    plt.hist(binary_times, bins=50, alpha=0.5, label="Binary Search", color="red")

    plt.xlabel("Execution Time (ns)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Execution Times for Linear vs Binary Search")
    plt.legend()
    plt.grid(True)
    plt.show()

# Main function to run the experiment
if __name__ == "__main__":
    # Parameters
    array_size = 1000  # Size of the sorted array
    num_measurements = 100  # Number of measurements per algorithm

    # Run the experiment
    linear_times, binary_times = run_experiment(array_size, num_measurements)

    # Plot the results
    plot_distributions(linear_times, binary_times)