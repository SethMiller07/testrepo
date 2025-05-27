def is_palindrome(s):
    s = s.lower()  # Make the string lowercase
    return s == s[::-1]  # Check if it reads the same backwards
