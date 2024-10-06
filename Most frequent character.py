# Function to find the most frequent character in a string
def most_frequent_char(s):
    frequency = {}  # Dictionary to count frequency of each character
    for char in s:
        if char in frequency:
            frequency[char] += 1  # Increment count if character exists in dictionary
        else:
            frequency[char] = 1  # Initialize count if character does not exist in dictionary
    return max(frequency, key=frequency.get)  # Return character with the highest frequency

# Example usage
string = "Your input string"
most_frequent = most_frequent_char(string)
print(f'Most frequent character: {most_frequent}')  # Print most frequent character
