import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Printing the entire array
print(arr1)  # Output: array('i', [1, 2, 3, 4, 5])

# Finding the index of the element 5
print(arr1.index(5))  # Output: 4 (The index of 5 in the array)
