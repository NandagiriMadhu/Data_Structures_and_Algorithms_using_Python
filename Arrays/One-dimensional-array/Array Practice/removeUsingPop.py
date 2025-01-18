import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Printing the original array
print(arr1)

# Using pop() to remove the last element (5) from the array
arr1.pop()

# Printing the updated array after the last element is removed
print(arr1)
