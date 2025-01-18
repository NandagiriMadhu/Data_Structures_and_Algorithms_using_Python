def sum_product(input_tuple):
    # Initialize sum and product variables
    sum_result = 0  # This will hold the sum of the elements in the tuple
    product_result = 1  # This will hold the product of the elements in the tuple
    
    # Iterate over each element in the input tuple
    for i in range(len(input_tuple)):
        # Add the current element to sum_result
        sum_result += input_tuple[i]
        
        # Multiply the current element with product_result
        product_result *= input_tuple[i]
        
    # Return both the sum and product of the elements
    return sum_result, product_result

# Example usage: calculate sum and product of elements in the tuple (1, 2, 3, 4)
print(sum_product((1, 2, 3, 4)))
