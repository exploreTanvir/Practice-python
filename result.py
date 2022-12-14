mark=int(input("enter your mark : "))
if mark>=80 and mark<=100:
    print("the result is A+" )
elif mark>=70 and mark<80:
    print("the result is A")

elif mark>=60 and mark<70:
    print("the result is B")
elif mark>=50 and mark<60:
    print("the result is C")
elif mark>=40 and mark<50:
    print("the result is D")
elif mark>100 or mark<0:
    print("mark is not defined")
else:
    print("the result is fail")
