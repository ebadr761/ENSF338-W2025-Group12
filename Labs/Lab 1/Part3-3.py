import json
import random
import timeit
from matplotlib import pyplot as plt
import numpy as np

def update_size_field(data):
    if type(data) == dict:  # Check if the data is a dictionary
        for key, value in data.items():
            if key == 'size':
                data[key] = 42  # Update 'size' field
            else:
                update_size_field(value)  # Again if it's a nested dictionary
    elif type(data) == list:  # OR the data is a list
        for i in data:
            update_size_field(i)  # Recurse for each item in the list

with open('large-file.json', 'r') as file:
    data = json.load(file)

# Select the first 1000 records
subset_data = data[:1000]

# Measure the time it takes to process the first 1000 records 1000 times
repeat_times = timeit.repeat(lambda: update_size_field(subset_data), number=1, repeat=1000)

# Plot the histogram of the measured times
plt.rcParams['figure.figsize'] = [10, 6]
plt.hist(repeat_times, bins=30, color='blue', edgecolor='black', alpha=0.7)

plt.xlabel('Processing Time (seconds)')
plt.ylabel('Frequency')
plt.title('Histogram of Processing Times for 1000 Records')
plt.grid(True)

# Save the histogram plot to a PNG file
plt.savefig('output.3.3.png')
plt.show()
