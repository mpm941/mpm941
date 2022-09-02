import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]  #initialisation of list
ages.sort() #function for sorting
print(ages)
m=min(ages) #function for finding minimum of the ages
n=max(ages) #function for finding minimum of the ages
ages.append(m) #function for appending minimum of the ages
ages.append(n) #function for appending minimum of the ages
print(ages)
print("Median of Ages is %s:"% statistics.median(ages)) #function for finding median of the ages
print("Average of Ages is %s" % statistics.mean(ages)) #function for finding average of the ages
range=n-m
print("range of ages is %s" %range) #Printing range of the ages
