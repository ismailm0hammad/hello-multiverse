def find_word_line_number(filename, target_word):
	line_number = 0

	with open(filename, 'r') as file:
		for line in file:
			line_number += 1
			if target_word in line:
				return line_number

	# If the word is not found in the file, return None
	return None

# Example usage
filename = "File_1.txt" # Replace with the name of your file
word_to_find = "hello" # Replace with the word you want to find
line_number = find_word_line_number(filename, word_to_find)
if line_number is not None:
	print(f"The word '{word_to_find}' is present in line number: {line_number}")
else:
	print(f"The word '{word_to_find}' is not found in the file.")
