def longest_palindromic_substring(s):
    def is_palindrome(subs):
        # Helper function to check if a string is a palindrome
        return subs == subs[::-1]

    max_length = 0
    longest_palindrome = ""

    # Loop through the string
    for i in range(len(s)):
        # Loop through the string again for each character
        for j in range(i, len(s)):
            # If the current substring is a palindrome and its length is greater than max_length
            if is_palindrome(s[i:j + 1]) and max_length < j - i + 1:
                # Update the max_length and longest_palindrome
                max_length = j - i + 1
                longest_palindrome = s[i:j + 1]

    return longest_palindrome

# Test the function
input_string = "babad"
print("The longest palindromic substring is:", longest_palindromic_substring(input_string))
