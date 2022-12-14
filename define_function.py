#learn dictionary
my_dict={"name":"tanvir","roll":532987,"department":"computer"}
print(my_dict["name"])
print(my_dict["roll"])
print(my_dict["department"])



#dictionary updatint
my_dict={"name":"tanvir","roll":532987}
my_dict["department"]="computer"
print(my_dict)



#delating dictionary item
squres={10:20,30:40,50:60}
print(squres.pop(30))
print(squres.popitem())
print(squres)



print(max(5,40,50))


import math
print(math.sqrt(9))



#define function
def add(x,y):
    return(x*y)
print(add(5,10))


def tanvir(x,y):
    return(x+y)
print(tanvir(5,10))
print(tanvir(15,15))
print(tanvir(10,10))


def area():
    lenth=int(input("Enter your lenth : "))
    width=int(input("Enter your width : "))
    rectangle_area=lenth*width
    print("Your rectengle area is ",rectangle_area)
area()

print(add(5,100))



print(round(3.72))


