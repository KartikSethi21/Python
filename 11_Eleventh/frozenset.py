x = frozenset({"apple","banana","cherry"})

print(x)
print(type(x))


# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

b = x.copy()
print(b)
print(id(x) == id(b)) 
# same reference
# shallow copy
del b
print(x)
# here only b is removed x still points to frozenset as del delte variable

b = {"apple","banana","cherry"}
c = b-x
print("Difference",c)
f = b.difference(x)
print("Difference",f)
g =b.intersection(x)
print("Intersection",g)
# &

t = b.isdisjoint(x)
print("wheter 2 frozenset have no intersection",t)
# Returns True if this frozenset is a (proper) subset of another
gh = b.issubset(x) 
#b==x or b<=x b {1,2}, x = {1,2,3} => true
print("is b a subset of x",gh)
hg = b.issuperset(x)
print("Is b suberset of x",hg)
l = {"roti","rice","dosa"}
v = b.union(l)
print("Union ",v)

# Not present in both set => symmetric difference
sd = b.symmetric_difference(l)
print("symmetric difference ^",sd)

