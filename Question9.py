N=int(input("Enter number of Students"))
if(N>0): #checking for the condition that number of students are greater than 0
    w_kg=[]
    for i in range(0,N): #running for loop from 0 to n i.e no of students
        lb=float(input("enter weight in lbs")) #taking input of weights in lbs
        kg=lb*0.454 #converting lb to kgs
        w_kg.append(kg) #appending into w_kg list

else:
    print("enter the Number of students in Positive and non zero value")
print(w_kg)
