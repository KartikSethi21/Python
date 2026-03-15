# First memory is assigned then reference is given

username = 'Kartik'
print("Value of username is ",username)
username = "sethi"
print("Value of username is ",username)

x=10
y=x
print("Value of x ",x)
print("Value of y ",y)

x = 15
print("Value of x ",x)
print("Value of y ",y)


user = 'sethi'
user2 = user
print(f"user1 is {user} and user2 is {user2}")
user[0]='b' #'str' object does not support item assignment
print(f"user1 is {user} and user2 is {user2}")
