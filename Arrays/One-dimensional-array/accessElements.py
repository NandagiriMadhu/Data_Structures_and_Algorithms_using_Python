import array

arr1 = array.array('i', [1,2,3,4,5,6])

def accessElementsIndex(array,index):
    if index >= len(array):
        print("No element at this index")
    else:
        print(array[index])

accessElementsIndex(arr1,3)
accessElementsIndex(arr1,6)
accessElementsIndex(arr1,200)
