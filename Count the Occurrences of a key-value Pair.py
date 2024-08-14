# opening text file
f = open("file.txt", "r")
d = dict()

for res in f:
	# removing new line and extra
	# space characters
	res = res.strip()

	# changing ase to prevent matching
	# errors
	res = res.lower()

	# separating key-value pairs
	lines = res.split()

	for line in lines:

		if line in d:

			# If the key-value pair
			# is present in d then 
			# increment its value by one
			d[line] = d[line]+1
		else:

			# Insert the key-value pair
			# in the dictionary and sets
			# its value to one
			d[line] = 1

f.close()

# Printing Result
for key in list(d.keys()):
	print("The count of {} is {}".format(key,d[key]))
