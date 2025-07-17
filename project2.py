"""Write a program to swap to numbers
there are two meths to do that 1) is by using temporary number and another is directly"""


#1st METHOD
print("THE 1ST(FIRST) METHOD OF SWAPPING NUMBERS")
x=12
y=13
print ("value of x is:",x)
print ("value of y is:",y)
temp=x
x=y
y=temp
print ("After swaping the number value of Y is:",y)
print ("value of x is:",x)
print ("value of y is:",y)

#2st METHOD
print("THE 2ND(SECOND) METHOD OF SWAPPING NUMBERS")
a=30
b=40
print("the value of A is:",a)
print("the value of B is:",b)

a,b=b,a

print("After swaping the numbers of A and B")
print("the value of A is:",a)
print("the value of B is:",b)
