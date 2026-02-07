# f = open("even.py")
f = open("13_Thirteenth/even.py","r")
print(f.readline())
print(f.readline())
print(f.readline())
# gives empty string at ends if we try to read file after end

 #raw method behind readline()
print(f.__next__())
print(f.__next__())
# gives error when file ends and we try to read the file


# iterables
for line in open("13_Thirteenth/even.py").readlines():
    print(line,end="")
# readlines() reads the entire file into memory
# Returns a list of strings
# Then the loop iterates over that list

for line in open("13_Thirteenth/even.py"):
    print(line,end="")
# Python reads the file line by line (lazy loading)
# Only one line is in memory at a time

while True:
    line = f.readline()
    if not line : break
    print(line,end="")


# Full file

# with ==> “Open the file, use it, and guarantee it gets closed.”

with open("13_Thirteenth/even.py") as f: #This is called a context manager
    print(repr(f.read()))

# 'hello\nworld' with repr instead of  >>hello >>world


f.close()