import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])

# Function to search for an element in the array
def searchElements(array, key):
    for i in range(len(array)):
        # If the element at index i matches the key, return the index
        if array[i] == key:
            return i
    # If the element is not found, return -1
    return -1

# Searching for the element 3 in the array
print(searchElements(arr1, 3))  # Expected output: 2 (index of 3 in the array)

# Searching for the element 10 in the array, which does not exist
print(searchElements(arr1, 10))  # Expected output: -1 (element not found)
