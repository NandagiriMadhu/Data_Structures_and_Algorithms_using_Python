import numpy as np

# Creating a 4x4 NumPy array with integers and printing it
arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

# Changing the element at row index 2 and column index 3 to 22
arr1[2][3] = 22
print(arr1)

# Deleting the first row (axis=0) of the array
arr2 = np.delete(arr1, 0, axis = 0)
print(arr2)

# Deleting the first column (axis=1) of the array
arr2 = np.delete(arr1, 0, axis = 1)
print(arr2)

# Deleting the third row (index 2) of the array
arr2 = np.delete(arr1, 2, axis = 0)
print(arr2)

# Deleting the third column (index 2) of the array
arr2 = np.delete(arr1, 2, axis = 1)
print(arr2)

# Deleting the fourth row (index 3) of the array
arr2 = np.delete(arr1, 3, axis = 0)
print(arr2)

# Deleting the fourth column (index 3) of the array
arr2 = np.delete(arr1, 3, axis = 1)
print(arr2)
