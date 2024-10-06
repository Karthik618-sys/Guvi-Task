# Function to remove vowels from a string
def remove_vowels(s):
    vowels = 'AEIOUaeiou'  # String containing all vowels
    return ''.join([char for char in s if char not in vowels])  # Join characters that are not vowels

# Example usage
string = "Your input string"
result = remove_vowels(string)
print(result)  # Print string without vowels
