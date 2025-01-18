import array

arr1 = array.array('i',[1,2,3,4,5])
for i in arr1:
    print(i)
arr1.append(6)
print(arr1)
for i in arr1:
    print(i)