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

# List of records from JSON file to measure time it takes to process the given # of records
record_num = [1000, 2000, 5000, 10000]

# Store avg time for each record count
avg_times = []

# For each record count (we process the first n # records in the data)
for count in record_num:
    subset_data = data[:count]  # Process only the first n # of records

    times = [] # measure time for processing the size field update
    for _ in range(100):  # Repeat 100 times for each count to obtain avg
        # Time the update process using timeit
        tm = timeit.timeit(lambda: update_size_field(subset_data), number=1)
        times.append(tm)
    
    avg_time = sum(times) / len(times)  # Calculate avg time
    avg_times.append(avg_time)
    print(f"Average time for {count} records: {avg_time:.6f} seconds")

#  linear regression
slope, intercept = np.polyfit(record_num, avg_times, 1)

# Plot the data and the linear regression line
plt.rcParams['figure.figsize'] = [10, 5]
plt.scatter(record_num, avg_times, label='Average Time', color='blue')
line_values = [slope * x + intercept for x in record_num]
plt.plot(record_num, line_values, 'r', label=f'Linear fit: t = {slope:.2e} * n + {intercept:.2e}')
plt.xlabel("Number of Records")
plt.ylabel("Average Processing Time (seconds)")
plt.title("Processing Time vs Number of Records")
plt.legend()

# Save the plot to a file and print y=mx+b line
plt.savefig('output.3.2.png')
plt.show()
print(f"The linear model is: t = {slope:.2e} * n + {intercept:.2e}")
