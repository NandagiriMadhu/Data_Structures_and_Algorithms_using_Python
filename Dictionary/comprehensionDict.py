import random

a = int(input())
b = [] 
for i in range(1, a + 1):
    c = input()
    b.append(c)
print(b)
d = {i:random.randint(20, 30) for i in b}
print(d)

e = {i:temp for (i, temp) in d.items() if temp > 25}
print(e)
print(d['2'])