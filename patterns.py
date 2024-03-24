rows = int(input())

print("right angle stars")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("\ninverted right angle stars")
for i in range(rows):
    for j in range(rows-i):
        print("*",end=" ")
    print()

print("\nhalf diamond") #right angle triangle + inverted right angle triangle
for i in range(1,rows+1):
    for j in range(1,i+1):
         print("*",end=" ")
    print()
for i in range(rows):
    for j in range(rows-i-1):
         print("*",end=" ")
    print()

print("\ntriangle pyramid")
for i in range(rows):
    for j in range(rows-i):
          print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()

print("\ninverted triangle pyramid")
for i in range(rows):
    for j in range(i+1):
          print(" ",end="")
    for k in range(rows-i):
        print("*",end=" ")
    print()

print("\nFull diamond") #full triangle + inverted triangle
for i in range(rows):
    for j in range(rows-i):
          print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,rows):
    for j in range(i+1):
          print(" ",end="")
    for k in range(rows-i):
        print("*",end=" ")
    print()

print("\nright angle numbers row wise")
k=0
for i in range(1,rows+1):
    for j in range(1,i+1):
        k=k+1
        print(k,end=" ")
    print()


print("\nright angle numbers col wise")
for i in range(1,rows+1):
    print(i,end=" ")
    k=1
    for j in range(1,i):
        if j == 1:
            inc = i+(rows-k)
        else:
            inc = inc + (rows-k)
        
        k=k+1

        print(inc,end=" ")

    print()

print("\ninverted right angle numbers")
k=0
for i in range(rows):
    for j in range(rows-i):
        k=k+1
        print(k,end=" ")
    print()


print("\nright angle number's square")
k=0
for i in range(1,rows+1):
    for j in range(1,i+1):
        k=k+1
        print(k**2,end=" ")
    print()

print("\nright angle ASCII")
k=65
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()

print("\ntriangle even")
k = 0
for i in range(rows):
    for j in range(rows-i):
         print(" ",end="")
    for l in range(i+1):
        k=k+2
        print(k,end=" ")
    print()


print("\nrow col *")
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==j:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()

  
print("\ninverted row col *")
for i in range(1,rows+1):
    for j in range(rows,0,-1):
        if i==j:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()

print("\nRectangle")
for i in range(1, rows+1) :
	for j in range(1, rows+1) :
		if (i == 1 or i == rows or
			j == 1 or j == rows) :
			print("*", end="")		
		else :
			print(" ", end="")		
	print()

print("char I")
for i in range(1,11):
    if i==1 or i==10:
        print("* "*10)
        continue
    for j in range(1,(20//2)+1):
        if j==20//2:
            print("*")
        else:
            print(" ",end="")

print("pyramid of isosceles triangle of desired cases")
for _ in range(int(input())):
    x = int(input())
    l=1
    for i in range(x):
        for j in range(x-i):
            print(" ",end=" ")
        for k in range(l):
            print("*",end=" ")
        l=l+2
        print()