# Python3 code to demonstrate
# Matrix Product
# Using chain() + loop
from itertools import chain

# getting Product


def prod(val):
	res = 1
	for ele in val:
		res *= ele
	return res


# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))

# using chain() + loop
# Matrix Product
res = prod(list(chain(*test_list)))

# print result
print("The total element product in lists is : " + str(res))
