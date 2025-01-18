# Function to calculate the sum of diagonal elements in a 2D array
def diagonalSum(arr):
    total = 0  # Initialize the total sum to 0
    for i in range(len(arr)):  # Iterate over each row (index i)
        total += arr[i][i]  # Add the diagonal element (arr[i][i]) to the total
    return total  # Return the sum of diagonal elements

# Input number of rows (n) and columns (m)
n = int(input("Enter the number of rows (n): "))
m = int(input("Enter the number of columns (m): "))

# Initialize an empty list to store the 2D array
arr1 = []

# Input the elements of the 2D array row by row
for i in range(n):  
    row = []  # Initialize an empty list for the current row
    for j in range(m):  # Input each element in the row
        ele = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(ele)  # Add the element to the current row
    arr1.append(row)  # Add the row to the 2D array

# Call the diagonalSum function and print the result
print("Sum of diagonal elements:", diagonalSum(arr1))
