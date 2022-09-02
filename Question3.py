sisters_tuple=("PAVANI","PRIYA","VARSHA") #Creating a tuple for sisters
print(sisters_tuple)
brothers_tuple=("JAYANTH","UDAY","SAINATH","RAHUL") #Creating a tuple for brothers
print(brothers_tuple)
sibblings_tuple=sisters_tuple+brothers_tuple  #using addition operator to join both tuples.
print(sibblings_tuple)
print("No:- of sibblings :",+len(sibblings_tuple)) #finding the length of the tuple using len() method
sibblings_tuple+=("Mahi","rocky") #appending tuple with father name and mother name
print(sibblings_tuple)
family_members=sibblings_tuple #modifying sibblings_tuple to Family_members
print(family_members)
