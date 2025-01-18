a = int(input("Enter the number of days of temperature you want to give: "))
c = 0
for i in range(1, a + 1):
    b = float(input("Enter the temperatue of day " + str(i) + " : "))
    c += b
print(c / a)


temp = int(input("Enter the number of days of temperature you want to give: "))
list = []
for j in range(1, temp + 1):
    d = float(input("Enter the temperatue of day " + str(j) + " : "))
    list.append(d)
print(sum(list) / len(list))