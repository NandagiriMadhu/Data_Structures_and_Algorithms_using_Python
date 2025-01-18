shoppingList = ['Milk', 'Cheese', 'Butter']
print('Milk' in shoppingList)
print('Orange' in shoppingList)

target = "Milk"
if target in shoppingList:
    print(f"{target} is in the list")
else: 
    print(f"{target} is not in the list")

target1 = "Bread"
if target1 in shoppingList:
    print(f"{target1} is in the list")
else: 
    print(f"{target1} is not in the list")

def searchElement(list, key):
    find = False
    for i in range(len(list)):
        if key == list[i]:
            find = True
            print(f"{key} found at index {i}")
    if not find:
        print(f"{key} is not found")

key1 = "Milk"
searchElement(shoppingList, key1)

key2 = "Milk1"
searchElement(shoppingList, key2)

def searchElement1(list1, key3):
    for i in range(len(list1)):
        if key3 == list1[i]:
            return f"{key3} found at index {i}"
    return f"{key3} is not found"

print(searchElement1(shoppingList, key1))

print(searchElement1(shoppingList, key2))

def searchElement2(list2, key4):
    for i in range(len(list2)):
        if key4 == list2[i]:
            print(f"{key4} found at index {i}")
            return 
    print(f"{key4} is not found") 

searchElement2(shoppingList, key1)
searchElement2(shoppingList, key2)

def searchElement3(list2, key5):
    for i, value in enumerate(list2):
        if value == key5:
            return i 
    return -1

print(searchElement3(shoppingList, key1))
print(searchElement3(shoppingList, key2))