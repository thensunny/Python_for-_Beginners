#A build-in data type that stores set of values. It like array in Python.
#It can store elements of different types (integer, float, string, etc)
#marks = [67,56,87,70,80]
# Strings --> Immutable ( We can not change) Only access
# List --> Mutable ( We can change) We can Do Access and change

#It hard to do in individually
marks1= 94.4
marks2= 87.4
makrks3=56.4
marks4=67.8
marks5=78.76

#So we can use using List
marks = [94.4, 87.4, 56.4, 67.8,78.76]
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])
print(len(marks))

#

student = [ "Sunny", 95.6, 17, "Chittagong"]
print(student)

# Mutable List
student = [ "Sunny", 95.6, 17, "Chittagong"]
print(student)
student[0]= "Asif"  #Sunny k mute kore Asif replace korchi, jeta string e kora possible na.
print(student)

# Immutable List
"""str="Asif"
print(str[0])
str[0]="T"  """  """ It Will be show the Error"""

#List Slicing
marks=[65,78,56,90,8]
print(marks[2:4])

#List Methodes
list=[2,1,3]
""" 
list.append(4) #adds one element at the end. [2,1,3,4]
list.sort() #Sorts in ascending order [1,2,3]
list.sort(reverse=True) #Sorts in decending order [3,2,1]
list.reverse() #reverse list [3,1,2]
list.insert(idx,el) #Insert elements at index
list.remove(1) #remove first occurrence of element [2,3,1]
list.pop(idx) #remove element at idx

"""
marks=[65,78,56,90,8]
marks.append(80)
print(marks)

marks=[65,78,56,90,8]
marks.sort()
print(marks)

list=["Orange", "Banana", "Apple", ]
list.sort()
print(list)

list=[32,12,56,32,43,78]
list.remove(32)    #First
print(list)