# Initializing the list
myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)  # Output: [1, 2, 3, 4, 5, 6, 7]

# Inserting 11 at the beginning (index 0) of the list
myList.insert(0, 11)
print(myList)  # Output: [11, 1, 2, 3, 4, 5, 6, 7]

# Inserting 55 at index 4
myList.insert(4, 55)
print(myList)  # Output: [11, 1, 2, 3, 55, 4, 5, 6, 7]

# Appending 66 to the end of the list
myList.append(66)
print(myList)  # Output: [11, 1, 2, 3, 55, 4, 5, 6, 7, 66]

# Creating a new list and extending it with the elements from myList
newList = []
newList.extend(myList)
print(newList)  # Output: [11, 1, 2, 3, 55, 4, 5, 6, 7, 66]
