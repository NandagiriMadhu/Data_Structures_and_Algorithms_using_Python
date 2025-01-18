import array as arr

a = int(input("How many days? "))
arr1 = arr.array("f", [])
c = 0 

for i in range(a):
    day = float(input("day " + str(i + 1) + "'s high temperature: "))
    arr1.insert(i, day)
    c += day 

d = c / a
print("Average temperature:", d)

for j in range(a):
    if arr1[j] > d:
        print("day " + str(j + 1) + " has a temperature higher than " + str(arr1[j]) + ".")
