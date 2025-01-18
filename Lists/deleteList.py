myList = ['a', 'b', 'c', 'd', 'e', 'f']
myList.pop()
print(myList)
myList.pop(-3)
print(myList)
myList.pop(1)
print(myList)

del myList[1]
print(myList)
del myList[0:2]
print(myList)

newList = [1,2,3,4,5,6]
myList.extend(newList)
print(myList)

myList.remove(4)
print(myList)