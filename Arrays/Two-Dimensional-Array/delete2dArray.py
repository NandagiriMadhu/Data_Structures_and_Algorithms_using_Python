import numpy as np

arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

arr1[2][3] = 22
print(arr1)
arr2 = np.delete(arr1, 0, axis = 0)
print(arr2)
arr2 = np.delete(arr1, 0, axis = 1)
print(arr2)
arr2 = np.delete(arr1, 2, axis = 0)
print(arr2)
arr2 = np.delete(arr1, 2, axis = 1)
print(arr2)
arr2 = np.delete(arr1, 3, axis = 0)
print(arr2)
arr2 = np.delete(arr1, 3, axis = 1)
print(arr2)