def parse(d):
	dictionary = dict()
	# Removes curly braces and splits the pairs into a list
	pairs = d.strip('{}').split(', ')
	for i in pairs:
		pair = i.split(': ')
		# Other symbols from the key-value pair should be stripped.
		dictionary[pair[0].strip('\'\'\"\"')] = pair[1].strip('\'\'\"\"')
	return dictionary
try:
	ism_file = open('ism_file.txt', 'rt')
	lines = ism_file.read().split('\n')
	for l in lines:
		if l != '':
			dictionary = parse(l)
			print(dictionary)
	ism_file.close()
except:
	print("Something unexpected occurred!")
