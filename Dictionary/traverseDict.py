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

# Function to traverse the dictionary and print each key-value pair
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])  # Print each key and its corresponding value

# Call the traverseDict function to print key-value pairs from the dictionary
traverseDict(d)
