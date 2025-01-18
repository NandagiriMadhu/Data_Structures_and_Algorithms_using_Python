import copy

n = int(input())
m = int(input())
arr1 = []
for i in range(n):
    row = []
    for j in range(m):
        ele = int(input())
        row.append(ele)
    arr1.append(row)
 
shallow_copied_list = copy.copy(arr1)

shallow_copied_list[0][0] = 100

print("Original List:", arr1) 
print("Shallow Copy:", shallow_copied_list) 

deep_copied_list = copy.deepcopy(shallow_copied_list)
deep_copied_list[0][1] = 100

print("Original List:", shallow_copied_list)  
print("Deep Copy:", deep_copied_list) 
