chai ='Kartik Sethi'
print("Chai is ",chai)
chai = 'Masala Chai'
print("Chai is ",chai)
first_ch = chai[0]
print("First Char ",first_ch)
slice_chai = chai[:6]
print("0 T0 6th Char ",slice_chai)

last=chai[-1]
print("Last char ",last)

num_list = "0123456789"
print("0 To 7 with skip of 2 ",num_list[0:7:2])
print("0 To 7 with skip of 3 ",num_list[0:7:3])

# Methods on Strings

print("Lower Form ",chai.lower())
print("Upper Form ",chai.upper())

chai = "  Masala Chai  "
print("Space in Chai ",chai)
print("No space Chai",chai.strip())



chai = "Lemon Chai"
print("Chai is ",chai)
chai.replace("Lemon","Ginger")
print("Chai is ",chai)
# String is immutable no change

chai = chai.replace("Lemon","Ginger")
print("Chai is ",chai)


# String To List

chai = "Lemon , Ginger , Masala , Mint "
print(chai.split())
print(chai)
print(chai.split(" , "))
print(chai)

chai = 'Masala Chai'
print("Find Chai",chai.find("Chai"))
print("Find chai",chai.find("chai"))
print("Find Masala",chai.find("Masala"))

chai = "Masala Chai Chai Chai "
print("Find Chai",chai.find("Chai"))
print("Count Chai",chai.count("Chai"))

# -----------------

chai_type = 'Masala'
quantity = 2

order = "I ordered {} cups of {} chai."
print(order)
print(order.format(quantity,chai_type))

# List To String

chai_variety = ['lemon','Masala','Ginger']
print(chai_variety)

print("".join(chai_variety))

print(" ".join(chai_variety))

print("-".join(chai_variety))

print(", ".join(chai_variety))

chai = "Masala Chai "
print(len(chai))

for let in chai:
    print(let)


chai = "\"Masala \nChai\""
print(chai)
chai = r"Masala\nChai"
print(chai)
# Raw string

path = r"c:\user\pwd"
print(path)
# path = "c:\user\pwd" #error
# print(path)
path = "c:\\user\\pwd" 
print(path)


chai = "Masala Chai "
print("Masala" in chai)
print("Masaaaaala" in chai)


