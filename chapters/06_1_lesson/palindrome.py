def is_palindrome(word):
    """Check if a word is a palindrome."""
    if len(word) <= 1:
        return True
    return word == word[::-1]

# Test cases
print(is_palindrome("racecar"))  # Should print True
print(is_palindrome("hello"))    # Should print False
print(is_palindrome("a"))        # Should print True
print(is_palindrome(""))         # Should print True
print(is_palindrome("madam"))    # Should print True