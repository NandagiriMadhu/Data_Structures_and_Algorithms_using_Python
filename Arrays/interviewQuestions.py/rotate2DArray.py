def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

n = int(input())
m = int(input())
arr1 = []
for i in range(n):
    row = []
    for j in range(m):
        ele = int(input())
        row.append(ele)
    arr1.append(row)

print(rotate(arr1))