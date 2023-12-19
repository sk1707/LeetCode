def lengthOfLongestSubstring(s):
    # Set to store the unique characters in the current window
    char_set = set()

    # These pointers will define the sliding window (left and right borders)
    left = 0
    right = 0

    # This will hold the length of the longest substring without repeating characters
    max_length = 0

    # Start sliding the window
    while right < len(s):
        # If the character is not in the set, add it and move the right pointer
        if s[right] not in char_set:
            char_set.add(s[right])
            right += 1
            # Update max_length if we've found a new longest
            max_length = max(max_length, right - left)
        else:
            # If we've seen the character, remove the leftmost character and move the left pointer
            char_set.remove(s[left])
            left += 1

    # Return the maximum length found
    return max_length


# Example usage:
input_string = "pwwkew"
print(f"Length of the longest substring without repeating characters: {lengthOfLongestSubstring(input_string)}")
