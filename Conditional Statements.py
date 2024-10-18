
#if-elif-else(SYNTAX)
""" if (condition):
        (4 space) then write ( Indentation or Proper spacing is most important thing in Python.
        Statement1
    elif(condition): (Here elif and else should be stay in same line like before "if" )
         (4 space) then write
        Statement2 (Here statement2 should be stay in same line like before "statement2" )
    else:
        Statement
           """
""" Example 1 : Traffic Light
              3 Colors Red -> Stop
                       Green-> Go
                       Yellow-> Look
                       Blue, White -> Light Broken 
 """

light = input("Light Color : ")
if(light=="Red"):
     print("Stop")
elif(light=="Yellow"):
     print("Look")
elif (light=="Green"):
     print("Go")
else:
     print("Light is Broken")

     """ Example 2 : Grades of Students """
'''marks = input("marks : ")
if(marks >= 90):
     print("A+")
elif(marks >= 80 and marks < 90):
     print("B")
elif(marks >= 70 and marks < 80):
     print("C")
else:
     print("D") This Code shows Error. Correct one is given bellow'''

marks_input = input("marks : ")

# Convert the input to an integer
marks = int(marks_input)

if marks >= 90:
    print("A+")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
else:
    print("D")
""" Single line if/ Ternary Operator """
# <var>=<var1> if <condition>else<var2>  Way Number 1
food = input("food : ")
eat = "yes" if food =="cake" else "no"
print (eat)
#Way Number 2
# <stt1>if<condition>else<stt2>
food=input("Food: ")
print("Sweet")if food=="cake" or food=="Laddu" else"Not sweet"

''' Clever if / Ternary Operator'''
# <var>(false_val, true_val) [<condition>] - this is square bracket
age=int(input("Age: "))
vote=("Yes", "No") [age<18]
print(vote)

# age condition for driving and Vote
age=int(input("Enter Your age"))
if(age>=18):
    print("You can drive")
    print("You can Vote")
else:
    print("Your are still little for those task")
