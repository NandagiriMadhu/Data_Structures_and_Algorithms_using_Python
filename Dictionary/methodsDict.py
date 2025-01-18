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
print(d.items())
print(d.keys())
print(d.values())
g = {"a":1, "b":2}
d.update(g)
print(d)
print(d.get('age', 28))
print(d.get("or", 23))
print(d.get("city"))
print(d.popitem())
print(d)
print(d.setdefault("age", 25))
print(d.setdefault("name1", "added"))
print(d.pop("name2", "not"))
print(d)
e = {}.fromkeys([1,2,3,4], 0)
print(e)
f = {}.fromkeys([1,2,3,4])
print(f)