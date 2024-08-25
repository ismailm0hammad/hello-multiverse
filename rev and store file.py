# Open the file in write mode
fl = open("out.txt", "w")

# Open the input file and get 
# the content into a variable data
with open("file.txt", "r") as myfile:
	data = myfile.read()

'''For Full Reversing we will store the 
value of data into new variable new_data 
in a reverse order using [start: end: step],
where step when passed -1 will reverse 
the string'''
new_data = data[::-1]

'''Now we will write the fully reverse 
data in the out file using 
following command'''
fl.write(new_data)

fl.close()
