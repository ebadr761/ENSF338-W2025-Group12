import timeit

# Function to compute 2^n
def pow2(n):
    return 2 ** n

# Timing 10,000 instances of pow2(10000)
time_pow2 = timeit.timeit(lambda: pow2(10000), number=10000)
print(f"Time for pow2(10000) across 10,000 instances: {time_pow2:.6f} seconds")

# Function 1: pow2 using a for loop
def pow2_for_loop(n):
    result = 1
    for _ in range(n):
        result *= 2
    return result

# Function 2: pow2 using list comprehension
def pow2_list_comprehension(n):
    return [2 ** i for i in range(n)][-1]

# Timing 1,000 instances for both methods
time_for_loop = timeit.timeit(lambda: pow2_for_loop(1000), number=1000)
time_list_comprehension = timeit.timeit(lambda: pow2_list_comprehension(1000), number=1000)

print(f"Time for for loop across 1,000 instances: {time_for_loop:.6f} seconds")
print(f"Time for list comprehension across 1,000 instances: {time_list_comprehension:.6f} seconds")
