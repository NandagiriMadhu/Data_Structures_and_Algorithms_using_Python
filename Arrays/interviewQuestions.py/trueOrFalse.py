# Function to check if any element in the list is a duplicate
def contains_duplicate(nums):
    # Using a set to track seen elements
    seen = set()
    for num in nums:
        if num in seen:  # If the number is already in the set, it's a duplicate
            return "true"
        seen.add(num)  # Add the number to the set if it's not already seen
    return "false"  # No duplicates found

# Input: Number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Input: List elements
st = []
print("Enter the elements of the list:")
for i in range(n):
    b = int(input(f"Enter element {i + 1}: "))
    st.append(b)

# Call the function and print the result
print(contains_duplicate(st))
