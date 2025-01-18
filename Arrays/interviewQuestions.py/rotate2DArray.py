# Function to rotate a matrix 90 degrees clockwise
def rotate(matrix):
    # Step 1: Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  # Swap elements across the diagonal

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()  # Reverse each row after transposition

    return matrix

# Input: Dimensions of the matrix (n x m)
n = int(input("Enter the number of rows (n): "))
m = int(input("Enter the number of columns (m): "))

# Input: Matrix elements
arr1 = []
print(f"Enter {n} rows and {m} columns of the matrix:")
for i in range(n):
    row = []
    for j in range(m):
        ele = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        row.append(ele)
    arr1.append(row)

# Check if the matrix is square (needed for a 90-degree rotation)
if n != m:
    print("Error: Only square matrices can be rotated 90 degrees.")
else:
    # Call the rotate function and print the rotated matrix
    print("Rotated matrix:")
    rotated_matrix = rotate(arr1)
    for row in rotated_matrix:
        print(row)
