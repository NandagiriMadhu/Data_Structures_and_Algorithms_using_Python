tup = ('a', 'b', 'c', 'd', 'e')

print(tup[1])  # Output: 'b' -> accessing the element at index 1, which is 'b'
print(tup[-1])  # Output: 'e' -> accessing the last element using negative index

print(tup[1:3])  # Output: ('b', 'c') -> slicing from index 1 to 3 (not including 3), gives ('b', 'c')
print(tup[-3:-1])  # Output: ('c', 'd') -> slicing from index -3 to -1 (not including -1), gives ('c', 'd')
print(tup[1:-3])  # Output: ('b',) -> slicing from index 1 to -3 (not including -3), gives ('b',)
print(tup[:3])  # Output: ('a', 'b', 'c') -> slicing from the start to index 3 (not including 3), gives ('a', 'b', 'c')
print(tup[1:])  # Output: ('b', 'c', 'd', 'e') -> slicing from index 1 to the end, gives ('b', 'c', 'd', 'e')
print(tup[:])  # Output: ('a', 'b', 'c', 'd', 'e') -> slicing from the start to the end, gives the whole tuple
