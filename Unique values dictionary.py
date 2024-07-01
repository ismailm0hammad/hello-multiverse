# Python3 code to demonstrate working of
# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()

# initializing dictionary
test_dict = {'A': [5, 6, 7, 8],
			'B': [10, 11, 7, 5],
			'C': [6, 12, 10, 8],
			'D': [1, 2, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract Unique values dictionary values
# Using set comprehension + values() + sorted()
res = list(sorted({ele for val in test_dict.values() for ele in val}))

# printing result
print("The unique values list is : " + str(res))
