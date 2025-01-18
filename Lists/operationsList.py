a = [1,2,3,4]
b = [5,6,7,8]
c = a + b
print(c)

print(len(c))

print(max(a))

print(sum(c))

print(sum(a)/len(a))

d = [5, 6]
d = d * 4
print(d)

total = 0
count = 0

while(True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    avg = total / count

print("average",avg)
print(f"average {avg}")

myList = list()

while(True):
    inr = input('Enter a number: ')
    if inr == 'done': break
    value = float(inr)
    myList.append(value)
avge = sum(myList)/len(myList)

print("average",avge)
print(f"average {avge}")
