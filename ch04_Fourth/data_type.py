username = 'kartij'
print("Length of username is ",len(username))

print("First Letter ",username[0])

# username[0]= "J"
# TypeError: 'str' object does not support item assignment


print("Full Name ",username)
print("Last Letter ",username[-1])
print("Second Letter ",username[1])

# username[-1] ='k'
print(username[1:3])
print(dir(username)) #tell all the operartions that can be perform on the variable=> datatype


# ------------LIST => Array

myList =[123,'chai',3.12]
print(myList)
print(dir(myList))
print(myList[0])
myList[0]='Kartr' #Mutable
print(myList)
resu = myList.__add__(['sethi'])
print("Old List ",myList)
print("New List ",resu)


# Dictionary
myD = {'one':'lemon','two' :"ginger",'comic':"Marvel"}
print(myD)
print(myD['comic'])
myD['one']='kal'
print(myD)
del myD['comic'] #remove key - value
# myD.pop('comic') # return the value
print(myD)


# Tuples
myTup = (1,2,3,4)
print(myTup)
print(myTup[0])
print(len(myTup))
# myTup[0]=23
# TypeError: 'tuple' object does not support item assignment