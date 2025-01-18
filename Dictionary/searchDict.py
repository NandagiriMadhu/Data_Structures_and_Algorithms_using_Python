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

# Function to search for a value in the dictionary and return the corresponding key
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:  # If the value is found in the dictionary
            return key, value    # Return the key and the value
    return "The Value doesn't exist"  # If the value is not found

# Input a value to search in the dictionary
e = input()
if e.isdigit():
    e = int(e)  # Convert the input value to an integer if it is a digit

# Call the searchDict function and print the result
print(searchDict(d, e))
