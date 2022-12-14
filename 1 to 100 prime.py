count=0
for n in range (2,101):
       if n > 0 :
        for i in range (2,n):
            if (n%i==0):
                break
        else:
            count+=1
            print(n)
else:
    print("1 to 100 total prime number is :-",count)
