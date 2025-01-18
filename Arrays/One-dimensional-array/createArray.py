import array

# Creating an empty array using the array module
my_array = array.array('i')  # 'i' denotes integers
print(my_array)  # Prints: array('i') (an empty array)

# Creating an array with predefined elements using the array module
my_array1 = array.array('i', [1, 2, 3, 4, 5])  # A simple array of integers
print(my_array1)  # Prints: array('i', [1, 2, 3, 4, 5])

# Importing NumPy to work with arrays
import numpy as np

# Creating an empty NumPy array
np_array = np.array([], dtype=int)  # dtype specifies that the array holds integers
print(np_array)  # Prints: []

# Creating a NumPy array with predefined elements
np_array1 = np.array([1, 2, 3, 4, 5], dtype=int)  # A simple NumPy array of integers
print(np_array1)  # Prints: [1 2 3 4 5]
