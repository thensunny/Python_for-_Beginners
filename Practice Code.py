
# Write a program to input 2 numbers & print their sum.
a=int(input("Enter the Number: "))
b=int(input("Enter the Number: "))
sum=(a+b)
print("sum =", sum)

#Write a program (WAP) to input side of a square & print its area.
side=float(input("Enter the square side : "))
print ("area=", side**2)

# WAP to input 2 floating point numbers & print their average.
First=float(input("Enter the Number:"))
Second=float(input("Enter the Number:"))
average= (First+Second)/2
print(" Their Average : ", average)

# WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False.
#First Methode
a=int(input("Enter the Number:"))
b=int(input("Enter the Number:"))

if(a>=b):
    print("True")
else:
    print("False")
    #2nd Methode  ( Don't need to use  Conditional Operator because it has logical operator. It will be by default showing the True False.
a=int(input("Enter the Number:"))
b=int(input("Enter the Number:"))

print(a>=b)

#WAP to input user's first name & print it's length
a=input("Enter Your First Name: ")
print(len(a))

#WAP ro find the occurrence of '$' in a String. "Occurrence means "Count"
str= " This Cycle's price is $45 but I can ask him for $28"
print(str.count("$"))

#WAP to check if a number entered by the user is odd or even
num=int(input("Enter the Number: "))
if(num%2==0):
    print("The number is Even")
else:
    print("The number is Odd")

# WAP to find the largest of 3 numbers entered by the user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1>= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
   print("The largest number is", largest)

   #2nd Methode of this code
   a = int(input("Enter the first number : "))
   b = int(input("Enter the second number : "))
   c = int(input("Enter the third number : "))
   if (a >= b and a >= c):
       print("First Number is Largest")
   elif (b >= c):
       print("Second Number is Largest")
   else:
       print("Third number is Largest")


#WAP to check if a number is a multiple of 7 or not
num=int(input("Enter the number: "))
if(num%7==0):
    print("The Number is a multiple of 7")
else:
    print("The number is not multiple of 7")

# WAP to ask the user to enter names of their 3 favorite movies & Store then in a list.
movies=[]  #First e ekta khali list nite hobe okhane rakhar jonno
mov1=input("Enter your first favorite Movie: ")
mov2=input("Enter your second favorite Movie: ")
mov3=input("Enter your third favorite Movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append (mov3)

print(movies)

#WAP to check if a list contains a palindrome of elements. (Hint:use copy() method)
list1=["m","a","a","m"]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("This is Palindrome")
else:
    print("This is not Palindrome")

# WAP to count the number of students with the "A" grade in the following tuple.
tup=("A","D","B","E","A","B","A")
print(tup.count("A"))

#Store the above values in a list  sort them from "A" to "D"
Grade=["A","D","B","C"]
Grade.sort()
print(Grade)

# Store following word meaning in a python dictionary:
#table: "a piece of furniture", "list of facts & figures"
#cat: "a small animal"

dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture","list of facts & figures"],

}
print(dictionary)

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classroom are needed by all students.
#"python","java","C++","python","javascript"
#"java","python","java","C++","C"

subjects = {
    "python", "java", "C++", "python", "JavaScript", "java", "python", "java", "C++", "C"
}
print(subjects)
print(len(subjects))  # Length joto classroom o totota hobe

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start eith an empty dictionary and add one by one. Use subject name as key and marks as value.

marks={}
x=int(input("Enter Phy marks : "))
marks.update({"Phy" :  x })
x=int(input("Enter Math marks : "))
marks.update({"Math" : x })
x=int(input("Enter English marks : "))
marks.update({"English" : x })
print(marks)

# Figure out a way to store 9 and 9.0 as separate values in the set. ( You can take help of built-in data types)
values={9,9.0}
print(values)

#Using builting data type
values={
    ("int",9),
    ("float",9.0)
}
print(values)

#print number 1 to 5
i=1
while i<=5:
    print(i)
    i+=1
print("Loops Ended")

#print number 5 to 1
i=5
while 1<=i:
    print(i)
    i-=1
print("Loops is Ended")

#Print numbers from 1 to 100.

i=1
while i<=100:
    print(i)
    i+=1
print("Loop is Ended")

#Print numbers form 100 to 1.
i=100
while i>=1:
    print(i)
    i-=1
print("The Reverse Loop is Ended")

#Print multiplication table of a number n.
n=int(input("Enter a number : "))
i=1
while i<=10:
    print(n*i)
    i+=1

# Print the elements of the following list using a loop:
# [1,4,9,25,36,49,64,81,100]
num=[1,4,9,16,25,36,49,64,81,100]
index=0
while index <= len(num)-1:
    print(num)
    index+=1
  # Here we are traverse in the list. Travers means kono set, tuples ba list e ek ek kore jawa.

# Search for a number x in this tuple using loop.
num=(1,4,9,16,25,36,49,64,81,100)
x=36   # You can get any number from the tuple for testing purpose.
i=0
while i< len(num):           # In this code we used Linear search for searching methode.
    if(num[i]==x):
        print("Found at index :", i )
    i+=1


# Unsing for & range()
#Print numbers from 1 to 100
for i in range(1,101):
    print(i)

#Print numbers from 100 to 1.
for i in range(100,0,-1):
    print(i)

#Print the multiplication table of a number n.
n=int(input("enter the number: "))
for i in range(1,11):
    print(n*i)

# WAP to find the sum of first n natural numbers. ( using while)
n = int(input("Enter the natural number: "))
sum = 0
i = 1  # Initialize a counter

while i <= n:
    sum += i
    i += 1
print("Total Sum:", sum)

# WAP to find the sum of first n natural numbers. ( Using For )
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("Total sum:", sum)

#WAP to find the factorial of first n  natural number. ( using while loop)
#Factorial of a non-negative integer n is the product of all positive integers less than or equal to n.**
# factorial of "n"= 1*2*3*4*......n.
n = int(input("Enter the natural number: "))
fact = 1
i = 1  # Initialize a counter

while i <= n:
    fact *= i
    i += 1
print("factorial:", fact)

#( using For loop)
n = int(input("Enter the natural number: "))
fact = 1
for i in range(1,n+1):
    fact *=i
print("factorial: ", fact)

# Write a function (WAF) to print the length of a list.(list in the parameter)
cities = ["Dhaka", "Chittagong", "Rangpur", "Khulna", "Rangamati"]
country = ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan"]

def print_len(list):
    return (len(list))

print(len(cities))
print(len(country))

#WAF to print the elements of a list in a single line.(list is the parameter)
cities = ["Dhaka", "Chittagong", "Rangpur", "Khulna", "Rangamati"]
country = ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan"]

def print_list(list):
    for item in  list:
        print(item,end=" ")

print_list(country)
print_list(cities)

#WAF to the find the factorial of n. ( n is the parameter)
def cal_fact(n): # Perenthesis er vitor always input dibo
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial", fact)

cal_fact(5)
cal_fact(2)
cal_fact(4)
cal_fact(6)

# WAF to convert USD to BDT
def converter(usd_val):
    bdt_val = usd_val * 94
    print (usd_val, "USD =", bdt_val,"BDT")

converter(50)

#WAF where give a input n then print it if "ODD" or "EVEN" as a string.
def get_num(n):
    if n % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

get_num(5)
get_num(6)

#Write a  recursive funcion to calculate the sum of fist n natural numbers.
def calc_sum(n):
    if(n == 0):
       return 0
    return calc_sum(n-1)+n
sum=calc_sum(5)
print(sum)

#Write a  recusive function to print all elements in a list.
#Hint: use list & index as if parameters:

numbers = [34, 65, 78, 98, 45, 66, 52]
cities = ["Dhaka", "Chittagong", "Rangpur", "Khulna", "Rangamati"]
country = ["Bangladesh", "India", "Pakistan", "Nepal", "Bhutan"]


def print_list(list, idx=0):
    if(idx == len(list)): #stopping conditon
        return
    print(list[idx])
    print_list(list, idx + 1)


print_list(country)
print_list(cities)
print_list(numbers)

# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# We are learning fil I/O
# Using java
# I like programming in java.

with open("practice.txt","w") as f:
    f.write("Hi everyone\nWe are learning fil I/O")
    f.write("Using java\nI like programming in Java.")

#WAF that replaces all accurrences of java with python in above file.
with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

# Search if the word "learning" exists in the file or not.
word="learning"
with open("practice.txt","r")as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("not found")

        # Using function
    def check_for_word(n):
        with open("practice.txt", "r") as f:
            data = f.read()
            if (data.find(n) != -1):
                print("Found")
            else:
                print("not found")

    check_for_word("python")

# WAF to find in which line of the file does the word "learning" occur first.
#Print-1 if not found.
def check_for_word():
     word = "xlearning"
     with open("practice.txt", "r") as f:
            data = f.read()
            if(word in data):
                print("Found")
            else:
                print("not found")

def check_for_line():
    word="learning"
    data= True
    line_no=1
    with open("prectice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
print(check_for_line())

#From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("practice.txt","r") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    for val in nums:
        if (int(val)%2 == 0):
            count+=1
print(count)

#Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self,name,marks):  #Construcktor # ekhane name marks call kore input nite parbo
        self.name=name
        self.marks=marks

    def get_avg(self):        #def used for create a function
        sum=0
        for val in marks:
            sum+= val
        print("hi",self.name, "Your average score is :", sum/3)
s1 = Student("Asif Khan",[99,67,87])
s1.get_avg()

# Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit and printing  the balance.

class Account:                  # Here we create a class. This 4 line is class stuff
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    #debit method
    def debit(self,amount):
        self.balance=-amount
        print("Tk",amount,"was debited")
    #credit method
    def credit(self,amount):
        self.balance=+amount
        print("Tk",amount,"ws credited")
    def get_balance(self):
        return self.balance

acc1= Account(25000,1602)        #This 3 lines is object of class
print(acc1.balance)
print(acc1.account_no)

#QS: Define a Circle class to create a circle with radius r using the constructor.
#   Define an Area() method of the class which calculates the area of the circle.
#   Define a Perameter() method of the class which allows you to calculate the perimeter of the
#   circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2* (22/7)* self.radius ** 2

c1= Circle(21)
print(c1.area())
print(c1.perimeter)

#Qs: Define a Employee class with attributes role, department and salary. This class also has a
# showDetails() method.
#Create an Engineer class that inherits properties from Employee and has additional attributes:
# name & age.

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
class Engineer(Employee):             # Ekhane parent class k inherit korechi
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Enginner","IT","142000") #Super() method is used to access methods of
        # the parent class.

# e1 = Employee("Accountant","Finance","60,000")
# e1.showDetails()
engg1=Engineer("Masud Rana","43")
engg1.showDetails()

#QS: Create a class called Order which stores item and its price.
# use dunder function __gt__() convey that:
#  order1>order2> if price of order 1> price of order 2.

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self, odr2):              # Here We used dunder function.
        return self.price>odr2.price

odr1=Order("chips",80)
odr2=Order("coffee",40)

print(odr1 > odr2)

                                       #Guess the Number
import random # Pythn er moddhe ekta inbuild random module thake. Random value, character nite
# eita use kora hy.ei function a theke b range er value nei.
ranNum = random.randint(1,5)
print(ranNum)
pass

##################
import  random
val=random.choice(['a','b',1,2,3])  # Random Choice amader ek ek bar vinno vinno value print kore
# dei. list er theke  value gula theke.
print(val)
pass

##############
import  random
import string # Eita use kore print korle small and capital letter er a theke z porjonto print hobe.
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
pass



