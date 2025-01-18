import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Function to access array elements by index and print them along with their index
def accessWithIndex(array):
    for index in range(len(array)):
        print(index, array[index])  # Prints the index and corresponding element

# Calling the function with arr1 as the argument
accessWithIndex(arr1)
