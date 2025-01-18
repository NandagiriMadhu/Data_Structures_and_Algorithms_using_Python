# Function to find the missing number from 1 to N natural numbers
def missingNumber(num_list, n):
    # Calculate the expected sum of the first N natural numbers using the formula
    total = n * (n + 1) // 2
    
    # Calculate the sum of the numbers in the given list
    current_sum = sum(num_list)
    
    # The missing number is the difference between the expected sum and the current sum
    missing_num = total - current_sum
    return missing_num

# Input: The value of N (total count of numbers including the missing one)
n = int(input("Enter the value of N: "))

# Input: The list of numbers (should contain N-1 numbers)
st = []
print(f"Enter {n - 1} numbers between 1 and {n}:")
for i in range(n - 1):
    b = int(input(f"Enter number {i + 1}: "))
    st.append(b)

# Call the function and print the missing number
print("The missing number is:", missingNumber(st, n))
