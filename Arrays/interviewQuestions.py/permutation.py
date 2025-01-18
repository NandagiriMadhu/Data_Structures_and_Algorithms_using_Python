# Function to check if two strings are permutations of each other
def permutation(str1, str2):
    # If the lengths are not equal, the strings cannot be permutations
    if len(str1) != len(str2):
        return False
    
    # Convert both strings to lists and sort them
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()  # Sort the characters in the first string
    list2.sort()  # Sort the characters in the second string

    # If the sorted lists are equal, the strings are permutations of each other
    if list1 == list2:
        return True
    else: 
        return False

# Input: Two strings to check
a = input("Enter first string: ")
b = input("Enter second string: ")

# Call the permutation function and print the result
print(permutation(a, b))
