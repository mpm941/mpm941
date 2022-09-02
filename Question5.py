def area(t): #function for defining the area of a circle
    area_of_circle=3.14*(t)**2 #formula for finding area of the circle
    print("Area of Circle is %s mts^2" % area_of_circle)
def cir(t): #defining circumference of function
    circum_of_circle=2*3.14*(t) #formula for finding Circumference
    print("Circumference of a circle is %s mts" % circum_of_circle)
radius=30
area(radius) #Calling area function to find area
cir(radius) #Calling Cir function to caluculate circumference
while(True):
    r=float(input("enter  radius"))
    if(r>0):
        area(r) #Calling area function to find area
        cir(r) #Calling Cir function to caluculate circumference
    elif(r<0):
        print("enter positive radius of circle")
    else:
        print("enter non-zero Value of the radius")