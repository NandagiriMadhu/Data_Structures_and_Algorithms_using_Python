import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# A Python list containing elements to be added to the array
tempList = [6, 7, 8, 9, 10]

# Using fromlist() to append elements from the list to the array
arr1.fromlist(tempList)

# Printing the updated array
print(arr1)