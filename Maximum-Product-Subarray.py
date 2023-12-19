def max_product_subarray(nums):
    # Initialize the maximum product as the first element of the array
    max_product = nums[0]
    # Initialize the current maximum and minimum product as 1
    curr_max_product = 1
    curr_min_product = 1

    # Loop through each number in the array
    for num in nums:
        # If the number is zero, reset the current max and min product to 1
        # because the product of any number with zero is zero.
        if num == 0:
            curr_max_product = 1
            curr_min_product = 1
            max_product = max(max_product, 0)
            continue

        # Temporarily store the current max product
        temp_max = curr_max_product

        # Update the current maximum product
        curr_max_product = max(num, num * curr_max_product, num * curr_min_product)
        # Update the current minimum product
        curr_min_product = min(num, num * temp_max, num * curr_min_product)

        # Update the maximum product found so far
        max_product = max(max_product, curr_max_product)

    return max_product


# Example usage:
example_1 = [2, 3, -2, 4]
example_2 = [-2, 0, -1]

# Find the maximum product subarray for the first example
max_product_1 = max_product_subarray(example_1)
print("Maximum product of subarray in [2, 3, -2, 4]:", max_product_1)

# Find the maximum product subarray for the second example
max_product_2 = max_product_subarray(example_2)
print("Maximum product of subarray in [-2, 0, -1]:", max_product_2)
