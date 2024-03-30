# This program calculates the power sum of a number

# input the number
n = int(input("Enter ")) 

# initialize sum to 0
sum = 0 

# initialize power value to 0
pv = 0 

# loop until all digits of the number are processed
while n>0:
    # get the last digit of the number
    u = n%10   
    # add the current digit raised to the power of the previous digit
    sum = sum + (u**pv) 
    # set the current digit as the power value for the next iteration
    pv=u  
    # remove the last digit of the number
    n//=10 

# print the sum

print(sum)