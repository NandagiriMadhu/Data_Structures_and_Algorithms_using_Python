# Initializing the list 'myList'
myList = [2, 4, 1, 7, 8, 3]

# Creating a copy of the original list 'myList' to preserve its order
orig = myList[:]  # Copy of 'myList' (shallow copy)

# Sorting 'myList' in-place
myList.sort()  # Sort the list 'myList' in ascending order
print(orig)  # Print the original list (unchanged)
print(myList)  # Print the sorted list (in-place modification)

# Another example where 'myList2' is sorted and stored in a new variable 'my'
myList2 = [3, 1, 6, 2, 9, 4, 0]

# Using the 'sorted()' function to sort 'myList2' and store the result in 'my'
my = sorted(myList2)  # Returns a new list with elements sorted
print(my)  # Print the new sorted list (the original list 'myList2' remains unchanged)
