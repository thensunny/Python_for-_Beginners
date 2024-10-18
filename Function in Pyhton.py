#Block of satements that perform a specific task.
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# In Python a function is defined using the "def"( function defining) keyword:
# We will use function for discrease the redandency in the code.
def my_function():
  print("Hello from a function")

my_function()  # Function ta jekhane sekhane call kore use kora jabe
               #Peranthesis er vitore ami input dibo
#Example:
def calc_sum(a,b):  # Here We built a function
    sum=a+b
    print(sum)
    return sum
calc_sum(5,10)

# after writing lots of line code then you can agin can the function anytime.
calc_sum(23,17)
calc_sum(45,56) #Here we called the function 3 times.

#The return statement is used to exit a function and optionally pass a value back to the caller.
#Syntax:
# def function_name(parameters):
#   # Function body
#   return value
#function defination
def calc_sum(a,b): #Perameters
    return a+b
sum=calc_sum(1,3) #vfunctions call; ( here a,b) is Argument
print(sum)

# print_hello called by 3 times
def print_hello():
    print("Hello")

print_hello()
print_hello()
print_hello()

# Make a function : average of 3 numbers

def average(a, b, c):
  return (a + b + c) / 3


avg = average(50, 45, 70)
print(avg)

avg = average(60, 57, 76)
print(avg)

avg = average(48, 80, 50)
print(avg)


# 2 types of function in python:
# 1. Built-in-functions,           2. User defined Functions ( It will be written by programmer)
 #print(),len(),type(),range()