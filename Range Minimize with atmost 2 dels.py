# Codechef : https://www.codechef.com/problems/MNR

for _tcs_ in range(int(input())):
    nism=int(input()) # size/no. of elemnts
    ism = list(map(int,input().split())) # List of nums
    ism.sort() # sorted list of nums
    min1 = ism[-1] - ism[2] # delete first two, max = last element, min = 3rd element
    min2 = ism[-3] - ism[0] # delete last two, max = 3rd from last, min = 1st element
    min3 = ism[-2] - ism[1] # delete first & last, max = 2ndlast element, min = 3rd element
    print(min([min1,min2,min3])) #printing minimum of 3 possibilities