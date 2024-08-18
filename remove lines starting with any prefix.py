file1 = open('hellowords.txt','r')
 
# defining object file2 to open GeeksforGeeksUpdated file in write mode
file2 = open('hellowordsUpdated.txt','w')
 
# reading each line from original text file
for line in file1.readlines():
   
     # reading all lines that do not begin with "TextGenerator"
    if not (line.startswith('TextGenerator')):
       
        # printing those lines
        print(line)
         
        # storing only those lines that 
        # do not begin with "TextGenerator"
        file2.write(line)
 
# close and save the files
file2.close()
file1.close()