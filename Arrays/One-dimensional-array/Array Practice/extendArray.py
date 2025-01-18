import array

arr1 = array.array('i', [1,2,3,4,5])
arr2 = array.array('i', [6,7,8,9,10])

arr1.extend(arr2)
print(arr1)

for i in arr1:
    print(i)