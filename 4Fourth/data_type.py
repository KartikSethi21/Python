username = 'kartik'
print("Length of username is ",len(username))

print("First Letter ",username[0])

# username[0]= "J"
# TypeError: 'str' object does not support item assignment


print("First Letter ",username)
print("Last Letter ",username[-1])
print("Second Letter ",username[0])

# username[-1] ='k'
print(username[1:3])
# print(dir(username))


# ------------LIST => Array

myList =[123,'chai',3.12]
print(myList)
print(myList[0])
myList[0]='Kartr' #Mutable
print(myList)

# Dictionary
myD = {'one':'lemon','two' :"ginger",'comic':"Marvel"}
print(myD)
print(myD['comic'])
myD['one']='kal'
print(myD)


# Tuples
myTup = (1,2,3,4)
print(myTup)
print(myTup[0])
print(len(myTup))
# myTup[0]=23
# TypeError: 'tuple' object does not support item assignment