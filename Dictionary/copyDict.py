# Input number of key-value pairs to be added to the dictionary
a = int(input("Enter the number of key-value pairs: "))

# Initialize an empty dictionary
d = {}

# Loop to take user inputs for key-value pairs and add them to the dictionary
for i in range(1, a + 1):
    b = input(f"Enter key {i}: ")  # Taking input for the key
    c = input(f"Enter value for key {b}: ")  # Taking input for the value

    # If the value is a digit, convert it to an integer
    if c.isdigit():
        c = int(c)

    # If the key is a digit, convert it to an integer
    if b.isdigit():
        b = int(b)
    
    # Add the key-value pair to the dictionary
    d[b] = c

# Printing the original dictionary
print("Original dictionary (d):", d)

# Assigning the original dictionary to a new variable e (Shallow Copy)
e = d
print("Shallow copy (e):", e)

# Input to modify an element in the shallow copy (e)
f = input("Enter a key to modify in the shallow copy (e): ")

# If the key is a digit, convert it to an integer
if f.isdigit():
    f = int(f)

# Modify the key-value pair in the shallow copy if the key exists
if f in e:
    e[f] = 100
else:
    print(f"Key {f} not found in the dictionary!")

# After modification, print both the original and shallow copy
print("After modification:")
print("Original dictionary (d):", d)
print("Shallow copy (e):", e) 

# Create an independent copy of the original dictionary
g = {}
for key, value in d.items():
    g[key] = value

# Input to modify an element in the independent copy (g)
h = input("Enter a key to modify in the independent copy (g): ")

# If the key is a digit, convert it to an integer
if h.isdigit():
    h = int(h)

# Modify the key-value pair in the independent copy if the key exists
if h in g:
    g[h] = "age"
else:
    print(f"Key {h} not found in the dictionary!")

# After independent copy modification, print all three dictionaries
print("After independent copy modification:")
print("Original dictionary (d):", d)
print("Shallow copy (e):", e)
print("Independent copy (g):", g)
