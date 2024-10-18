#Set is the collection of the unordered items.
#Each elements in the set must be unique and immutable.
# sets is mutable. but element of a set is a immutable
collection={1,2,2,3,4,"hello","hello"} #Duplicate value will be ignored
print(collection)
print(type(collection))

#How to write a empty set.
# collection = {} It will be consider as empty dictionary
collection=set() #This is empty set syntax
print(type(collection))


"""
        Set methods
set.add(el) #adds an element
set.remove(el) #remove the element
set.clean() #empties the set
set.pop() #removes a random value
set1.union(set2)#combination both set values & returns new
set.intersection(set2) #combines common values & return new
"""
collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("Sunny")
print(collection)

#Union & intersection
set1={1,3,4,5}
set2={1,3,5,4,3,6}
print(set1.union(set2))
print(set1.intersection(set2))