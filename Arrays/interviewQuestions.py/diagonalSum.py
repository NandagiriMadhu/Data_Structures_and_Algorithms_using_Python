# Calculate the sum of diagonal elements in 2D Array
def diagonalSum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i][i]
    return total

n = int(input())
m = int(input())
arr1 = []
for i in range(n):
    row = []
    for j in range(m):
        ele = int(input())
        row.append(ele)
    arr1.append(row)

print(diagonalSum(arr1))
