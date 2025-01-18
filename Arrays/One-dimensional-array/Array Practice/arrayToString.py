import array

arr1 = array.array('i', [1,2,3,4,5])
print(arr1)
str_rep = str(arr1)[str(arr1).find("[")+1:str(arr1).find("]")]
print(str_rep)
