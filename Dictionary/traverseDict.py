a = int(input())
d = {}
for i in range(1, a + 1):
    b = input()
    c = input()
    if c.isdigit():
        c = int(c)
    if b.isdigit():
        b = int(b)
    d[b] = c
print(d)

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(d)