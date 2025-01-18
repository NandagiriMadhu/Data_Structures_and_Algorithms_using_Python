import numpy as np

arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(arr1)):
            print(array[i][j])

traverseArray(arr1)