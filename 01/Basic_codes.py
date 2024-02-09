# Method 1 (+) operator#
num1=int(input("enter value"))
num2=int(input("enter value"))
add=num1+num2
print(add)

# Method 2 user imput#
num1=int(input("enter value"))
num2=int(input("enter value"))
add=int(num1)+int(num2)
print(add)

# Method 3 using function#
def add(a,b):
    return a+b
num1=int(input("enter value"))
num2=int(input("enter value"))
sum=add(num1,num2)
print(sum)  ##print(add(num1,num2))

# Method 4 using operator.add() #
num1=int(input("enter value"))
num2=int(input("enter value"))
import operator
sum=operator.add(num1,num2)
print(sum)
#Method 5 using #






# Pattern Print #
a=int(input("enter value"))
for x in range (a):
    for y in range(x+1):
        print("*",end=" ")
    print()

# Reverse the array Method 1 #
a=[1,2,3,4,5,6]
for x in range(len(a)):
    print(a[-(x+1)],end=" ")

# Reverse the array Method 2 #
a=[1,2,3,4,5,6]
a.reverse()
print(a)

# Reverse the array Method 3 #
a=[1,2,3,4,5,6]
b=len(a)
start, end= 0,b
for x in range (b//2):
    temp=a[x]
    a[x]=a[end-1-x]
    a[end-1-x]=temp
print(a)