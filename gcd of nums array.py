# GCD of more than two (or array) numbers
# This function implements the Euclidean 
# algorithm to find H.C.F. of two number
 
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
 
    return x
     
     
l = list(map(int,input().split()))
 
num1=l[0]
num2=l[1]
gcd=find_gcd(num1,num2)
 
for i in range(2,len(l)):
    gcd=find_gcd(gcd,l[i])
     
print(gcd)