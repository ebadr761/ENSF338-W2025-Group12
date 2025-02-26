
import timeit
import matplotlib.pyplot as plt

#1. This code recursively finds the Fibonacci Sequence for n number of indexes. 
#2. No, this isn't an example of a divide and conquer algorithm since divide and conquer algorithms split a 
#   problem into smalller INDEPENDENT problems, which this does not do since func(n-1) and func(n-2) are computed
#   by returning n from the base case and it builds upon that, making it a DEPENDENT problem.
#3. O(2^n) because each call branches into two subproblems, forming an exponential recursion tree.
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
    
#4. Implementing memoization to the function above
#5. The time complexity for this new optimized algorithm is O(n)
def func_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = func_memoized(n-1, memo) + func_memoized(n-2, memo)
    return memo[n]

#6. Timing the time to run the function before and after memoizing
print("Time measurement and plots saved as ex1.6.1.jpg and ex1.6.2.jpg")
time_original = []
time_memoized = []
n_values = list(range(36))

for n in n_values:
    start = timeit.default_timer()
    func(n)
    time_original.append(timeit.default_timer()-start)
    
    start = timeit.default_timer()
    func_memoized(n)
    time_memoized.append(timeit.default_timer()-start)
    
# original function
plt.figure(figsize=(8, 5))
plt.plot(n_values, time_original, marker='o', linestyle='-', color='red', label="Original")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Execution Time of Original Fibonacci Function")
plt.legend()
plt.grid()
plt.savefig("ex1.6.1.jpg")

# memoized function
plt.figure(figsize=(8, 5))
plt.plot(n_values, time_memoized, marker='o', linestyle='-', color='blue', label="Memoized")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Execution Time of Memoized Fibonacci Function")
plt.legend()
plt.grid()
plt.savefig("ex1.6.2.jpg")