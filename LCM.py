num_one=int(input("Enter your first number :"))
num_two=int(input("Enter your second number :"))
num_three=int(input("Enter your third number :"))
if num_one>num_two:
    h=num_one
elif num_one>num_three:
    h=num_two
else:
    h=num_three
while True:
    if h%num_one==0 and h%num_two==0 and h%num_three==0:
        break
    h+=1
print("LCM is ",h)
