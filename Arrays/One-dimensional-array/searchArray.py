import array

arr1 = array.array('i', [1,2,3,4,5,6])

def searchElements(array,key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1

print(searchElements(arr1, 3))
print(searchElements(arr1, 10))

