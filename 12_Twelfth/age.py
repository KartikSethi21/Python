underscore = input("Enter the total score obtain ")
print(underscore)
# print(underscore/2) #=> error str/2

a = int(underscore)
print(a)
print(a/2)

age = int(input("Enter your age "))
print("Category is ")

if age<13:
    print("Child")
elif age<20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")

if age<13:
    print("Child")
elif 13<=age and age<20:
    print("Teenager")
elif 20<=age and age<60:
    print("Adult")
else:
    print("Senior")




