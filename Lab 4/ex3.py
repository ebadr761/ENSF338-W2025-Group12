#Exercise 3: More Dynamic Arrays

#1. Identify and explain the strategy used to grow arrays when full, with references to specific lines of code in the file above. What is the growth factor?
#ANS: 
#   The list (dynamic array) reaches its capacity, it must resize to accommodate new elements. This is done by
#   creating a new array with a larger capacity, copying the elements from the old array to the new array, and
#   freeing the memory of the old array. The growth factor is calculated by the expression:
#   new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
#   The new_allocated variable is the new size of the list, which is calculated by adding the current
#   size of the list with the current size of the list right shifted by 3 bits, then adding 6 to the result. The
#   result is then bitwise ANDed with the complement of 3. This calculation is done to ensure that the new size
#   is a multiple of 4, to help with memory alignment since bytes are multiples of 4 bits.

#   So the main idea is to create space for the new element by increasing capacity if full, 
#   this strategy balances memory efficiency and performance, ensuring amortized O(1) time for appends.

#2. Produce test code that checks the correctness of your inference for lists up to 64 elements. 
#   Specifically, write a Python loop that grows a list from 0 to 63 integers, printing out a message
#   when the underlying capacity of the list changes.
import sys

lst = []
prev_size = sys.getsizeof(lst)
S = 0 # placeholder for the largest size before growth

for i in range(64):
    lst.append(i)
    new_size = sys.getsizeof(lst)
    if new_size != prev_size:
        print(f"Size changed at {i} elements: {prev_size} → {new_size}")
        prev_size = new_size
        S = i
print(f"Using S = {S} for timing measurements.")

#3. Measure the time it takes to grow the array from size S to S+1 (i.e., start from an array of size S and append one element). Repeat the measure 1,000 times
import time
times_S_plus_1 = []
lst = list(range(S))  # Start with size S
for _ in range(1000):
    start = time.perf_counter()
    lst.append(0)
    end = time.perf_counter()
    lst.pop()  # Reset to size S
    times_S_plus_1.append(end - start)

print(f"Average time from {S} to {S+1}: {sum(times_S_plus_1) / len(times_S_plus_1):.9f} sec")

#4. Measure the time it takes to grow the array from size S-1 to S. Repeat the measure 1,000 times
times_S = []
lst.pop()  # Reduce to S-1
for _ in range(1000):
    start = time.perf_counter()
    lst.append(0)
    end = time.perf_counter()
    lst.pop()  # Reset to size S-1
    times_S.append(end - start)

print(f"Average time from {S-1} to {S}: {sum(times_S) / len(times_S):.9f} sec")

#5. Plot the distribution of both measurements (you can use hist or similar). Do you see any difference? Why?
import matplotlib.pyplot as plt

plt.hist(times_S_plus_1, bins=30, alpha=0.7, label="S → S+1")
plt.hist(times_S, bins=30, alpha=0.7, label="S-1 → S")
plt.legend()
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.title("Time Distribution for List Growth")
plt.show()
