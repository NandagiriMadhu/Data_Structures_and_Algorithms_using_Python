import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Iterating through the array and printing each element
for i in arr1:
    print(i)

# Appending a new element (6) to the array
arr1.append(6)

# Printing the updated array
print(arr1)

# Iterating through the updated array and printing each element
for i in arr1:
    print(i)
