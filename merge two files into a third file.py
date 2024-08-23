data1 = data2 = "";

# Reading data1 from file1
with open('file1.txt') as fp:
	data1 = fp.read()

# Reading data1 from file2
with open('file2.txt') as fp:
	data2 = fp.read()

data1 += "\n"
data1 += data2

with open ('file3.txt', 'w') as fp:
	fp.write(data1)
