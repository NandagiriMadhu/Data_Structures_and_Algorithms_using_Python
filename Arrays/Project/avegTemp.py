import array as arr

# Asking the user how many days of temperature data to input
a = int(input("How many days? "))

# Creating an empty array to store high temperatures
arr1 = arr.array("f", [])  # 'f' indicates that the array stores float values
c = 0  # Variable to accumulate the sum of temperatures

# Loop to get temperatures for each day
for i in range(a):
    day = float(input("day " + str(i + 1) + "'s high temperature: "))  # Get temperature input for each day
    arr1.insert(i, day)  # Insert the temperature into the array at the corresponding index
    c += day  # Add the temperature to the total sum

# Calculating the average temperature
d = c / a
print("Average temperature:", d)

# Checking each day to see if the temperature was higher than the average
for j in range(a):
    if arr1[j] > d:  # If the temperature is greater than the average
        print("day " + str(j + 1) + " has a temperature higher than " + str(arr1[j]) + ".")
