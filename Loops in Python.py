# Loops are used to repeat instruction
#  1. While Loops 2. For Loops
#
#  while Loops syntax -->
#      while Condition:
#          #some  work

 #Manually
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

 #Using While Loop
count = 1  # Initialization ( Means, J value ta diye amra start korchi)
while count <= 6:  #Stoping Condition
    print("Hello")
    count += 1  # Ekhane 1,2,3.. Eivabe count hocche shate value increase hocche.
    # Loops e run hoa k iteration. 1 Iteration means 1 loop complete.
print(count)

#
count = 1  #Iterator
while count <= 6:
    print("Hello",count)
    count += 1
print(count)

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

# Break & Continue in Loops
#Break : Break key word amra loop er jekhanei use krbo, loop okhanei terminate( bndh ) hoie jabe.
i=1
while i<=5:
    print(i)
    if (i==4):
        break
    i+=1
print("This Loop is End")

#Continue: Terminates execution in the current interation & continues execution of the loop with the next iteration.
       # Break er opposite

i=1
while i<=6:
    print(i)
    if (i==4):
        i+=1
        continue #Skip  # 4 print naa kore loop continue krbe then 4 er porer gula print krbe
    print(i)
    i+=1

#Continue use kore Even and Odd number print
i=1
while i<=10:
    if (i%2==0):
        i+=1
        continue #Skip all even number
    print(i)
    i+=1
#
    i = 1
    while i <= 10:
        if (i % 2 != 0):
            i += 1
            continue  # Skip all odd number
        print(i) #even numbers
        i += 1

        """ For Loops """
        # For loops are used for sequential traversal. For traversing list,string,tuples etc.
        # For loops syntax :
        #                    for element in list:   (Here for and in is key)
    #                       else: (it is optional)

        nums=[1,3,4,5,6]

        for val in nums:
            print(val)

#
nums=["Poteto", "Banana","Apple","Mango","Lichy"]
for val in nums:
    print(val)


#                    """ Range ()"""
#    Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stop before a specified number.
# range(start?,stop,step?)
#    sequence = range(5)
#    print(sequence[0])
#    print(sequence[1])
 #example with for loop in Range

for i in range(10):  # range (stop)
    print(i)

for j in range(2, 10):  # range(start, stop)
    print(j)

for k in range(2, 10, 2):  # range(start, stop, step)
    print(k)


  """ pass Statement """
 #pass is a null statement that does nothing.It is used as a placeholder for future code.
 # for el in range(10):
      # pass
 # code ta run na koriye nicher poroborti code gula run korbe but error dibe na.

for i in range(5):
    pass

print("Here we skip the for loop using pass statement")
