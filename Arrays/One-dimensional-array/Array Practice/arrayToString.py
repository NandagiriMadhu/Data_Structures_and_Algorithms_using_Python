import array

# Creating an array of integers
arr1 = array.array('i', [1, 2, 3, 4, 5])

# Printing the array
print(arr1)

# Converting the array to string and extracting the elements inside the brackets
str_rep = str(arr1)[str(arr1).find("[")+1:str(arr1).find("]")]
print(str_rep)
