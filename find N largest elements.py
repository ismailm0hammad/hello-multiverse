# Python program to find N largest
# element from given list of integers

# Function returns N largest elements


def Nmaxelements(list1, N):
	final_list = []

	for i in range(0, N):
		max1 = 0

		for j in range(len(list1)):
			if list1[j] > max1:
				max1 = list1[j]

		list1.remove(max1)
		final_list.append(max1)

	print(final_list)


# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

# Calling the function
Nmaxelements(list1, N)




# Python program to find N largest
# element from given list of integers
#using sort function

l = [1000, 298, 3579, 100, 200, -45, 900]
n = 4

l.sort()
print(l[-n:])
