def twoSum(nums, target):
    # Loop through each number in the list
    for i in range(len(nums)):
        # Loop through the list again, starting from the next number
        for j in range(i + 1, len(nums)):
            # Check if the sum of the current pair of numbers equals the target
            if nums[i] + nums[j] == target:
                # If it does, return their indices
                return [i, j]

    # If no pair is found, return an empty list
    return []

# Example usage of the function
numbers = [2, 7, 11, 15]
target_sum = 9
result = twoSum(numbers, target_sum)

# Print the result
print(f"Indices of numbers that add up to {target_sum}: {result}")
