# Taking the input form the user, after code execuation

# Here We take the input
input("Enter Your name : ")
#Here yow store the input and then print this store value
name=input("Enter Your name : ")
print("Welcome ", name)

# When we take any input from user, It always consider as a "String".
val = input("Enter the Value : ")
print(type(val), val)

#Here we type casting to Integer
val = int(input("Enter the Value : "))
print(type(val), val)

#Applying Type casting in diffrent line
name =input("Enter the Name :")
age = int(input("Enter the Age :"))
marks = float(input("Enter the Marks :"))

print("Welcome", name)
print("your age is",age)
print ("Your marks is", marks)