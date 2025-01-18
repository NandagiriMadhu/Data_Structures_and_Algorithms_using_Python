import array

# Creating two arrays of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])
arr2 = array.array('i', [6, 7, 8, 9, 10])

# Extending arr1 by appending all elements from arr2
arr1.extend(arr2)
print(arr1)

# Iterating through each element in the extended arr1 and printing it
for i in arr1:
    print(i)
