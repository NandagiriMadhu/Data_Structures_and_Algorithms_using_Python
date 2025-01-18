# Define the shopping list
shoppingList = ['Milk', 'Cheese', 'Butter']

# Check if 'Milk' is in the shopping list
print('Milk' in shoppingList)  # True, as 'Milk' is in the list

# Check if 'Orange' is in the shopping list
print('Orange' in shoppingList)  # False, as 'Orange' is not in the list

# Search for an element in the shopping list using an if-else statement
target = "Milk"
if target in shoppingList:
    print(f"{target} is in the list")  # This will be printed
else: 
    print(f"{target} is not in the list")

# Another search with a different target item
target1 = "Bread"
if target1 in shoppingList:
    print(f"{target1} is in the list")
else: 
    print(f"{target1} is not in the list")  # This will be printed

# Function to search for an element in the list and print its index if found
def searchElement(list, key):
    find = False
    for i in range(len(list)):  # Iterate through the list
        if key == list[i]:
            find = True
            print(f"{key} found at index {i}")
    if not find:
        print(f"{key} is not found")

key1 = "Milk"
searchElement(shoppingList, key1)  # Function call to search for 'Milk'

key2 = "Milk1"
searchElement(shoppingList, key2)  # Function call to search for 'Milk1'

# Function to return a message about the search result instead of printing
def searchElement1(list1, key3):
    for i in range(len(list1)):  # Iterate through the list
        if key3 == list1[i]:
            return f"{key3} found at index {i}"  # Return the index if found
    return f"{key3} is not found"  # Return a message if not found

print(searchElement1(shoppingList, key1))  # Search for 'Milk' and print the result
print(searchElement1(shoppingList, key2))  # Search for 'Milk1' and print the result

# Another search function that prints the index directly
def searchElement2(list2, key4):
    for i in range(len(list2)):  # Iterate through the list
        if key4 == list2[i]:
            print(f"{key4} found at index {i}")  # Print the index if found
            return  # Exit the function once the element is found
    print(f"{key4} is not found")  # Print a message if not found

searchElement2(shoppingList, key1)  # Search for 'Milk'
searchElement2(shoppingList, key2)  # Search for 'Milk1'

# Using enumerate for a cleaner approach to search and return the index
def searchElement3(list2, key5):
    for i, value in enumerate(list2):  # Using enumerate to get index and value
        if value == key5:
            return i  # Return the index if found
    return -1  # Return -1 if not found

print(searchElement3(shoppingList, key1))  # Search for 'Milk' and print the index
print(searchElement3(shoppingList, key2))  # Search for 'Milk1' and print -1 (not found)