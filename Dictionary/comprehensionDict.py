import random

# Taking user input for the number of elements
a = int(input())

# Initialize an empty list to store the input strings
b = [] 
for i in range(1, a + 1):
    # Taking input for each element and appending it to the list
    c = input()
    b.append(c)

# Printing the list of inputs
print(b)

# Creating a dictionary where each key from the list `b` has a random value between 20 and 30
d = {i: random.randint(20, 30) for i in b}
print(d)

# Creating a new dictionary `e` that contains only the items from `d` where the value is greater than 25
e = {i: temp for (i, temp) in d.items() if temp > 25}
print(e)

# Printing the value associated with key '2' in the dictionary `d`
# Note: Ensure that '2' exists as a key in the input list, otherwise an error will occur.
print(d['2'])
