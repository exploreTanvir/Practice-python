num=int(input("Enter your number : "))

if num%2==0 and num%3==0:
    print(num,"is divided by 2 and 3")
elif num%2==0:
    print(num,"is divided by 2 and not divided by 3")
elif num%3==0:
    print(num,"is divided by 3 and not divided by 2")
else:
    print(num,"is not divided by 2 and 3")
