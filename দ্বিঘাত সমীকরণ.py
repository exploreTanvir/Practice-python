import math
a=int(input("Enter the value of first number : "))
b=int(input("Enter the value of second number : "))
c=int(input("Enter the value of third number : "))
d=(b*b)-(4*a*c);
if d==0:
    x=-b/(2*a)
    print("The ans is : ",x)

elif (d>0):
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b+math.sqrt(d))/2*a
    print("The ans is :",x1,"\nAnd the another ans is",x2)
else:
    print("The roots are imaginary")
