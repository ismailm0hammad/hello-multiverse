def hasConsecutiveZeroes(N, K):
	# Convert N to base K
	s = ""
	while N > 0:
		s = str(N % K) + s
		N //= K

	# Traverse through the converted string and check for consecutive 0s
	count = 0
	for c in s:
		if c == '0':
			count += 1
			if count >= 2:
				return False
		else:
			count = 0

	return True

N = int(input())
K = int(input())
if hasConsecutiveZeroes(N, K):
	print("Yes")
else:
	print("No")
