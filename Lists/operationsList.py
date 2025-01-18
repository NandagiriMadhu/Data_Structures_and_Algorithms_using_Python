# Initializing two lists and combining them into a new list 'c'
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b  # Concatenate the two lists 'a' and 'b'
print(c)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Calculate and print the length of the list 'c'
print(len(c))  # Output: 8 (length of the concatenated list)

# Find and print the maximum value in list 'a'
print(max(a))  # Output: 4 (maximum value in list 'a')

# Calculate and print the sum of the list 'c'
print(sum(c))  # Output: 36 (sum of elements in list 'c')

# Calculate and print the average of the list 'a'
print(sum(a)/len(a))  # Output: 2.5 (average of list 'a')

# Create a list 'd' and repeat it 4 times
d = [5, 6]
d = d * 4  # Repeat list 'd' 4 times
print(d)  # Output: [5, 6, 5, 6, 5, 6, 5, 6]

# Calculate the average of numbers entered by the user using a while loop
total = 0
count = 0

while(True):
    inp = input('Enter a number: ')  # Ask the user for input
    if inp == 'done': break  # Break the loop if the user enters 'done'
    value = float(inp)  # Convert the input to a float
    total = total + value  # Add the value to the total sum
    count = count + 1  # Increment the count
    avg = total / count  # Calculate the average

print("average", avg)  # Print the average
print(f"average {avg}")  # Print the average using an f-string

# Create an empty list 'myList' and append numbers entered by the user
myList = list()

while(True):
    inr = input('Enter a number: ')  # Ask the user for input
    if inr == 'done': break  # Break the loop if the user enters 'done'
    value = float(inr)  # Convert the input to a float
    myList.append(value)  # Append the value to the list
avge = sum(myList) / len(myList)  # Calculate the average of the list

print("average", avge)  # Print the average
print(f"average {avge}")  # Print the average using an f-string
