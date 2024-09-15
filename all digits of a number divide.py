from math import sqrt

def factorize(n):
	factors = []
	while n % 2 == 0:
		factors.append(2)
		n = n // 2
	for i in range(3, int(sqrt(n)) + 1, 2):
		while n % i == 0:
			factors.append(i)
			n = n // i
	if n > 2:
		factors.append(n)
	return factors

def check_divide(n):
	factors = factorize(n)
	for factor in factors:
		if factor < 1 or factor > 9 or n % factor != 0:
			return 'No'
	return 'Yes'
n=int(input()) # Example 128
print(check_divide(n))
