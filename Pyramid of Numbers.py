# Loop through numbers from 1 to 20
for i in range(1, 21):
    # Loop to print numbers for the current row
    for j in range(1, i+1):
        print(j, end=' ')  # Print number and stay on the same line
    print()  # Move to the next line after each row
