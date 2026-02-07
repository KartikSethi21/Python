mylist = [1,2,3,4,5]
i = iter(mylist)   # creates an iterator object
print(i)
print(i.__next__())
print(i)
print(i.__next__())
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
# print(i.__next__()) error list ends


# how for loop works

for x in mylist:
    print(x)


it = iter(mylist)
while True:
    try:
        x = next(it) #it.__next__()
        print(x)
    except StopIteration:
        break


# Dictionary
print("\nDictionary")

d = {'a':1,'b':2}

for key in d.keys():
    print(key)

i = iter(d)
print(i)
print(next(i))
print(next(i))


print("\nRange")
r = range(0,10)
i = iter(r)
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())