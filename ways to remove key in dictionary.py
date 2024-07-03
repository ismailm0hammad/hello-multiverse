# Initializing dictionary
test_dict = {"Ismail": 22, "Visesh": 21, "Rehman": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : ", test_dict)

# Using del to remove a dict
# removes Visesh
del test_dict['Visesh']

# Printing dictionary after removal
print("The dictionary after remove is : ", test_dict)

# Initializing dictionary
test_dict = {"Ismail": 22, "Umesh": 21, "Visesh": 21, "Rehman": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : " + str(test_dict))

# Using pop() to remove a dict. pair
# removes Visesh
removed_value = test_dict.pop('Visesh')

# Printing dictionary after removal
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))

print('\r')

# Using pop() to remove a dict. pair
# doesn't raise exception
# assigns 'No Key found' to removed_value
removed_value = test_dict.pop('Manjeet', 'No Key found')

# Printing dictionary after removal
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))

# Initializing dictionary
test_dict = {"Ismail": 22, "Umesh": 21, "Visesh": 21, "Rehman": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : \n" + str(test_dict))

a_dict = {key: test_dict[key] for key in test_dict if key != 'Visesh'}

print("The dictionary after performing remove is : \n", a_dict)
