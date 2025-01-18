import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])

# Removing the first occurrence of the element '3' from the array
arr1.remove(3)

# Printing the modified array
print(arr1)  # Expected output: array('i', [1, 2, 4, 5, 6])
