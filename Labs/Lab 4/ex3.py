#Exercise 3: More Dynamic Arrays

#1. Identify and explain the strategy used to grow arrays when full, with references to specific lines of code in the file above. What is the growth factor?
#ANS: When the size of the array reaches it's capacity, the array is copied to a new array with a growth factor.
#   The list grows using a growth factor of approximately 1.125x (12.5%). When the list is full, the new size
#   is calculated as newsize >> 3 adds 12.5% of the current size and + 6 ensures small lists grow enough with
#   ~(size_t)3 rounding up to the nearest multiple of 4 for alignment. 
#   This strategy balances memory efficiency and performance, ensuring amortized O(1) time for appends.

#2. Produce test code that checks the correctness of your inference for lists up to 64 elements. 
#   Specifically, write a Python loop that grows a list from 0 to 63 integers, printing out a message
#   when the underlying capacity of the list changes.

#3. Measure the time it takes to grow the array from size S to S+1 (i.e., start from an array of size S and append one element). Repeat the measure 1,000 times
import sys
import time
import matplotlib.pyplot as plt

def get_list_capacity(lst):
    overhead = sys.getsizeof([])  # Size of an empty list
    element_size = sys.getsizeof(0)  # Size of an integer
    return (sys.getsizeof(lst) - overhead) // element_size

def find_capacity_changes():
    lst = []
    prev_capacity = get_list_capacity(lst)
    capacity_changes = []

    for i in range(64):
        lst.append(i)
        current_capacity = get_list_capacity(lst)
        if current_capacity != prev_capacity:
            capacity_changes.append((len(lst), prev_capacity, current_capacity))
            prev_capacity = current_capacity

    return capacity_changes

def measure_growth_time(S, num_measurements=1000):
    # Measure time to grow from S-1 to S
    lst_S_minus_1 = list(range(S - 1))
    times_S_minus_1_to_S = []

    for _ in range(num_measurements):
        start_time = time.time_ns()
        lst_S_minus_1.append(S - 1)  # Append one element
        end_time = time.time_ns()
        times_S_minus_1_to_S.append(end_time - start_time)
        lst_S_minus_1.pop()  # Reset the list to size S-1

    # Measure time to grow from S to S+1
    lst_S = list(range(S))
    times_S_to_S_plus_1 = []

    for _ in range(num_measurements):
        start_time = time.time_ns()
        lst_S.append(S)  # Append one element
        end_time = time.time_ns()
        times_S_to_S_plus_1.append(end_time - start_time)
        lst_S.pop()  # Reset the list to size S

    return times_S_minus_1_to_S, times_S_to_S_plus_1

def plot_distributions(times_S_minus_1_to_S, times_S_to_S_plus_1):
    plt.figure(figsize=(10, 6))

    # Plot histogram for S-1 to S
    plt.hist(times_S_minus_1_to_S, bins=50, alpha=0.5, label="S-1 to S", color="blue")

    # Plot histogram for S to S+1
    plt.hist(times_S_to_S_plus_1, bins=50, alpha=0.5, label="S to S+1", color="red")

    plt.xlabel("Time (ns)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Time to Grow List")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Find the capacity changes
    capacity_changes = find_capacity_changes()
    S = capacity_changes[-1][0]  # Largest size S causing expansion
    print(f"Largest size S causing expansion: {S}")

    # Measure growth times
    times_S_minus_1_to_S, times_S_to_S_plus_1 = measure_growth_time(S)

    # Plot distributions
    plot_distributions(times_S_minus_1_to_S, times_S_to_S_plus_1)
#4. Measure the time it takes to grow the array from size S-1 to S. Repeat the measure 1,000 times
#5. Plot the distribution of both measurements (you can use hist or similar). Do you see any difference? Why?