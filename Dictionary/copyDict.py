a = int(input("Enter the number of key-value pairs: "))
d = {}
for i in range(1, a + 1):
    b = input(f"Enter key {i}: ")
    c = input(f"Enter value for key {b}: ")
    if c.isdigit():
        c = int(c)
    if b.isdigit():
        b = int(b)
    d[b] = c
print("Original dictionary (d):", d)

e = d
print("Shallow copy (e):", e)

f = input("Enter a key to modify in the shallow copy (e): ")
if f.isdigit():
    f = int(f)
if f in e:
    e[f] = 100
else:
    print(f"Key {f} not found in the dictionary!")

print("After modification:")
print("Original dictionary (d):", d)
print("Shallow copy (e):", e) 

g = {}
for key, value in d.items():
    g[key] = value 

h = input("Enter a key to modify in the independent copy (g): ")
if h.isdigit():
    h = int(h)
if h in g:
    g[h] = "age"
else:
    print(f"Key {h} not found in the dictionary!")

print("After independent copy modification:")
print("Original dictionary (d):", d)
print("Shallow copy (e):", d)
print("Independent copy (g):", g)
