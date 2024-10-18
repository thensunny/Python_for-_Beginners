#Recursion is like a mirror reflecting itself. It's when a function calls itself to solve a problem.
# When a function calls itself repeatedly
#print n to 1 backwards
#its work with layar by layer.
def show (n):
    if(n==0): #Base case # Stoping statement
        return  #this is called controlled return
    print(n)
    show(n-1) # recursion function nijeke call kore shate nijeke requirement onujayi updated kore.
#show(5)
show(int(input("Enter the Number: "))) # Here We get input from user.

#return n!
def fact(n):
    if n == 0 or n == 1:  # Corrected indentation
        return 1
    else:
        return n * fact(n - 1)

result = fact(5)  # Store the result in a variable
print(result)  # Print the result
