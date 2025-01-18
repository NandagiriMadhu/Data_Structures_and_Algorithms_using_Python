import numpy as np

# Creating a 4x4 2D NumPy array
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(arr1)

# Function to access an element at a specific row and column index
def accessElements(array, r_index, c_index):
    if r_index >= len(array) or c_index >= len(array[0]):
        print("No Element Found")  # Checks if indices are out of bounds
    else:
        print(array[r_index][c_index])  # Accesses the element at the given indices
    
# Calling the function to access the element at row 3, column 1
accessElements(arr1, 3, 1)
