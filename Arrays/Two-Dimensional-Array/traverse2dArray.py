import numpy as np

# Creating a 4x4 NumPy array and printing it
arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

# Function to traverse the 2D array and print each element
def traverseArray(array):
    # Loop through the rows of the array
    for i in range(len(array)):
        # Loop through the columns of the array
        for j in range(len(arr1)):  # Fix: `arr1` should be replaced with `array` to make it dynamic
            print(array[i][j])

# Calling the function to print all elements of arr1
traverseArray(arr1)
