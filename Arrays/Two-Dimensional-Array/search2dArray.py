import numpy as np

# Creating a 4x4 NumPy array and printing it
arr1 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13, 14, 15, 16]])
print(arr1)

# Function to search for an element in the 2D array
def searchElements(array, value):
    # Loop through the rows of the array
    for i in range(len(array)):
        # Loop through the columns of the array
        for j in range (len(array[i])):  # Fixed the error where len(array) was used instead of len(array[i])
            if array[i][j] == value:
                # If the value is found, return the index where it was found
                return "Element found at index ["+str(i)+"] ["+str(j)+"]"
    # If the element is not found, return a message
    return "The element is not found"

# Searching for the element 7 in the array
print(searchElements(arr1, 7))

# Searching for the element 21, which is not in the array
print(searchElements(arr1, 21))
