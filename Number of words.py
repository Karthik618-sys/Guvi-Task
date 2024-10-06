# Function to count the number of words in a string
def word_count(s):
    return len(s.split())  # Split the string by spaces and return the length of the list

# Example usage
string = "Your input string"
num_words = word_count(string)
print(f'Number of words: {num_words}')  # Print number of words in the string
