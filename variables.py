# A Variable is a name given to a memory location in a Program.

name =("Sunny") # Here Sunny is string. In double quotation everything is string.
age = (24)
price = 25.99
print (name, age, price)
print("My name is :",name) # Without double quotation it will be consider as a Variable.
print("My Age is :",age)

#DataType
print(type(name))
print(type(age))
print(type(price))

# Boolean and None Datatype
age = 24
old = True # First letter should be Capital
a = None
print (type(old))
print(type(a))

#Print Sum
a=2
b=5
sum = a+b
print(sum)

#Expression Execution
# String & Numeric values can operate together with *
A,B =2,3
Txt ="#"
print (A*Txt*B)
#String & String can operate with +
A,B="2",3
Txt="#"
print ((A+Txt)*B)
#Numeric values can operate with all arithmetic operations
A,B=2,3
C=4
print(A+B*C) #first Multipy then sum
#Arithmetic expression with integer and float will result in float
A,B= 10,5.0
C=A*B
print(C)
#Result of division operator with two integers will be float
A,B=1,2
C=A/B
print(C)
#Integer division with float and int will give int displayed as float
A,B=1.5,3
C=A//B
print(C,A/B)
#Floor gives closest integer, which is lesser than or equal to the float value Result of (A//B) is sa,e as floor (A/B)
A,B= 12,5
C = A//B
print (C)

A,B= -12,5
C = A//B
print (C)

A,B= 12,-5
C = A//B
print (C)
# Reminder is negative when denominator is negative
# we know (+ +)= +, (- -)= +,(+ -)= -,(- +)= +
A,B= -5,2
C= A%B
print (C)

A,B= 5,2
C= A%B
print (C)

A,B= 5,-2
C= A%B
print (C)

A,B= -5,-2
C= A%B
print (C)
#Comments in Python
#This is signle line comment
"""Three time double quotation for long comments"""
#print ("Hello")  -> Won't be printed
print ("world")    # Will be Printed

""" Input in Python """
#input() statement is used to accept values (using keyboard) from user

#string input
name=input ("name : ")
print (name)
#int input
age = int (input("age : "))
#Float input
price = float(input("price: "))
#print'("My name is" :, name, "and My age is", age)




