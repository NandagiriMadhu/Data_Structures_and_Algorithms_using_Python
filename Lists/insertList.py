myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(0,11)
print(myList)
myList.insert(4,55)
print(myList)

myList.append(66)
print(myList)

newList = []
newList.extend(myList)
print(newList)