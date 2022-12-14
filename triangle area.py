import cmath
a=int(input("enter first number="))
b=int(input("enter second number="))
c=int(input("enter thard number="))
        
if (a+b)>c and (b+c)>a and(c+a)>b:
        s=(a+b+c)/2
        area=cmath.sqrt(s*(s-a)*(s-b)*(s-c))
        print("triangle area is =",area)
else:
        print("triangle is not possible")
