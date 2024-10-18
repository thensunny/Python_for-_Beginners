# This is python mini project
# Here, Software give you a random number, then you have to guess the number

   # here random is a inbuild python module
import random
target = random.randint(1,100)

while True:
   userChoice= (input("Guess the target or Quit(Q): "))
   if(userChoice == "Q"):
      break
   userChoice = int(userChoice)
   if (userChoice==target):
      print("Success: Correct Guess!!")
      break
   elif (userChoice < target):
      print("Your number was too small. Take a bigger guess..")
   else:
      print("your Number was too Big.. Take a smaller guess..")

print("------Game Over------")