# Function to remove duplicates from a list
def remove_duplicates(arr):
    unique_list = []  # A list to store unique elements
    for num in arr:
        if num not in unique_list:  # Check if the element is not already in the unique list
            unique_list.append(num)  # If not, add it to the unique list
    return unique_list

# Input: Number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Input: List elements
st = []
print("Enter the elements of the list:")
for i in range(n):
    b = int(input(f"Enter element {i + 1}: "))
    st.append(b)

# Call the function and print the result
print("List after removing duplicates:", remove_duplicates(st))
