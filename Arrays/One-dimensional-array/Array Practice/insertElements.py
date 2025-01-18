import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Inserting 0 at the beginning (index 0) of the array
arr1.insert(0, 0)
print(arr1)

# Inserting -2 at index 3 of the array
arr1.insert(3, -2)
print(arr1)

# Inserting 6 at index 7 of the array
arr1.insert(7, 6)
print(arr1)

# Attempting to insert 8 at index 71 (which is out of bounds)
arr1.insert(71, 8)
print(arr1)
