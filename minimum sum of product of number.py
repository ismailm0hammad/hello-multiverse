# Find minimum sum of product of number

# To find minimum sum of
# product of number

def find_min_sum(num):
	min_sum = num
	
	for i in range(2, int(num**0.5) + 1):
		if num % i == 0:
			factor = num // i
			min_sum = min(min_sum, i + factor)
	
	return min_sum

# driver code
number = int(input())

# Call the function and print the result
result = find_min_sum(number)
print("The minimum sum of factors for", number, "is", result)

