
""" String is a data type  that stores a sequence of Characters
     Basic Operations:
     *Concatenation
               "Hello"+"world" ---> "Helloworld"
     * Length of String
               len(str)
 """
str1="This is a String."
str2='WeSunny'
str3= """ This is a String"""

#for getting new line we will use "Escape sequence Characters"
str1= "This is a String.\n We are creating it in Python"
print(str1)
len(str1)
print(len(str1))

""" Indexing"""  #index helps us to access chacrecters.
 # KHAN MANSION
 # 01234567891011

str= "Khan Mansion"
chr=str[3]
print(chr)

""" Slicing """
#Accessing Parts of a String.
str= "Khan Mansion"
sl=str[5:8] # Index 5 to 7 will be print. all time 1 index beshi likhte hobe.
print(sl)

#Negative Index ( Backward counting)
str="Apple"
print(str[-5:-2])

""" String Functions """
#str.endswith("er")
#str.capitalize() this will be capitalizes 1st Character
#str.replace("old","new") This will replace new value to old value
#str.find(word) It will find the mentioning word
#str.count("am") How many time this "am" exist in the string it will be check this.
#there are lots of functions for using with string
str = " I am a studing python from Premier University Chittagong"
print(str.replace("python","JavaScript"))

str = " I am a studing python from Premier University Chittagong"
print(str.find("Chitta"))

str = " I am a studing python from Premier University Chittagong"
print(str.count("on"))