import random
import string #Eita use kore print korle small and capital letter er a theke z porjonto print hobe.

pass_len=12
charValues= string.ascii_letters + string.digits + string.punctuation
print(random.choice(charValues))

password=""
for i in range(pass_len):
 password+=random.choice(charValues)
print("Your random password is:", password)

# val=random.choice(['a','b',1,2,3])  # Random Choice amader ek ek bar vinno vinno value print kore
# # dei. list er theke  value gula theke.
# print(val)
# Amader password e ki ki use korte pari : A-Z,a-z,0-9,punctuation: %,/ \- #!&$

