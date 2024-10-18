# Dictonaries are used to store data values in "key"value" pairs.
#They are unorderd, mutable(changeable)& don't allow duplicate key.
# key:value
# Strings, Dist, Tuple they have one common thing that is "Index"/ Like : they start with 0,1,2,3,4,5......

# For example sotring some Information
info={
    "name":"SunnyProject",
    "subjects": ["python","C","Java"],
    "Topics": ("dict","Set"),
    "age":35,
    "is_adult": True,
    "Makrs": 94.4
}
print(type(info))
print(info)
# If we want to print individually any key. We can do it
print(info["name"])
print(info["Topics"])
#print(info["Marks"])

""" Nested Dictonary """
  # if else condition er vitor jemon if else condition thakte pare same vabe dictonaryr vitor dictonary creat kora jaai jetake amra nasted dictonary boli.
  #Ekhane amra aldha aladha sob portion printed korte paro. Here is the example:

student = {
    "name": "Asif Khan ",
    "Subjects": {
        "phy": 97,
        "Chem": 87,
        "math": 90
    }
}

print(student)
print(student["Subjects"]["math"])

#Dictonary Methodes
"""
myDict.keys() #returns all key
myDict.values() #return all values
myDict.items() #returns all (key, val) pairs as tuples
 myDict.get("key") #retuen the key according the value 
 myDict.update({newDict") #inserts the specified items to the dictionaries . update key and value 
 


"""
student.update({"City":"Chittagong"})
print(student)
