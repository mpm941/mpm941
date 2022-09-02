dog ={"name":"Charlie","color":"brown","breed": "Labrador","legs": 4,"age": 2}
print(dog) # Dog Dictonary
student={"first_name":"Prudhvi Mahesh","last_name": "Meka","Gender":"Male","Age":26,"marital status":"Single","skills":"CAD","Country":"INDIA","City":"Palacole","Address":"3-64, Near Panchayathi Ofc, West Godavari Dist, Andhra Pradesh-534268"}
print(student) # Student Dictionary
print(len(student)) #length of the student dictonary
print ("Value : %s" %  student.get('skills'))
print(type(student.get('skills')))
def val_append(dict_obj, key, value):
    if key in student:
        if not isinstance(student[key], list):
            # converting key to list type
            student[key] = [student[key]]
 # Append the key's value in list
            student[key].append(value)
# calling the function to append values
val_append(student, 'skills', 'python')
print('after adding value to dictionary =\n',student)
keys_list=list(student.keys())
print(keys_list)
values_list=list(student.values())
print(values_list)