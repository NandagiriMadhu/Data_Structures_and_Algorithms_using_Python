shoppingList = ['Milk', 'Cheese', 'Butter']

# Using a simple for loop to iterate through the list
for i in shoppingList:
    print(i)  # Output: Prints each item in the shoppingList: Milk, Cheese, Butter

# Using a for loop with the range function to access each index of the list
for i in range(len(shoppingList)):
    print(shoppingList[i])  # Output: Prints each item in the shoppingList again: Milk, Cheese, Butter

# Using a for loop to iterate through an empty list
empty = []
for i in empty:
    print("I am empty")  # This will not print anything because the list is empty
