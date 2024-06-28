def checkEmpty(input, pattern):
	
	# If both are empty
	if len(input)== 0 and len(pattern)== 0:
		return 'true'

	# If only pattern is empty
	if len(pattern)== 0:
		return 'false'

	while (len(input) != 0):

		# find sub-string in main string
		index = input.find(pattern)

		# check if sub-string founded or not
		if (index ==(-1)):
			return 'false'

		# slice input string in two parts and concatenate
		input = input[0:index] + input[index + len(pattern):]		 
	return 'true'

# Driver program
if __name__ == "__main__":
	input ='HELLHELLOO'
	pattern ='HELLO'
	print (checkEmpty(input, pattern))
