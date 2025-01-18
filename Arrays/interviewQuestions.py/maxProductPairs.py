# Function to find the maximum product of two numbers in a list
def max_product(arr):
    # Initialize the two largest numbers as 0
    first_max = second_max = 0

    # Traverse the list to find the two largest numbers
    for num in arr:
        if num > first_max:  # If the current number is larger than the largest number
            second_max = first_max  # Update the second largest number
            first_max = num  # Update the largest number
        elif num > second_max:  # If the current number is larger than the second largest
            second_max = num  # Update the second largest number

    # Return the product of the two largest numbers
    return first_max * second_max

# Input: number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Input: elements of the list
st = []
for i in range(n):
    b = int(input(f"Enter element {i + 1}: "))
    st.append(b)

# Call the function and print the result
print("Maximum product of two numbers:", max_product(st))
