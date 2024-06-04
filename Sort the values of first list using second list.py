def sorting_of_element(list1, list2):

	# initializing blank dictionary
	f_1 = {}

	# initializing blank list
	final_list = []

	# Addition of two list in one dictionary
	f_1 = {list1[i]: list2[i] for i in range(len(list2))}

	# sorting of dictionary based on value
	f_lst = {k: v for k, v in sorted(f_1.items(), key=lambda item: item[1])}

	# Element addition in the list
	for i in f_lst.keys():
		final_list.append(i)
	return final_list


list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]


list3 = sorting_of_element(list1, list2)
print(list3)
