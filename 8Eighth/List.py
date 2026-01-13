tea = ['Black','Green','OOlong','White']
print(tea)
print("Value at index 0 ",tea[0])
print("Value at index -1 ",tea[-1])
print("Slicing from 1 to 2 ",tea[1:3])
print("Slicing from 0 to 1",tea[:2])
print("Hopping by 1",tea[0:4:1])
print("Hopping by 2",tea[0:4:2])

tea[3]= 'Herbal'
print("New Tea",tea)

print(tea[1:2] )
tea[1:2]='Lemon'
# Left side: a list slice
# Right side: an iterable
print(tea)
tea = ['Black','Green','OOlong','White']
print(tea)
tea[1:2]=['Lemon']
print(tea)
# tea[1:3]=['Lemon']
# print(tea)
tea[1:3]=['Lemon','Bannana']
print(tea)

print("Empty tea ",tea[1:1])

tea[1:1]=['test','test']
print(tea)
# tea[1:2]=['test','test']
# print(tea)

print(tea[1:2])
print(tea[1:3])
tea[1:3]=[]
print(tea)


# For Loop
for i in tea:
    print(i)

for i in tea:
    print(i,end='-')

# By Default
# for i in tea:
#     print(i,end='\n')
print("\n")
if "Oolong" in tea:
    print("I have Oolong tea")
if "White" in tea:
    print("I have White tea")
tea.append("Oolong")
if "Oolong" in tea:
    print("I have Oolong tea")

tea.pop()
print(tea)
tea.remove("Bannana")
# If not in the list then gives error

print(tea)

tea.insert(1,"Mango")
print(tea)
tea_copy = tea # same reference
tea_copyed = tea.copy() # Different Reference
tea_copyed.append("Kashmirir")
print("Tea is ",tea)
print("Tea Copyed is ",tea_copyed)
tea_copy.pop()
print("Tea is ",tea)
print("Tea copy is ",tea_copy)

squared_nums = [x**2 for x in range(10)]
print(squared_nums)
print(range(10))
# range(10) is NOT a list
# It is a range object
# It generates numbers lazily (on demand)
print(list(range(10)))
print([range(10)]) # [range(0, 10)]

cube_y = [y**3 for y in range(0,13,3)]
print(cube_y)
