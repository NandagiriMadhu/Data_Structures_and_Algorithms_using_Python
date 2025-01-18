# checking number is that present in the array
import numpy as np

def numberCheck(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return "found at index " +str(i)
    return -1

n = int(input())
arr1 = np.array([])
for i in range(n):
    b = int(input())
    arr1 = np.append(arr1, b)
a = int(input())

print(numberCheck(arr1, a))
