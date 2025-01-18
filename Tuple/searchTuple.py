# Define a tuple with elements 'a', 'b', 'c', 'd', 'e'
tup = ('a', 'b', 'c', 'd', 'e')

# Check if the element 'a' is present in the tuple and print the result (True or False)
print('a' in tup)  # Output: True

# Check if the element 'f' is present in the tuple and print the result (True or False)
print('f' in tup)  # Output: False

# Find and print the index of the element 'b' in the tuple
print(tup.index('b'))  # Output: 1 (the index of 'b' in the tuple)

# Define a function to search for an element in a tuple and return its index, or -1 if not found
def searchTuple(tup1, element):
    # Iterate through the tuple by index
    for i in range(len(tup1)):
        # If the element matches the current tuple item, return its index
        if tup1[i] == element:
            return i
    # If the element is not found, return -1
    return -1

# Call the searchTuple function to search for 'c' in the tuple and print the result
print(searchTuple(tup, 'c'))  # Output: 2 (the index of 'c' in the tuple)

# Call the searchTuple function to search for 'h' in the tuple and print the result
print(searchTuple(tup, 'h'))  # Output: -1 (because 'h' is not in the tuple)
