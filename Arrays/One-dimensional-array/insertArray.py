import array

# Creating an empty array using the array module
my_array = array.array('i')  # 'i' denotes integers
print(my_array)  # Prints: array('i') (an empty array)

# Creating an array with predefined elements using the array module
my_array1 = array.array('i', [1, 2, 3, 4, 5])  # Array of integers
print(my_array1)  # Prints: array('i', [1, 2, 3, 4, 5])

# Inserting the value 6 at index 0 (beginning of the array)
my_array1.insert(0, 6)  
print(my_array1)  # Prints: array('i', [6, 1, 2, 3, 4, 5])

# Inserting the value 7 at index 3
my_array1.insert(3, 7)  
print(my_array1)  # Prints: array('i', [6, 1, 2, 7, 3, 4, 5])

# Inserting the value 8 at index 7 (which is the end of the array)
my_array1.insert(7, 8)  
print(my_array1)  # Prints: array('i', [6, 1, 2, 7, 3, 4, 5, 8])

# Working with NumPy arrays
import numpy as np

# Creating an empty NumPy array
np_array = np.array([], dtype=int)  # Empty array
print(np_array)  # Prints: []

# Creating a NumPy array with predefined elements
np_array1 = np.array([1, 2, 3, 4, 5], dtype=int)  # NumPy array of integers
print(np_array1)  # Prints: [1 2 3 4 5]

# Inserting the value 6 at index 0 in the NumPy array
np_array1 = np.insert(np_array1, 0, 6)  
print(np_array1)  # Prints: [6 1 2 3 4 5]

# Inserting the value 7 at index 3 in the NumPy array
np_array1 = np.insert(np_array1, 3, 7)  
print(np_array1)  # Prints: [6 1 2 7 3 4 5]

# Inserting the value 8 at index 7 in the NumPy array
np_array1 = np.insert(np_array1, 7, 8)  
print(np_array1)  # Prints: [6 1 2 7 3 4 5 8]
