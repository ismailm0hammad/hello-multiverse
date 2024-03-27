n = int(input("emter a no."))
'''div = 2
while div<n:
    if div<n:
        if n%div==0:
            print("not prime")
            break
        else:
            div+=1
    else:
        print("prime")
if n>1:
    for i in range(2,n):
        print(i)
        if n%i==0:
            print(n,n/i,i)
            print("for not prime")
            break
    else:
        print("for prime")
see first a limit is given
we have to check each no within limit is prime or not
each number = for i in range(2,num):
    so that i is to be checked is it divided by any number less than it'''
for i in range(1,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
