# Python3 code to demonstrate working of 
# Closest Pair to Kth index element in Tuple
# Using enumerate() + loop

# initializing list
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]

# printing original list
print("The original list is : " + str(test_list))

# initializing tuple
tup = (17, 23)

# initializing K 
K = 1

# Closest Pair to Kth index element in Tuple
# Using enumerate() + loop
min_dif, res = 999999999, None
for idx, val in enumerate(test_list):
    dif = abs(tup[K - 1] - val[K - 1])
    if dif &lt; min_dif:
        min_dif, res = dif, idx

# printing result 
print("The nearest tuple to Kth index element is : " + str(test_list[res])) 
