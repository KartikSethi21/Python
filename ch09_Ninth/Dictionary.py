chai_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
print(chai_types)
a = chai_types['Masala']
print("At Masala we have",a)
b = chai_types.get('Ginger')
print("At Ginger we have",b)

# Error
# c=chai_types["Greeen"]
# print("At Greeen we have",c)

chai_types['Green']="Fresh"
print(chai_types)

print("Keys are ")
for chai in chai_types:
    print(chai)
print("Keys and Values ")
for chai in chai_types:
    print(chai,chai_types[chai])

print("Key and Values Using .items() ")
# chai_types.items() => getting types
for key,values in chai_types.items():
    print(key,values)
 
if "Masala" in chai_types:
    print("I have Masala")

print(len(chai_types))

chai_types["Early Grey"] = "Citrus"
print(chai_types)

# Returns the value of that key
a =chai_types.pop('Ginger')
print(a)
print(chai_types)

# Returns a tuple (key, value)
b = chai_types.popitem()
print(b,type(b))
# Delete Last Item
print(chai_types)

del chai_types["Green"]
print(chai_types)

# Copy Value
chai_types_copy = chai_types.copy() # Diff Reference
chai_types_c2 = chai_types # same reference

print("Copy with ref",chai_types_c2)
print("Copy without ref",chai_types_copy)

# List in List
a  = [[],[],[]]
print(a)
a[0].append(1)
print(a) 

b = [{},{},{}]
print(b)
b[1]["chai"] = "ginger"
print(b)

# c = {{},{},{}}
# print(c)
# {} means dictionary, not set
# Sets can only contain hashable (immutable) elements
# Dictionaries are mutable → unhashable

tea_shop = {
    "chai":{"Masala":"Spicy","Ginger":"Zesty"},
    "Tea": {"Grren":"Mild","Black":"Strong"}
}
print("Dictionay inside Dictionary")
print(tea_shop)

print(tea_shop['chai'])
print(tea_shop['chai']['Ginger'])

squared_num = {x:x**2 for x in range(10) }
print(squared_num)

squared_num.clear()
print(squared_num)

keys = ["Masala","Ginger","Lemon"]

default_values = "Delicious"

new_dict = dict.fromkeys(keys,default_values)

print(new_dict)

new_dict.clear()
print(new_dict)

new_dict= dict.fromkeys(keys,keys)
print(new_dict)



n = int(input())
student_marks = {}
for _ in range(n):
     name, *line = input().split()
     scores = list(map(float, line))
     student_marks[name] = scores
query_name = input()            



if __name__ == '__main__':
    N = int(input())
    lst = []

    for _ in range(N):
        parts = input().split()
        cmd = parts[0]

        if cmd == "print":
            print(lst)
        else:
            args = list(map(int, parts[1:]))

            operations = {
                "insert": lambda: lst.insert(args[0], args[1]),
                "remove": lambda: lst.remove(args[0]),
                "append": lambda: lst.append(args[0]),
                "sort": lambda: lst.sort(),
                "pop": lambda: lst.pop(),
                "reverse": lambda: lst.reverse()
            }

            operations[cmd]()