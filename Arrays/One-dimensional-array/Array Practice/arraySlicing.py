import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Printing elements from index 1 to 2 (inclusive of 1, exclusive of 3)
print(arr1[1:3])

# Printing elements from index 1 to the end
print(arr1[1:])

# Printing elements from the start to index 2 (exclusive of 3)
print(arr1[:3])

# Printing the entire array
print(arr1[:])
