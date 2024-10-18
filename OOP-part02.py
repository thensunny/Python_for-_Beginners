#** del Keyword **#
# Used to delete object properties or object itself.
#                del s1.name
#                del s1

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Sunny")
del s1.name
print(s1.name)  #print hocche na karon s1 object delete hoie geche shate taar attributes o delete
                 # hoie geche

                           #** Private(like) attributes and methods **#
#Conceptual Implementations in Python
#Private attributes and methods are meant to be used only within the class and are nit accessible \
#from outside the class.

#Public
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass #Ekhane class ta public karon ekahne amra class er baire er data
        # use korte partesi.

acc1=Account("12354","abc123")
print(acc1.acc_no)
print(acc1.acc_pass)  #We can access

#Private
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Ekhane class ta 2ta (__) underscore lagiye private kore
        # nilam. Ekhn r baire theke access kora jabe na.
    def rest_pass(self):
        print(self.__acc_pass)



acc1 = Account("12354", "abc123")
print(acc1.acc_no)
#print(acc1.__acc_pass)  #Eita run korle error asbe karon ota class er vitor
print(acc1.__acc_pass()) # Eita class er bairer attributes k call kortese

                                   # Inheritance #
#when one class (child class/derived) derivers the properties and methods of another class(
# parent class/base class).
#class Car:            # parent class
                  #Ekhane parent class er kichu propertis j gula child class e common thakte pare,
                 # se gula amra r child class e likhbo na. amra oi logic k parent class theke child
                # class e inherit kore felbo.

#class ToyotaCar(Car):  # Ekhane amra parent class theke method inherit kore felchi

class Car:
    @staticmethod
    def start():
        print("car started ..")

    @staticmethod
    def stop():
        print("car stopped")    #Etotuk porjonto parent class

# Then ekhan theke child class start.
class ToyotaCar(Car):  # Ekhane Toyota hocche class r niche car1 and car2 hocche er object.
    def __init__(self, name):  # constructor
        self.name = name


car1 = ToyotaCar("Fortuner")  #car1 and car2 holo ToyotaCar class er object
car2 = ToyotaCar("Prius")

print(car1.start)  # Eiti chilo single inheritance

# There are 3 types of Inheritance availble :  1. Single Inheritance
                                             # 2. Multi-level Inheritance
                                           #   3. Multiple inheritance

   ## --> Multi-level Inheritance
class Car:
    @staticmethod
    def start():
        print("car started ..")

    @staticmethod
    def stop():
        print("car stopped")    #Etotuk porjonto parent class

# Then ekhan theke child class start.
class ToyotaCar(Car):  # Ekhane Toyota hocche class r niche car1 and car2 hocche er object.
    def __init__(self, brand):  # constructor
        self.name = brand

class Prius(ToyotaCar):        # Eita k grand child o bolte pari
    def __init__(self,type):  #Type : Diesel, petrol, CNG, LPG, Electric..?
        self.type=type

car1= Prius("LPG")
car1.stop()
car1.start()

                              # ------> Multiple inheritance
# Ekhane 2 ba taar odhik parent class thakte pare, sekhan theke child class properties inherit kore.
class A:
    varA= "welcome to class A"

class B:
    varB="welcome to class B"
class C(A,B): # Here Child class is C, but here "C" inherit the Class "A" and "B". Then printed
    # successfully.
    varC= "welcome to class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
                                    #* Super Method *#

#Super() method is used to access methods of the parent class.

                                     #Class Methode
#A class methode is a bound to the class and receives the class as an implicit first argument.
#Note: static methode can not access or modify class state and generally for utility.

class Studnet:
    @classmethod # decoreator
    def college(cls):
        pass

class Person:
    name="anonymous"

    def changeName(self,name):
        Person.name=name  #class er vitor attributes change kora jai eivabe (Persion.name)
        # #1st method
        #self.__class__.name="Tofa"  #2nd method
p1=Person()
p1.changeName("Tofa khanam")
print(p1.name)
print(Person.name)

                              # Property Decoretors
#We use @property decorator on any method in the class to use the method as a property.
class Student:
    def __init__(self,phy,chem,math):
        self.phy= phy
        self.chem=chem
        self.math=math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+"%"

stu1= Student(87,67,90)
print(stu1.percentage)

stu1.phy=86
print(stu1.percentage)

                             #Polymorphism: operator Overloading
#When the same operator is allowed to have different meaning according to the context.
#The word polymorphism means having many forms. In simple words, we can define polymorphism as the ability of a message to be displayed in more than one form. Real life example of polymorphism, a person at the same time can have different characteristic. Like a man at the same time is a father, a husband, an employee.
#Operators  & Dunder functions:
#a+b      #addition        a.__add__(b)
#a-b     #subtraction      b.__sub__(b)
#a*b     #multiplication   a.__mul__(b)
#a/b     #division         a.__truediv____(b)
#a%b     #addition         a.__mod____(b)
# a>b   # Gater than less than.  __get__

print(1+2) # For numbers it's - addition
print("Asif"+"Khan") #For string it's - concatenation
print([1,2,3]+[4,5,6]) #For list it's - merge
pass
# Ekhane operator "+" ek ek jaigai ek ek rokom role play kortese. etake bole Polymorphism operator Overloading.

#Complex number: Complex numbers combine regular numbers with imaginary ones.
              # example:  2i + 3j / Here, 2,3 is real part & i,j is imaginary part.
# real number : 0 1 2 3 4 5 6 7 8 9
#For Complex Number:

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):  # this function create for Dunder Function
        newReal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newReal, newimg)


num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()
# ekhn ei 2 ta complex numbers addition korte amader use korte hobe Dunder function.
# Dunder Function: How to use
num3 = num1 + num2  # er jonno upore ekta function create korte hobe.
num2.showNumber()












