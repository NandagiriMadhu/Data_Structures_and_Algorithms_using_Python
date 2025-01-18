import numpy as np

# Creating a numpy array and a list with the same elements
myArray = np.array([1, 2, 3, 4, 5, 6])  # Numpy array
myList = [1, 2, 3, 4, 5, 6]  # Regular Python list

# Dividing each element of the numpy array by 2
print(myArray / 2)  # Numpy arrays allow element-wise operations, so each element is divided by 2

# The following line will raise an error because division cannot be applied element-wise to a regular Python list
print(myList / 2)  # This will raise a TypeError: unsupported operand type(s) for /: 'list' and 'int'


# Creating arrays with mixed types (integers and a string)
myArray1 = np.array([1, 2, 3, 4, 5, 6, 'a'])  # Numpy array with mixed types
myList1 = [1, 2, 3, 4, 5, 6, 'a']  # Regular Python list with mixed types

print(myArray1)  # Numpy arrays with mixed types will convert all elements to a common type (string here)
print(myList1)  # The list will retain the mixed types (integers and a string)
