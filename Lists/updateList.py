myList = [1,2,3,4,5,6,7]
print(myList)  # Output: [1, 2, 3, 4, 5, 6, 7]

# Updating the element at index 2 (which is '3') to 33
myList[2] = 33
print(myList)  # Output: [1, 2, 33, 4, 5, 6, 7]

# Replacing the first two elements ([1, 2]) with ['x', 'y']
myList[0:2] = ['x', 'y']
print(myList)  # Output: ['x', 'y', 33, 4, 5, 6, 7]
