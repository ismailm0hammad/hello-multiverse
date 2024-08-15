def find_words_with_three_chars(file_path,n):
	with open(file_path, 'r') as file:
		content = file.read()
		words = content.split()

		words_with_three_chars = [word for word in words if len(word) == n]

		return words_with_three_chars

file_name = "smile.txt"
result = find_words_with_three_chars(file_name,3)

print("Words containing three characters:")
print(result)