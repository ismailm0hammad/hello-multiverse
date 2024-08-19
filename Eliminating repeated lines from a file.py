def remove_duplicates(input_file, output_file):
	lines_seen = set()
	with open(output_file, 'w') as out_file:
		with open(input_file, 'r') as in_file:
			for line in in_file:
				if line not in lines_seen:
					out_file.write(line)
					lines_seen.add(line)

# Usage
input_file = open('C:/Users/user/Desktop/Lorem_input.txt', "r")
output_file = open('C:/Users/user/Desktop/Lorem_output.txt', "w")
remove_duplicates(input_file, output_file)


# Using psndas
import pandas as pd

def remove_duplicates(input_file, output_file):
	df = pd.read_csv(input_file, header=None)
	df.drop_duplicates(inplace=True)
	df.to_csv(output_file, header=False, index=False)

# creating the output file
outputFile = open('C:/Users/user/Desktop/Lorem_output.txt', "w")
# reading the input file
inputFile = open('C:/Users/user/Desktop/Lorem_input.txt', "r")
remove_duplicates(input_file, output_file)
