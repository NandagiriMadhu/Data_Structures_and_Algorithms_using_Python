shoppingList = ['Milk', 'Cheese', 'Butter']  # Define a shopping list

print(shoppingList[0])  # Prints the first item in the list (Index 0: 'Milk')
print(shoppingList[2])  # Prints the third item in the list (Index 2: 'Butter')
print(shoppingList[-1])  # Prints the last item in the list (Index -1: 'Butter')

# The following lines will raise errors as the indices are out of range:
print(shoppingList[-4])  # Error: There is no item at index -4, as the list has only 3 items
print(shoppingList[4])   # Error: Index 4 is out of range since the list has only 3 items
