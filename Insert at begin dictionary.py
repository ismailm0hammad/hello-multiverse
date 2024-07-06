# Python code to demonstrate
# insertion of items in beginning of ordered dict
from collections import OrderedDict

# initialising ordered_dict
ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil', '2')])
ini_dict2 = OrderedDict([("manjeet", '4'), ("akash", '4')])

# adding in beginning of dict
both = OrderedDict(list(ini_dict2.items()) + list(ini_dict1.items()))

# print result
print ("Resultant Dictionary :"+str(both))
