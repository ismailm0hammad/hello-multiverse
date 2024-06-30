

def replace_substring(test_str, s1, s2):
	# Initialize an empty string to store the result
	result = ""
	# Initialize a variable to keep track of our position in the string
	i = 0
	# Loop through the string one character at a time
	while i < len(test_str):
		# Check if the current substring matches the substring we want to replace
		if test_str[i:i+len(s1)] == s1:
			# If it does, add the replacement substring to the result and move the pointer forward
			result += s2
			i += len(s1)
		else:
			# If it doesn't, add the current character to the result and move the pointer forward
			result += test_str[i]
			i += 1
	# Return the final result
	return result

# test
test_str = "Hello world. Welcome to the new world."
s1="world"
s2="universe"
print(replace_substring(test_str, s1, s2))
