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

# Uncomment these lines to test different deletion methods:

# e = input()  # Input a key to delete
# del d[e]  # Deletes the key-value pair with the specified key
# d.pop(e)  # Removes the key-value pair with the specified key
# d.pop(e, None)  # Removes the key-value pair with the specified key, returns None if the key is not found
# d.popitem()  # Removes and returns an arbitrary key-value pair (last inserted item in Python 3.7+)

# Clear the entire dictionary
d.clear()
print(d)  # Prints an empty dictionary after clearing
