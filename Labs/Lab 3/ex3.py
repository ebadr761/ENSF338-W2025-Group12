import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap if out of order
                swaps += 1
    return comparisons, swaps

# random inputs of increasing size (want to show O(n²) output so use linearly increasing inputs)
sizes = [10, 20, 30, 40, 50, 60, 70]
comparisons_list = []
swaps_list = []

# Run bubble sort on each input size
for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]  # fill array with random inputs
    comparisons, swaps = bubble_sort(arr)
    comparisons_list.append(comparisons)
    swaps_list.append(swaps)

plt.figure(figsize=(12, 5))
# Comparisons Plot
plt.subplot(1, 2, 1)
plt.plot(sizes, comparisons_list, 'o-', label="Comparisons")
plt.plot(sizes, [0.5 * n * (n - 1) for n in sizes], '--', label="Expected Comparisons n(n-1)/2 -> O(n²)")
plt.xlabel("Input Size (n)")
plt.ylabel("# Comparisons")
plt.title("Comparisons vs. Input Size")
plt.legend()

# Swaps Plot
plt.subplot(1, 2, 2)
plt.plot(sizes, swaps_list, 's-', label="Swaps")
plt.plot(sizes, [0.25 * n * (n - 1) for n in sizes], '--', label="Expected Swaps n(n-1)/4 -> O(n²)")
plt.xlabel("Input Size (n)")
plt.ylabel("# Swaps")
plt.title("Swaps vs. Input Size")
plt.legend()

plt.tight_layout() # Make it all fit in one figure
plt.show()
