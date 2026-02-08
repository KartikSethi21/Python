username = 'chai aur code'
def func():
    # print("Inside func use 1",username)
    username = 'Kartik'
    print("Inside func after dec 2",username)

print("Use outside 1",username)
func()
print("Use outside 2 after func call",username)

# How python search
# Local → Enclosing → Global → Built-in
# Local - within function , Enclosing - closest function(nested),global - full code, then built-in like len

x=99
def func2(y):
    z=x+y
    return z
result = func2(1)
print(result)

x=99
def func3():
    global x
    print("Value 1 of x",x)
    x=89
    print("Value 2 of x",x)

print("Value outside 1",x)
func3()
print("Value outside 2",x)

# Nested function
def f1():
    x=99 #enclosing
    def f2():
        print("Inside f2",x) #enclosing
        return x
    return f2

myresult = f1()
a=myresult() # value of x
print(a) # value of x


def f1():
    c=99
    def f2():
        nonlocal c
        print("Inside f2 nonlocal",c)
        c=78
        return c
    return f2

myresult = f1()
a=myresult() # value of x
print("nonlocal",a) # value of x

# why not use global 
# becoz global will tell to look from whole module and no c in whole module tus error
# nonlocal tells => “Use c from the nearest enclosing function, not local”



def chaicoder(num):
    def actual(x):
        return num**x
    return actual

a = chaicoder(7)
print(a)
b = a(2)
print(b)
g = chaicoder(2)
print(g(2))