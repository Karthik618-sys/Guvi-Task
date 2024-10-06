# Function to check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]  # Compare string with its reverse

# Example usage
string = "Your input string"
result = is_palindrome(string)
print(f'Is the string a palindrome? {result}')  # Print whether the string is a palindrome
