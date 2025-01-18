# Initializing the list
myList = ['a', 'b', 'c', 'd', 'e', 'f']

# Removing the last element using pop()
myList.pop()
print(myList)  # Output: ['a', 'b', 'c', 'd', 'e']

# Removing the third last element (index -3) using pop()
myList.pop(-3)
print(myList)  # Output: ['a', 'b', 'd', 'e']

# Removing the element at index 1 using pop()
myList.pop(1)
print(myList)  # Output: ['a', 'd', 'e']

# Deleting the element at index 1 using del
del myList[1]
print(myList)  # Output: ['a', 'e']

# Deleting elements from index 0 to 1 (not inclusive of 2) using del
del myList[0:2]
print(myList)  # Output: []

# Extending the list with a new list
newList = [1, 2, 3, 4, 5, 6]
myList.extend(newList)
print(myList)  # Output: [1, 2, 3, 4, 5, 6]

# Removing the first occurrence of 4 from the list
myList.remove(4)
print(myList)  # Output: [1, 2, 3, 5, 6]
