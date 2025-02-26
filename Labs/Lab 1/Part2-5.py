import json #NOTICE no reversal here, only finding the timing of the changes in size fields, not reversing data!
import timeit

# Recursively find and update 'size' fields
def update_size_field(data):
    if type(data) == dict:  # Check if the data is a dictionary
        for key, value in data.items():
            if key == 'size':
                data[key] = 42  # Update 'size' field
            else:
                update_size_field(value)  # Recurse if it's a nested dictionary
    elif type(data) == list:  # If the data is a list
        for i in data:
            update_size_field(i)  # Recurse for each item in the list

# Load the data BUT without timing
with open('large-file.json', 'r') as file:
    data = json.load(file)

# Time the update_size_field function
def time_update():
    update_size_field(data)

# Run the timing 10 times and print the average time
timing = timeit.timeit('time_update()', globals=globals(), number=10)
average_time = timing / 10  # Calculate the average time over 10 repetitions

print(f'Average time to modify size field over 10 repetitions: {average_time:.6f} seconds')
