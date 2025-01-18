import array

arr1 = array.array('i', [1,2,3,4,5])
tempList = [6,7,8,9,10]
arr1.fromlist(tempList)
print(arr1)

