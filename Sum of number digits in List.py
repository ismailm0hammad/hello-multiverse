# Python3 code to demonstrate 
# Sum of number digits in List
# using loop + str()

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using loop + str()
res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)
    
# printing result 
print ("List Integer Summation : " + str(res))

# Python3 code to demonstrate 
# Sum of number digits in List
# using sum() + list comprehension

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using sum() + list comprehension
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
    
# printing result 
print ("List Integer Summation : " + str(res))

import numpy as np

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using numpy
res = np.sum([list(map(int, str(ele))) for ele in test_list], axis=1)

# printing result
print("List Integer Summation : " + str(list(res)))
