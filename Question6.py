str="I am a teacher and I love to inspire and teach people"
print(type(str)) #using type() function to get the data type
y=str.split() #using split function to get every word
print(y)
set_str=set(y) #adding split words into set
print(set_str)
print("no:- of unique words in given sentence is %s" % len(set_str)) #as set doesn't take duplicate keys we can directly find the length