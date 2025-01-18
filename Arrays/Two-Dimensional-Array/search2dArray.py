import numpy as np

arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

def searchElements(array, value):
    for i in range(len(array)):
        for j in range (len(array)):
            if array[i][j] == value:
                return "Element found at index ["+str(i)+"] ["+str(j)+"]"
    return "The element is not found"

print(searchElements(arr1, 7))
print(searchElements(arr1, 21))