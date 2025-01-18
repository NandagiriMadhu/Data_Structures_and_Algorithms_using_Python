import array

# List of strings to be converted to a byte array
stringList = ["Hello ", "Python ", "World"]

# Creating an empty byte array
byte_arr = array.array('B')  # 'B' denotes unsigned char (1 byte elements)

# Encoding each string in the list and extending the byte array
for s in stringList:
    byte_arr.extend(s.encode('utf-8'))  # Encoding each string to bytes and adding to the array
print(byte_arr)  # Prints the byte array

# Converting the byte array back to a string
recovered_string = byte_arr.tobytes().decode('utf-8')
print(recovered_string)  # Prints the recovered string

# Arrays of integers and floats
arr1 = array.array('i', [1, 2, 3, 4, 5, 6])  # Integer array
arr2 = array.array('d', [1.1, 2.2, 3.3, 4.4, 5.5, 6.6])  # Float array

# Function to traverse and print elements of an array
def traverseArray(array):
    for i in array:
        print(i)

# Traversing and printing elements of both arrays
traverseArray(arr1)  # Prints each element of arr1
traverseArray(arr2)  # Prints each element of arr2

# Function to search for an element in an array
def searchElements(arr1, key):
    found = False
    for i in range(len(arr1)):
        if arr1[i] == key:
            print(i)  # Prints the index of the found element
            found = True
    if not found:
        print("Element doesn't exist")  # Prints if element is not found

# Searching for the element 1 in arr1
searchElements(arr1, 1)  # Expected output: index 0 (the element '1' is at index 0)
