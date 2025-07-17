"""1. WRITE A PROGRAM TO CREATE A AREA CALCULATOR"""

print("LETS FIND YOUR AREA WITH AREA CALCULATOR")
print(""" press 1 to get the area of circle
press 2 to get the area of square
press 3 to get the area of rectangle
press 4 to get the area of triangle""")

choice=int(input("enter numbers between 1-4:"))
if choice==1:
    radius=float(input("enter radius:"))
    area=((22/7)*(radius**2))
    print("The area of circle is ",area)

elif choice==2:
    side=float(input("enter side:"))
    area=(side**2)
    print("The area of square is ",area)

elif choice==3:
    length=float(input("enter length:"))
    width=float(input("enter width:"))
    area= length*width
    print("The area of rectangle is ",area)

elif choice==4:
    base=float(input("enter base:"))
    height=float(input("enter height:"))
    area= 0.5*base*height
    print("The area of triangle is ",area)

else:
    print("its and invalid input")



