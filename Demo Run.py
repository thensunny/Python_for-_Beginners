import random
target=random.randint(1,100)
while True:
     userChoice=(input("Guess the number or Quit (Q): "))
     if(userChoice == "Q"):
        break
     userChoice=int(userChoice)
     if(userChoice==target):
         print("Success: Correct Guess")
         break
     elif(userChoice<target):
         print("Your guessing number is too small, Take a bigger guess ..")
     else:
         print("Your guessing number is to big, Take a smaller guess ..")
print("-----Game Over------")



