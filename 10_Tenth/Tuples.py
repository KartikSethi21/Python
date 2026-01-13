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

