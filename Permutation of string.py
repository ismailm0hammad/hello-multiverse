def generate_permutations(string):
	if len(string) == 1:
		return [string]

	permutations = []
	for i in range(len(string)):
		fixed_char = string[i]
		remaining_chars = string[:i] + string[i+1:]
		for perm in generate_permutations(remaining_chars):
			permutations.append(fixed_char + perm)

	return permutations

string ='ismail'

permutations_list = generate_permutations(string)
z=set(permutations_list)

for perm in z:
	print(perm)
