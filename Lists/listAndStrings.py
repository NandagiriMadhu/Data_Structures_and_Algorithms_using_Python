# Convert the string 'a' into a list of characters
a = 'Nanda'
b = list(a)  # The string 'Nanda' is converted to a list of characters
print(b)  # Output: ['N', 'a', 'n', 'd', 'a']

# Split the string 'c' based on a delimiter '-' and join them back with the same delimiter
c = 'Nanda-Madhu-Maddy'
delimiter = '-'  # Define the delimiter to split the string
d = c.split(delimiter)  # Split the string 'c' at each occurrence of the delimiter '-'
print(d)  # Output: ['Nanda', 'Madhu', 'Maddy']

# Join the list 'd' back into a string using the delimiter '-'
print(delimiter.join(d))  # Output: 'Nanda-Madhu-Maddy'
