import numpy as np  # Importing the NumPy library for array operations

# Function to check if a number is present in the array
def numberCheck(arr, key):
    # Iterate through the array to find the key
    for i in range(len(arr)):
        if arr[i] == key:  # If the number matches the key
            return "Found at index " + str(i)  # Return the index where it's found
    return -1  # Return -1 if the key is not found in the array

# Input: Number of elements in the array
n = int(input("Enter the number of elements in the array: "))

# Initialize an empty NumPy array
arr1 = np.array([])

# Input: Elements of the array
print("Enter the elements of the array:")
for i in range(n):
    b = int(input(f"Enter element {i + 1}: "))
    arr1 = np.append(arr1, b)  # Append the element to the NumPy array

# Input: Number to check
a = int(input("Enter the number to check: "))

# Call the function and print the result
result = numberCheck(arr1, a)
if result != -1:
    print(result)
else:
    print("Number not found in the array.")
