def common_elements(tuple1, tuple2):
    # Convert both tuples to sets and find their intersection using the '&' operator
    # The intersection of two sets contains only the elements that are present in both sets
    return tuple(set(tuple1) & set(tuple2))

# Example usage: find common elements between two tuples
print(common_elements((1, 2, 3, 4), (3, 4, 5, 6)))
