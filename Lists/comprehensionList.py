# Initializing prev_list with values [1, 2, 3, 4]
prev_list = [1, 2, 3, 4]

# Creating a new list where each element of prev_list is multiplied by 2
new_list = [i*2 for i in prev_list]
print(prev_list)  # Output: [1, 2, 3, 4]
print(new_list)   # Output: [2, 4, 6, 8]

# Defining a string "Python"
lan = "Python"

# Creating a list where each character of the string is added as a separate element
list = [letter for letter in lan]
print(lan)        # Output: Python
print(list)       # Output: ['P', 'y', 't', 'h', 'o', 'n']

# Creating a list of numbers from 1 to 9 (inclusive) using range()
list1 = [number for number in range(1, 10)]
print(list1)      # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initializing a tuple
tup = (1, 2, 3, 4, 5)

# Converting the elements of the tuple into a new tuple using a generator expression
tup2 = tuple(i for i in tup)
print(tup2)       # Output: (1, 2, 3, 4, 5)
