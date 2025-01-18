# First approach using a simple loop for calculating the average temperature:

a = int(input("Enter the number of days of temperature you want to give: "))  # Input the number of days
c = 0  # Initialize variable to hold the sum of temperatures
for i in range(1, a + 1):  # Loop for the number of days
    b = float(input("Enter the temperature of day " + str(i) + " : "))  # Input temperature for each day
    c += b  # Add the temperature of the day to the sum
print(c / a)  # Calculate and print the average temperature

# Second approach using a list to store the temperatures:

temp = int(input("Enter the number of days of temperature you want to give: "))  # Input the number of days
list = []  # Initialize an empty list to store the temperatures
for j in range(1, temp + 1):  # Loop for the number of days
    d = float(input("Enter the temperature of day " + str(j) + " : "))  # Input temperature for each day
    list.append(d)  # Append each temperature to the list
print(sum(list) / len(list))  # Calculate and print the average temperature from the list