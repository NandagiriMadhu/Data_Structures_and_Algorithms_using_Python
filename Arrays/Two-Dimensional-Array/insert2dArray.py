import numpy as np

# Creating a 4x4 NumPy array and printing it
arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

# Inserting a new column at index 0 (axis=1) with values [-3,-2,-1,0]
arr2 = np.insert(arr1, 0, [[-3,-2,-1,0]], axis = 1)
print(arr2)

# Inserting a new row at index 0 (axis=0) with values [-3,-2,-1,0]
arr2 = np.insert(arr1, 0, [[-3,-2,-1,0]], axis = 0)
print(arr2)

# Inserting a new column at index 2 (axis=1) with values [-3,-2,-1,0]
arr2 = np.insert(arr1, 2, [[-3,-2,-1,0]], axis = 1)
print(arr2)

# Inserting a new row at index 2 (axis=0) with values [-3,-2,-1,0]
arr2 = np.insert(arr1, 2, [[-3,-2,-1,0]], axis = 0)
print(arr2)

# Inserting a new column at index 4 (axis=1) with values [-3,-2,-1,0]
arr2 = np.insert(arr1, 4, [[-3,-2,-1,0]], axis = 1)
print(arr2)

# Inserting a new row at index 4 (axis=0) with values [-3,-2,-1,0]
arr2 = np.insert(arr1, 4, [[-3,-2,-1,0]], axis = 0)
print(arr2)

# Appending a new column with values [-3,-2,-1,0] at the end (axis=1)
arr2 = np.append(arr1, [[-3],[-2],[-1],[0]], axis = 1)
print(arr2)
