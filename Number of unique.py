def unique_char_count(s):
    return len(set(s))

string = "Your input string"
unique_count = unique_char_count(string)
print(f'Number of unique characters: {unique_count}')
# Function to count unique characters in a string
def unique_char_count(s):
    return len(set(s))  # Convert string to set to get unique characters and return its length

# Example usage
string = "Your input string"
unique_count = unique_char_count(string)
print(f'Number of unique characters: {unique_count}')  # Print count of unique characters
