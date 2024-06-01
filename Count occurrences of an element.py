# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,countX(lst, x)))

l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5] 
ele=1
x=[i for j,i in enumerate(l) if i==ele] 
print("the element",ele,"occurs",len(x),"times")


from collections import Counter

# declaring the list
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))

import operator as op

# declaring the list
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
x = 2
print(f"{x} has occurred {op.countOf(l, x)} times")
