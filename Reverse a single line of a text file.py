# Open file in read mode
f = open('demo.txt', 'r')

# Read the content of the
# file and store it in a list
lines = f.readlines()
	
# Close file
f.close()

# User's choice
choice = 1

# Split the line into words 
line = lines[choice].split()

# line is reversed
Reversed = " ".join(line[::-1])

# Updating the content of the
# file
lines.pop(choice)
lines.insert(choice, Reversed)

# Open file in write mode
u = open('demo.txt', 'w')

# Write the new content in file
# and note, it is overwritten 
u.writelines(lines)
u.close()
