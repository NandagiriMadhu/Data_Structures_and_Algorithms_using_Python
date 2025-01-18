# Function to find pairs with a sum equal to the target
def findPairs(nums, tar):
    pairs = []  # List to store the pairs
    count = 0  # Counter for the number of valid pairs

    # Iterate over all pairs of numbers in the list
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):  # Ensure each pair is unique (i < j)
            if nums[i] == nums[j]:  # Skip if the numbers are equal
                continue
            elif nums[i] + nums[j] == tar:  # Check if the pair sums to the target
                count += 1
                pairs.append(f"{nums[i]}+{nums[j]}")  # Add the pair to the list

    # Print the pairs and return the count
    print("Pairs:", pairs)
    return count

# Input: number of elements in the list and the target sum
n = int(input("Enter the number of elements in the list: "))
a = int(input("Enter the target sum: "))

# Input: elements of the list
st = []
for i in range(n):
    b = int(input(f"Enter element {i+1}: "))
    st.append(b)

# Call the function and print the result
print("Number of pairs:", findPairs(st, a))
