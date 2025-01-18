import numpy as np

arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

def accessElements(array, r_index, c_index):
    if r_index >= len(array) or c_index >=len(array):
        print("No Element Found")
    else:
        print(array[r_index][c_index])
    
accessElements(arr1, 3, 1)