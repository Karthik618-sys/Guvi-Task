# Function to check if two strings are anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)  # Check if sorted characters of both strings are equal

# Example usage
string1 = "Your first string"
string2 = "Your second string"
result = is_anagram(string1, string2)
print(f'Are the strings anagrams? {result}')  # Print whether the strings are anagrams
