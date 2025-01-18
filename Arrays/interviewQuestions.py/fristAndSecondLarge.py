# Function to find the first and second largest numbers in a list
def first_second(my_list):
    # Sort the list in descending order
    sorted_list = sorted(my_list, reverse=True)
    
    # The largest number is the first element in the sorted list
    first_num = sorted_list[0]
    
    # Initialize the second largest number to 0
    second_num = 0
    
    # Iterate through the sorted list to find the first number less than the largest
    for num in sorted_list:
        if num < first_num:
            second_num = num  # Update second largest number
            break  # Exit the loop once the second largest number is found

    return first_num, second_num  # Return the largest and second largest numbers

# Input: number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Input: elements of the list
st = []
for i in range(n):
    b = int(input(f"Enter element {i + 1}: "))
    st.append(b)

# Call the function and print the result
print("First and second largest numbers:", first_second(st))
