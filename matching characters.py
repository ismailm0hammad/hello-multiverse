def count(str1, str2):
    # Initialize an empty dictionary to keep track of the count of each character in str1.
    char_count = {}

    # Iterate over each character in str1.
    for char in str1:
        # If the character is already in the dictionary, increment its count.
        if char in char_count:
            char_count[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1.
        else:
            char_count[char] = 1

    # Initialize a counter variable to 0.
    counter = 0

    # Iterate over each character in str2.
    for char in str2:
        # If the character is in the char_count dictionary and its count is greater than 0, increment the counter and decrement the count.
        if char in char_count and char_count[char] > 0:
            counter += 1
            char_count[char] -= 1

    # Print the number of matching characters.
    print("No. of matching characters are: " + str(counter))

# Driver code
if __name__ == "__main__":
    # Define two strings to compare.
    str1 = 'aabcddekll12@'
    str2 = 'bb2211@55k'

    # Call the count function with the two strings.
    count(str1, str2)
