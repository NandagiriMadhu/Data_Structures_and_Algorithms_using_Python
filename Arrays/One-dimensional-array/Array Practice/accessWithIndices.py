import array

arr1 = array.array('i',[1,2,3,4,5])

def accessWithIndex(array):
    for index in range(len(array)):
        print(index, arr1[index])

accessWithIndex(arr1)