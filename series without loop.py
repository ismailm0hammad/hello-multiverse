# print series without loop
def print_series(N, K):
	if N <= 0:
		print(N, end=" ")
		return
	print(N, end=" ")
	print_series(N-K, K)
	print(N, end=" ")

N = int(input())
K = int(input())
print_series(N, K)