import numpy as np

arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

arr2 = np.insert(arr1, 0, [[-3,-2,-1,0]], axis = 1)
print(arr2)
arr2 = np.insert(arr1, 0, [[-3,-2,-1,0]], axis = 0)
print(arr2)
arr2 = np.insert(arr1, 2, [[-3,-2,-1,0]], axis = 1)
print(arr2)
arr2 = np.insert(arr1, 2, [[-3,-2,-1,0]], axis = 0)
print(arr2)
arr2 = np.insert(arr1, 4, [[-3,-2,-1,0]], axis = 1)
print(arr2)
arr2 = np.insert(arr1, 4, [[-3,-2,-1,0]], axis = 0)
print(arr2)
arr2 = np.append(arr1, [[-3],[-2],[-1],[0]], axis = 1)
print(arr2)