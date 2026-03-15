# count positive numbers in list
a = [1,2,3,4,4,-9,-8,-2]
print(a)
count=0
for i in a:
    if i<0:
        count+=1

print(f"Number of negative numbers are {count}")

