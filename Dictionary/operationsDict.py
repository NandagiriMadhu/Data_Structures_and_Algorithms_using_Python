# Input the number of key-value pairs to be added to the dictionary
a = int(input())  # Input for the number of key-value pairs

# Initialize an empty dictionary
d = {}

# Loop to take inputs and populate the dictionary
for i in range(1, a + 1):
    # Input key and value
    b = input()  # Key input
    c = input()  # Value input
    
    # If the value is a digit, convert it to an integer
    if c.isdigit():
        c = int(c)
    
    # If the key is a digit, convert it to an integer
    if b.isdigit():
        b = int(b)
    
    # Assign key-value pair to dictionary
    d[b] = c

# Print the original dictionary
print(d)

# Check if the key 'name' exists in the dictionary
print("name" in d)  # Returns True if 'name' is a key in the dictionary, otherwise False

# Check if the key 'name' does not exist in the dictionary
print("name" not in d)  # Returns True if 'name' is not a key in the dictionary, otherwise False

# Check if the value 23 exists in the dictionary values
print(23 in d.values())  # Returns True if 23 is a value in the dictionary, otherwise False

# Check if the value 23 does not exist in the dictionary values
print(23 not in d.values())  # Returns True if 23 is not a value in the dictionary, otherwise False

# Get the length of the dictionary (number of key-value pairs)
print(len(d))  # Returns the number of key-value pairs in the dictionary

# Check if all dictionary values are truthy
print(all(d))  # Returns True if all values in the dictionary are truthy, otherwise False

# Check if any dictionary value is truthy
print(any(d))  # Returns True if any value in the dictionary is truthy, otherwise False

# Print the sorted list of dictionary keys
print(sorted(d))  # Sorts and prints the keys of the dictionary
