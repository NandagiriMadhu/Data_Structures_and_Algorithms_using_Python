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
print("name" in d)
print("name" not in d)
print(23 in d.values())
print(23 not in d.values())
print(len(d))
print(all(d))
print(any(d))
print(sorted(d))