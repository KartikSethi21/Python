# List Mutable Data Types
# Tuples are Immutable


tea_types = ('Black','Green',"Oolong")

print(tea_types)
print("Value at index 0",tea_types[0])
print("Value at  index -1",tea_types[-1])
print("Value from 1 till end ",tea_types[1:])

# tea_types[0] = "Lemon"
# TypeError: 'tuple' object does not support item assignment    
# print(tea_types)

print(len(tea_types))

more_tea =('Herbal','Earl Grey')
alt_tea = more_tea + tea_types 
print(alt_tea)
print(type(alt_tea))

if "Green" in alt_tea:
    print("I have green tea")


# extra =('Earl Grey') Will be treated as a string 
# Parentheses are only for grouping expressions
# There is no comma, so Python sees just a normal string inside brackets

extra =('Earl Grey',)
alt_tea2 = alt_tea + extra
print(alt_tea2)
print(alt_tea2.count('Earl Grey'))
print(alt_tea2.count("Indian"))

alt_tea = alt_tea + extra
print(alt_tea)
print(alt_tea.count('Earl Grey'))
print(alt_tea.count("Indian"))


# Unwrap Tuples
(a,b,c) = tea_types
print(a,b,c)

# Nested Tuple

g = ("1",(1,2,3),"Kart",'c')
print(g)
print(type(g[0])) #str

ind = g.index("Kart")
print("Index of \'Kart\'",ind)