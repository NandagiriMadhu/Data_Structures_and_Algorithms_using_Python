import array

stringList = ["Hello ", "Python ", "World"]
byte_arr = array.array('B')

for s in stringList:
    byte_arr.extend(s.encode('utf-8'))
print(byte_arr)

recovered_string = byte_arr.tobytes().decode('utf-8')
print(recovered_string)

arr1 = array.array('i', [1,2,3,4,5,6])
arr2 = array.array('d', [1.1, 2.2, 3.3, 4.4, 5.5, 6.6])

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr1)
traverseArray(arr2)

def searchElements(arr1,key):
    found = False
    for i in range(len(arr1)):
        if arr1[i] == key:
            print(i)
            found = True
    if not found:
        print("Element doesn't exist")

searchElements(arr1,1)


