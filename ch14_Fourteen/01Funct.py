import math

# Square of 2 numbers
def square(n):
    print(n**2)
r = square(4)
# print(r) #None

# better
def sq_2(b):
    return b**2

a = sq_2(5)
print("Square is",a)

# Sum of 2 numbers
def sum(a,b):
    return a+b

print("Sum is",sum(5,7))

# Multiply 2 numbers

def mult(a,b):
    return a*b
print(mult(2,3))
print(mult('a',3))
print(mult(2,'b'))



# Circle area and circumference

def circle(r):
    area = math.pi * (r**2)
    peri = 2* math.pi *r
    return area,peri

a,c = circle(3)
print("Area is",a)
print("Circumference is",c)


# Greet user
def greet(name="User"):
    return "Hello, "+name+"!"

print(greet("Kartik"))
print(greet())


# Lambda Function

cube = lambda x:x**3
print("Cube is",cube(3))

even = lambda y:y%2==0
print("Is Even",even(41))

