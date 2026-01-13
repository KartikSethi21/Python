a = 40+ 23.32
print(a)
b = float(40)
print(b)

c = int(2.23)
print(c)

# Operator Overloding
x = 'chai'+'code'
print(x)

x=2
y=3
z=4
print(x,y,z)
print(x+1,y*2,z)
print(y%2)
print(z**2)
print(100**2)
print(2**100)
# print(2**1000)

result = 1/3.0
print(result)


print(repr('chai')) # shows developer version how it is shown in code 
print(str('chai'))  # readable version
print('chai')  # uses str obj.__str__()

print("is 1<2 ",1<2)
print("is 1>2 ",1>2)
print("is 5.0 == 5.0 ",5.0 == 5.0)
print("is 4.0 != 5.0 ",4.0 != 5.0)
print("is x<y<z ",x<y<z) # x<y and y<z

print("is 1==2<3 ",1==2<3)  # 1==2 and 2<3 => False and True => False

# MAths

import math
a = math.floor(3.5)
print("Lowest value to 3.5 round off ",a)
a = math.floor(-3.5)
print("Lowest value to -3.5 round off ",a)
a = math.floor(3.6)
print("Lowest value to 3.6 round off ",a)



b = math.trunc(2.8)
print("Trunc value takes towards zero ",b)
b = math.trunc(-2.8)
print("Trunc value takes towards zero ",b)


# Complex Number

k = 2+1j
print(k)

k = 2+1j*3
print(k)
k = (2+1j)*3
print(k)

# Number type

print(oct(64))
print(hex(64))
print(bin(64))
print("Integer value ",int(64))
print("Octal value ",int('64',8))
print("Hexal ",int('64',16))
print("Binary value ",int('11100010101',2))

# Bitwise Operator
x=1
print("Value of x ",x)
print("Value of x<<2 ",x<<2) # x << n  ==  x × (2ⁿ)
print(x)
print("Value of x|2 ",x|2) # 001 | 010 = 011 = 3
x=4
print("Square root of x is ",x ** 0.5)

# random

import random
a = random.random()
print(a)

a = random.random()
print(a)

a = random.randint(1,10)
print(a)
a = random.randint(1,10)
print(a)


li = ['lemon','masala','ginger','mint']
print(li)
x = random.choice(li)
print(x)
# Selects ONE random element from the list
a =random.choice(li) #random on your choice of value
print(a)

# Randomly rearranges (shuffles) the list in-place
# It modifies the original list
g = random.shuffle(li)
print(g) # => returns None
print(li)

# Decimal Context Manager


print(0.1+0.1+0.4)
print(0.1+0.1+0.1)

from decimal import Decimal
print(Decimal('0.1') +Decimal('0.1')+ Decimal('0.1'))

from fractions import Fraction
myFra = Fraction(2,7)
print(myFra)


# Sets
setOne = {1,2,3,4}
print(setOne&{1,3})
print(setOne|{1,3,7})
print(setOne-{1,2,3,4})
print(type({}))
print(type(True))

print(type(setOne))
s = {}      # ❌ NOT a set
s = set()   # ✅ correct empty set


print("True ==1 ",True ==1)
print("False ==0 ",False ==0)
print("True is 1 ",True is 1 )
print("True+4 ",True is 1 )
