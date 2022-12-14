mark=int(input("Enter your marks :-"))
if mark>=80 and mark<=100:
    print("The GPA is 4.00")
elif mark>=70 and mark<80:
    print("The GPA is 3.50")
elif mark>=60 and mark<70:
    print("The GPA is 3.00")
elif mark>=50 and mark<60:
    print("The GPA is 2.50")
elif mark>=40 and mark<50:
    print("The GPA is 2.00")
else:
    print("You are fail")
