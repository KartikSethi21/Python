# $12 => adults (18 and over)
# $8 =>children
# $2 discount on wednesday

age = int(input("Enter your age "))
day = input("Enter the day ")

if age<18:
    charges = 8
else:
    charges = 12

if day == 'Wednesday' or day ==  'wednesday':
    charges = charges-2
print("Total Charges are $",charges)

# or 
price = 12 if age>18 else 8

if day.lower()=='wednesday':
    price-=2
print(f"Total Charges are ${price}")

# Wednesday, WEDNESDAY, wEdNeSdAy
# day.lower handles all cases

# no ? : in python


check = 5 if age < 12 else 10 if age < 60 else 7
print("Check this value",check)
# if age < 12:
#     price = 5
# elif age < 60:
#     price = 10
# else:
#     price = 7
price =(12 if age>18 else 8) - (2 if day.lower() == 'wednesday' else 0)
print(f"Total Charges are ${price}")