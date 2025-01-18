def get_diagonal(input_tuple):
    # Use tuple comprehension to extract diagonal elements from a 2D tuple
    # For each index 'i', access the element at position (i, i)
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# Example usage: extract diagonal elements from a 2D tuple (matrix)
print(get_diagonal(((1, 2, 3), (4, 5, 6), (7, 8, 9))))
