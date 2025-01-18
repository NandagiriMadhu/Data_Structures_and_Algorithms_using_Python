# checking whether the given two strings are permuted 
def permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else: 
        return False
a = input()
b = input()
print(permutation(a, b))