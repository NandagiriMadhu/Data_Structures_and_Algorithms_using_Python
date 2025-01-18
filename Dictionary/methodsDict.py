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

# Print dictionary items (key-value pairs)
print(d.items())

# Print the dictionary keys
print(d.keys())

# Print the dictionary values
print(d.values())

# Define another dictionary
g = {"a": 1, "b": 2}

# Update the original dictionary with the contents of 'g'
d.update(g)
print(d)

# Using 'get' to fetch a value by key with a default value
print(d.get('age', 28))  # Key 'age' does not exist, returns 28
print(d.get("or", 23))  # Key 'or' does not exist, returns 23
print(d.get("city"))  # Key 'city' does not exist, returns None (no default)

# Pop a random item from the dictionary and print it
print(d.popitem())  # Removes and returns a key-value pair

# Print the dictionary after popitem
print(d)

# Set default value for a key if it doesn't exist
print(d.setdefault("age", 25))  # If 'age' doesn't exist, it sets to 25, else returns current value
print(d.setdefault("name1", "added"))  # Adds 'name1' with value 'added' if it doesn't exist

# Try to pop a key that doesn't exist and return the default
print(d.pop("name2", "not"))  # 'name2' doesn't exist, so returns 'not'

# Print the dictionary after pop
print(d)

# Create a new dictionary with keys from a list and default value of 0
e = {}.fromkeys([1, 2, 3, 4], 0)
print(e)

# Create a new dictionary with keys from a list and default value of None
f = {}.fromkeys([1, 2, 3, 4])
print(f)
