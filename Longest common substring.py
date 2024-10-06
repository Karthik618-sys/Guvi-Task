# Function to find the longest common substring between two strings
def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]  # Initialize a matrix for dynamic programming
    longest, x_longest = 0, 0  # Variables to track the longest length and position
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:  # Check if characters match
                m[x][y] = m[x - 1][y - 1] + 1  # Increment length of common substring
                if m[x][y] > longest:
                    longest = m[x][y]  # Update longest length
                    x_longest = x  # Update position
            else:
                m[x][y] = 0  # Reset if characters do not match
    return s1[x_longest - longest: x_longest]  # Return the longest common substring

# Example usage
string1 = "Your first string"
string2 = "Your second string"
result = longest_common_substring(string1, string2)
print(f'Longest common substring: {result}')  # Print longest common substring
