import json

# recursively find and update 'size' fields
def update_size_field(data):
    if type(data)==dict:  # Check if the data is a dictionary
        for key, value in data.items():
            if key == 'size':
                data[key] = 42  # Update 'size' field
            else:
                update_size_field(value)  # Recurse if it's a nested dictionary
    elif type(data)==list:  # If the data is a list
        for i in data:
            update_size_field(i)  # Recurse for each item in the list

#1. load JSON file
with open('large-file.json','r') as file:
    data = json.load(file)

#2. change size = 42 for all data
update_size_field(data)

#3. write modified data in reverse
with open('output.2.3.json', 'w') as output_file:
    json.dump(data[::-1], output_file, indent=4) # ::-1 reverses list using slicing
