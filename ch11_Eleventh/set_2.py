


# Union of set
print("Union")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# same
set4 = set1 | set2
print(set4)



set5 = {"John", "Elena"}
set6 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set5, set6)
print(myset)


myset = set1 | set2 | set5 |set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#Intercestion
print("Intersection")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set4 = set1 & set2
print(set4)

# The & operator only allows you to join sets with sets, and
#  not with other data types like you can with the intersection() method.


#  intersection_update it will change the original set instead of returning a new set.
set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3) 

print("Difference")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
set3 = set1 - set2
print(set3)

set1.difference_update(set2)

print(set1)

# it will change the original set instead of returning a new set. => difference_update




set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print("Not present in both sets",set3)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.

set3 = set1 ^ set2
print("Not present in both sets",set3)
# ^ only for sets
print("Not present in both sets")
set1.symmetric_difference_update(set2)

print(set1)
# it will change the original set instead of returning a new set => symmetric_difference_update