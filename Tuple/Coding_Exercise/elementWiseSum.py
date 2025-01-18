def tuple_elementwise_sum(t1, t2):
    # Check if the lengths of the two input tuples are the same
    if len(t1) != len(t2):
        # Raise an error if the lengths do not match
        raise ValueError("Input tuples must have the same length.")
    
    # Use a tuple comprehension to add corresponding elements from both tuples
    result = tuple(a + b for a, b in zip(t1, t2))
    
    # Return the resulting tuple
    return result

# Example usage: sum corresponding elements from two tuples
print(tuple_elementwise_sum((1, 2, 3, 4), (5, 6, 7, 8)))
