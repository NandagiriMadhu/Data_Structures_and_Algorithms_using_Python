import copy

# Input the dimensions of the 2D array (n x m)
n = int(input())
m = int(input())
arr1 = []
# Constructing the 2D array
for i in range(n):
    row = []
    for j in range(m):
        ele = int(input())
        row.append(ele)
    arr1.append(row)

# Shallow copy of arr1
shallow_copied_list = copy.copy(arr1)

# Modify an element in the shallow copy
shallow_copied_list[0][0] = 100

# Display original and shallow copied lists
print("Original List:", arr1) 
print("Shallow Copy:", shallow_copied_list) 

# Deep copy of the shallow copy
deep_copied_list = copy.deepcopy(shallow_copied_list)

# Modify an element in the deep copy
deep_copied_list[0][1] = 100

# Display the shallow copy and deep copy after modification
print("Original List:", shallow_copied_list)  
print("Deep Copy:", deep_copied_list) 
