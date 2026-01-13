import sys
kar=2
a=sys.getrefcount('kar')
print(a)

# Python does not have datatype. we does not assign data type in variable
# -----------------------explain
# Python variables do not have data types; they are references to objects. 
# The objects stored in memory have data types, which are determined at runtime.

x = 10
y = "hello"
z = 3.14
print(type(x))    # <class 'int'>
print(id(x))      # memory address (implementation detail)
# x → [ int object (10) ]
x = 10
x = "hello"
# Before:
# x → [ int 10 ]
# After:
# x → [ str "hello" ]

# Reference

a=1
print("Value of a is ",a)
a=a+1
print("Value of a is ",a)

myListOne = [1,2,3]
print("List1 is ",myListOne)
myListTwo = myListOne
print("List2 is ",myListTwo)
myListOne = 'chai'
print("List1 is ",myListOne)
print("List2 is ",myListTwo)

myListOne = [1,2,3]
# myListTwo = myListOne
myListOne[0] = 33
print("List1 is ",myListOne)
print("List2 is ",myListTwo)


myListOne = [1,2,3]
myListTwo = myListOne
myListOne[0] = 23
print("List1 is ",myListOne)
print("List2 is ",myListTwo)

# ---------------------------------
p1=[1,2,3]
p2 = p1
p2 = [1,2,3]
print("P1 LIST ",p1) 
print("P1 LIST ",p2)
p1[1] = 55
print("P1 LIST ",p1) 
print("P1 LIST ",p2) 

# MAKING A COPY => slicing
h1 = [1,2,3]
h2 = h1[:]
print("H1 LIST ",h1)
print("H2 LIST ",h2)
h1[0]=231
print("H1 LIST ",h1)
print("H2 LIST ",h2)


# Using Copy

import copy 
g1 = [1,2,3]
g2 = copy.copy(g1)
print("G1 List is ",g1)
print("G2 List is ",g2)
g1[2]=76
print("G1 List is ",g1)
print("G2 List is ",g2)


g1 = [1,2,3]
g2 = copy.deepcopy(g1) # for list inside list

print("G1 List is ",g1)
print("G2 List is ",g2)
g1[2]=76
print("G1 List is ",g1)
print("G2 List is ",g2)



# How to compare 

n=[1,2,3]
m=n
print("If  m==n",m==n)
print("M IS n",m is n)
n = [1,2,3]
print("If  m==n",m==n)
print("M IS n",m is n)

#  IN python we have dynamic reference type, variable does not have info of data type
