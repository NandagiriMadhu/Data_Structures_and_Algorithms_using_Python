def insert_value_front(input_tuple, value_to_insert):
    # Create a new tuple by prepending value_to_insert to the input_tuple
    return (value_to_insert,) + input_tuple

# Example usage: insert 0 at the front of the tuple (1, 2, 3)
print(insert_value_front((1, 2, 3), 0))
