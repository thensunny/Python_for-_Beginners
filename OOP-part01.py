#To map with real world scenarios, we started using object in code.
# This is called Object oriented programming

#Procedural -> functional ->  Object oriented programming
#Normal code -> functional redundancy komai r reusability barai -> oop  er theke advance

# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
#Class is a blueprint for creating objects

#Create a class named Student, with a property named "name":
class Studnet:  #class er name amra capital letter diye start kori
  name = "Asif Khan"
#Create an object named s1, and print the value of Student:
s1=Studnet()
print(s1.name)

s2=Studnet()
print(s2.name)

# We have factory where I do produce car.
class Car:
    color ="Blue"
    brand = "BMW"
car1=Car()
print(car1.color)
print(car1.brand)

                             # """Constructor""" Or __init__() Function #
#All classes have a function called _init-(), which is always executed when the class is being initiated.
#Constructors are generally used for instantiating (represent as) an object.
class Studnet:
  name = "Asif Khan"
  def __init__(self):  # nicher s1 er location r self er location same.
      print("Adding new studnet in Database..")
s1=Studnet()


                        # Class and Instance Attributes #
# Class.att
# obj.attr

class Student:
    college_name = "Sunny College"  # ekhane college_name holo class attribute

    def __init__(self, name, marks):
        self.name = name  # Object attributes
        self.marks = marks
        print("Adding new student in Database...") # Eita nicher s1 and s2 2tar jonnoi use hobe.


s1 = Student("Asif", 94)
print(s1.name)
print(s1.marks)

s2 = Student("Sunny", "97")
print(s2.name)
print(s2.marks)

#Object attributes are get higher preference than class attributes. ei 2ta attributes jodi same thake tokhon aobject attributes heigher preference paai.

                                      # Methods #
#Methods are functions that belongs to object.
#Class er vitor amra j function ta likhbo otai method naam daka hy class e
#Class is a collections of 2 things :  1. data (attributies) 2. Methods

class Student:
    college_name = "Sunny College"  # ekhane college_name holo class attribute

    def __init__(self, name, marks):
        self.name = name  # Object attributes
        self.marks = marks
    def welcome(self):
        print("Welcome Student")



s1 = Student("Asif", 94)
print(s1.name)
print(s1.marks)

                                    ### Static Methods ###
#A static method is a method that belongs to a class but doesn't require an instance of the class to be called.
#methods that don't use the self parameter( work at class level)
class Student:
    @staticmethod #decorator
    def college():
        print("ABC College")
#Decorators allow us to wrap another function in order to extend the behavior of the wrapped
# function,
# without permanently modifying it.

                                #*** Important ***# ( 4 pillers of OOP)
           # 1. Absatraction 2. Encapsulation 3. Inheritance 4.Polymoophism
#1.Absatraction : Hiding the implementation details of a class and only showing the essential
# features to the user.
    # Here unneccesery features are hiding from users, only important features will shown.
   #  Example:
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):         #This 4 line is unecessery
        self.clutch = True
        self.acc = True
        print("Car is started")

car1=Car()
car1.start()
                                       #** Encapsulation **#
#Encapsulation : Wrapping data and functions into a single unit (Which is object)
#Encapsulation is a fundamental object-oriented principle in Python. It protects your
# classes from accidental changes or deletions and promotes code reusability and maintainability.
