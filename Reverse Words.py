# initializing string
string = "This code reverse the words in string"

# creating an empty stack
stack = []

# pushing words onto the stack
for word in string.split():
	stack.append(word)

# creating an empty list to store the reversed words
reversed_words = []

# popping words off the stack and appending them to the list
while stack:
	reversed_words.append(stack.pop())

# joining the reversed words with a space
reversed_string = " ".join(reversed_words)

# printing the reversed string
print(reversed_string)
