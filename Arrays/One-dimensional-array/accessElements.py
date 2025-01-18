import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])

# Function to access elements by index in the array
def accessElementsIndex(arr, index):
    # Check if the index is within the bounds of the array
    if index >= len(arr):
        print("No element at this index")  # Print a message if index is out of bounds
    else:
        print(arr[index])  # Print the element at the given index

# Test cases: Accessing elements at various indices
accessElementsIndex(arr1, 3)  # Valid index
accessElementsIndex(arr1, 6)  # Invalid index (out of bounds)
accessElementsIndex(arr1, 200)  # Invalid index (out of bounds)
