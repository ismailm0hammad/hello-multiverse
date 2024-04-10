# Friendly Pair Numbers
# The numbers whose ( sum of divisors ) / number ratio is same are known as Friendly Pair Numbers.
# Let's try and understand it better using an example

# Example
# Input : 6 28
# Output : Yes, they are a friendly pair
# Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
# Now the sum of factors of both the numbers are 6 and 28 respectively. 
# When we divide the sums with the numbers we get 1 and 1 respectively. 
# As the ratio of both the number match, they are considered as a friendly pair

num1=int(input("Enter the number:"))
num2=int(input("Enter the number:"))
def sumfactor(n):
    sum=1
    for i in range(2,n):
        if n%i== 0:
            sum = sum + i
    return sum 
a=sumfactor(num1)
    
b=sumfactor(num2) 
if a/num1 == b/num2 :
    print("It is the friendly pair")
else:
    print("It is not the friendly pair")