# Function to remove the first and last elements of the list
def removeEle(lst):
    # Return a new list excluding the first and last elements
    return lst[1:-1]

# Input: Number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Input: Elements of the list
st = []
print("Enter the elements of the list:")
for i in range(n):
    b = int(input(f"Enter element {i + 1}: "))
    st.append(b)

# Call the function and print the modified list
print("List after removing first and last elements:", removeEle(st))
