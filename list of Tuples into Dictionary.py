def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di


# Driver Code
tups = [("ismail", 10), ("rehman", 12), ("umesh", 14),
		("vamsi", 20), ("dinesh", 25), ("gouse", 30)]
dictionary = {}
print(Convert(tups, dictionary))
