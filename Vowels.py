# Function to count vowels in a string
def count_vowels(s):
    vowels = 'AEIOUaeiou'  # String containing all vowels
    total_vowels = sum(1 for char in s if char in vowels)  # Count total vowels
    counts = {vowel: s.lower().count(vowel) for vowel in 'aeiou'}  # Count each vowel
    return total_vowels, counts  # Return total count and individual counts

# Example usage
string = "Guvi Geeks Network Private Limited"
total, vowel_counts = count_vowels(string)
print(f'Total vowels: {total}')  # Print total vowel count
print(f'Vowel counts: {vowel_counts}')  # Print individual vowel counts
