#python can be used to perform operation on a file. (read & write data)

# Types of all files :
# 1. Text Files: .txt, .docx, .log etc. ( We store character here)
# 2. Binary Files : .mp4,.mov, .png, .jpeg etc.  ( Video, photo, store here)
#but when we store any kinds of file in a memory then it store as a Bits.

 #RAM - Random Access Memory  Ekhane just temporary file open hy. System jotokkhn open thake totokkhn file ta ram e thake.
 #File store hy SSD ba HDD te.

                 #We have to open a file before reading or writing
  #f= open("file_name","mode")
 #file_name: sample.txt, demo.docx.        Mode-> r:read mode, w: write mode.
   # If we do not write what mode is it then python by default take it as a read mode.
   # data=f.read() #reads entire file
   # data=f.readline() #reads one line at a time
   # f.close() #for closing file


       #How to open file for reading if my file present in same folder
f = open("text.txt", "r")
data= f.read()
print(data)
print(type(data))
f.close()

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending ( appending means, add somthing in the end), creates the file if it does not exist. ( a b c ache then amra  x y z add korte chiale eita use krbo, output hobe. (a b c x y z).
# "w" - Write (overs write) - Opens a file for writing, creates the file if it does not exist. Eita appending er ulto. ekhane a b c k replace kore x y z write hoie jabe.
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images).
# '+' - open a desk file for updating ( reading and writing )

f = open("text.txt", "r")
data= f.read(5) # 5 characters will be show
print(data)
f.close()
############
f = open("text.txt", "r")
line1= f.readline() # It will be read the just 1 line
print(line1)
line2= f.readline() # It will be read the just 2 line
print(line2)
f.close()

""" Writing to a file """
# f= open("text.txt","w")
# f.write("This is a new line") #overwrites the entire file

# f= open("text.txt","a")
# f.write("This is a new line") # adds to the new file

#write
f= open("text.txt","w")
f.write("I want to learn python in advance level")
f.close()

#append
f= open("text.txt","a")
f.write("\n I want to learn python in advance level")  #\m for new line
f.close()

# r+ ( it will be over write in starting of the line
f=open("text.txt","r+")
f.write("abc")  # Here we overight first 3 character to abc. r+ always overight form beginning
print(f.read())
f.close()
#w+ ( Overight the exciting value
f=open("text.txt","w+") # Here abc overight the entire txt.
f.write("abc")
print(f.read())
f.close()
#a+ ( It will be read and append) it it add value in the end.
f=open("text.txt","a+")
f.write("abc")
print(f.read())
f.close()

                          #   """ With syntax"""
 #with open("text.txt","a")as f:
  #   data =f.read()

with open("text.txt","r") as f:  #as means alias
        data=f.read()
        print(data)

                                  #Deleting a file
      #  using the os module
   # Module (like a code library) is a file written by another programmer that generally has a functions we can use.
   #import os
  #os.remove(file_name)

import os
os.remove("smpl.txt") # This smpl.txt file is deleted.

