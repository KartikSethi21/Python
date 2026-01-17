# A set is a collection which is unordered, unchangeable*, and unindexed.
#A set is an unordered collection of unique elements.


thisset ={'apple','bannana','cherry','apple'}
print(thisset)
# will automatically remove apple no error

# print(thisset[0])
# TypeError: 'set' object is not subscriptable



thisset ={'apple','bannana','cherry','apple',True,"True",1,2}
# thisset ={'apple','bannana','cherry','apple',1,True,"True",2} => will remove True

print(thisset)

thisset ={'apple','bannana','cherry','apple',0,True,False,2,3} 
print(thisset)

print("Length ",len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print("String ",set1)
print("Number ",set2)
print("Boolean ",set3)


set4 = {"abc", 34, True, 40, "male"}
print("Mixed ",set4)
print(type(set4))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

for x in thisset:
    print(x)

print("is cherry in set","cherry" in thisset)

print("Is banana nt in set","banana" not in thisset)


# Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")
print(thisset)

# To add items from another set into the current set, use the update() method.
# The update() changes the original set, and does not return a new set.


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print("Set added in another Set")


print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print("List added in set")
print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset.discard("cherry")

print(thisset)

# If the item to remove does not exist, remove() will raise an error. 
# Not in discard

# POP removes at random
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("Element removed",x)
print(thisset)

# clear to fu;;y empty the array
thisset.clear()
print(thisset)

# Create set using set() function

a = set("abc ddd")
print(a)

# To delete the set completely
thisset = {'apple','banana','mango'}
del thisset
# print(thisset) 
# error not defined




# Because the set changes its contents, not the identity of the elements stored inside it.
# {{},{},{}} =>error
# A set is a hash table (same idea as a dictionary).
# For each element:
# Python computes hash(element)
# Uses that hash to decide where to store it
# Later uses the SAME hash to find it again

