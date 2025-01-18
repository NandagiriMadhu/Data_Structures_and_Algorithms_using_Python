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

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The Value doesn't exist"

e = input()
if e.isdigit():
    e = int(e)
print(searchDict(d, e))